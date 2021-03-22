# coding: utf-8

#slackbotを作成するためのライブラリ
from slackbot.bot import respond_to
from slackbot.bot import default_reply  
# 今回は使用しない
# from slackbot.bot import listen_to      

# データを保存する為のライブラリ
# py -m pip install datasetで使用できるように
import dataset

# 時間を管理するライブラリ
import time
import datetime

# table.dbというファイルでデータを保存する
db = dataset.connect("sqlite:///table.db")
USER = "users"
BOOKING = "bookings"

MSG_TEMPLATE={
    "promoteRegister":"事前に名前を登録をしてください。\n「I am 名前」で登録ができます。\n再登録も同じ方法です。",
    "resRegistered":"<@%s|username>\n名前を「%s」として登録しました。",
    "usedList":"\n現在以下のPCを使用中です。\n%s",
    "resBooked":"<@%s|username>\n使用申請は正常に処理されました。%s",
    "alreadyBooked":"<@%s|username>\nPC%sは既に%sさんが使用しています。",
    "showListItem":" - PC%s : %s (%sから使用)\n",
    "resShow":"<@%s|username>\n現在の使用状況は以下の通りです。\n%s",
    "resRemove":"<@%s|username>\n使用状況は正常に開放されました。\n%s",
    "help":"<@%s|username>\nメッセージが解釈できませんでした。\n - 「I am 名前」で名前を登録します。\n - 「N使用」でPCのN番を使用を開始します。\n - 「N開放」でPCのN番の使用を停止します。\n - 「開放」ですべてのPCの使用を停止します。\n - 「show」で現在の使用状況を出力します。"
}

# 事前知識
# + データの保存方法
#   + ライブラリを使用して、データの種類を選択、map形式で読み書きを行う
# + map形式
#   + データを名前と値の二つの情報に分け、それの組を保存する形式
#   + 例: name:taro -> key=name, value=taro
#   + このような形式で任意のデータを自由に保存できる
# + Slackbotで取得できる情報
#   + slackbotで呼び出される関数の第一引数(message)にslackbotからの情報がmap形式で入っている
#       + type:イベントの種類(slackbotの場合はmessage),
#       + ts:タイムスタンプ
#       + user:送信元のユーザーのID(以下uid)
#       + text:メッセージの内容
# + uidについて
#   + Slackの内部的なユーザーを識別するID
#   + 「U023BECGF」といった内容で、解釈は不可能、表示名を取得する方法もあると思われるが、自分で苗字なりを登録する形式の方が楽

# 処理を定義していないメッセージに対する応答
# ヘルプメッセージを表示する
@default_reply
def help(message):
    message.reply(MSG_TEMPLATE["help"]%message.body["user"])

# 「I am 名前」とメンションされた場合の応答
# PCの使用者としての名前を更新する
@respond_to('^I am (.*)$')
def addUser(message,name):
    # ユーザーに関するデータを選択
    users = db[USER]
    # 既に存在するユーザーに関するデータをすべて削除
    users.delete(user=message.body["user"])
    # 新しい名前とuidの組を登録する
    users.insert({
        "uid":message.body["user"],
        "name":name
    })
    # Slack側に登録結果を通知
    message.reply(MSG_TEMPLATE["resRegistered"]%(message.body["user"],name),in_thread=True)


# 「N使用」とメンションされた場合の応答(Nは0~9)
# その番号のPCに対する使用情報を登録する
@respond_to('^([0-9])使用$')
def reg(message,pc):
    # 頻繁にuidにアクセスするので、変数に取っておく
    uid = message.body["user"]
    # 未登録の場合は促すその旨を通知する
    if not isRegistered(uid):
        message.reply(MSG_TEMPLATE["promoteRegister"],in_thread=True)
        return
    # 予約に関するデータを選択
    booking = db[BOOKING]
    # 既に予約が存在しないか確認する
    # まず最初に予約リストからpc番号で検索
    bookedRecord = booking.find_one(pc=pc)
    # データが存在した場合はエラーを通知する
    if bookedRecord != None:
        message.reply(MSG_TEMPLATE["alreadyBooked"]%(uid,pc,getUserName(bookedRecord["uid"])),in_thread=True)
        return
    # 予約データを追加する
    booking.insert({
        "uid":uid,
        "pc":pc,
        "timestamp":time.time()
    })
    # 予約済みのリストを作成
    myBooked = getBookedList(uid)
    # Slackに通知する
    message.reply(MSG_TEMPLATE["resBooked"]%(uid,myBooked),in_thread=True)


# 「show」とメンションされた場合の応答
# PCの使用情報を出力する
@respond_to('^show$')
def show(message):
    # 予約に関するデータを選択
    booking = db[BOOKING]
    result=""
    # すべての結果を検索し、一覧で表示する
    for row in booking.find(_limit=10):
        # 予約時に保存したタイムスタンプを処理
        # 日時表記にするために、timestamp -> datetime -> stringと変換する
        timestamp = datetime.datetime.fromtimestamp(row["timestamp"])
        date = timestamp.strftime("%m/%d %H:%M")
        # すべての情報をいい感じに並べる
        result+=MSG_TEMPLATE["showListItem"]%(row["pc"],getUserName(row["uid"]),date)
    if(result==""):
        result = "すべてのPCが未使用"
    message.reply(MSG_TEMPLATE["resShow"]%(message.body["user"],result),in_thread=True)


# 「開放」とメンションされた場合の応答
# すべてのPC使用情報を削除する
@respond_to('^開放$')
def rmAll(message):
    # 頻繁にuidにアクセスするので、変数に取っておく
    uid = message.body["user"]
    # 未登録の場合は促すその旨を通知する
    if not isRegistered(uid):
        message.reply(MSG_TEMPLATE["promoteRegister"],in_thread=True)
        return
    # 予約に関するデータを選択
    booking = db[BOOKING]
    # 自分のIDで登録したデータをすべて削除
    booking.delete(uid=uid)
    # Slackに通知
    message.reply(MSG_TEMPLATE["resRemove"]%(uid,getBookedList(uid)),in_thread=True)


# 「開放」とメンションされた場合の応答
# すべてのPC使用情報を削除する
@respond_to('^([0-9])開放$')
def rm(message,pc):
    # 頻繁にuidにアクセスするので、変数に取っておく
    uid = message.body["user"]
    # 未登録の場合は促すその旨を通知する
    if not isRegistered(uid):
        message.reply(MSG_TEMPLATE["promoteRegister"],in_thread=True)
        return
    # 予約に関するデータを選択
    booking = db[BOOKING]
    # 自分のIDで登録したデータかつ指定したPC番号を削除
    booking.delete(uid=uid,pc=pc)
    # Slackに通知
    message.reply(MSG_TEMPLATE["resRemove"]%(uid,getBookedList(uid)),in_thread=True)


# 名前が登録されているかどうかを判断する
def isRegistered(uid):
    user = db[USER]
    info = user.count(uid=uid)
    # 一つ以上、自分のuidのデータが存在したらtrue
    return info > 0


def getBookedList(uid):
    # 予約に関するデータを選択
    booking = db[BOOKING]
    # 一つも予約データが存在しない場合は何もしない
    if booking.count(uid=uid)==0:
        return ""
    # 一つ以上のデータが存在したら、カンマ区切りで整形する
    booked = ""
    for row in booking.find(uid=uid):
        # 初めの一回はカンマを入れない
        if booked != "":
            booked+=", "
        # PC番号を連結
        booked+="PC"+row["pc"]
    # 最終的にきれいな文字列に埋め込む
    return MSG_TEMPLATE["usedList"]%booked


# 登録名を検索する
def getUserName(uid):
    # ユーザーに関するデータを選択
    user = db[USER]
    # uidで検索して、上位一件を取得
    result = user.find_one(uid=uid)
    # データが存在しない場合は「未登録」
    if result == None:
        return "未登録"
    # それ以外は登録された名前を返す
    return result["name"]
