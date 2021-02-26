---
theme : "sky"
transition: "slide"
---

# Slackbot勉強会

> Auther: Takato Ikezawa

---

### 本題:Slackbotを作ろう

---

### How to do?
ライブラリで簡単に実現!

--

### Step1: ライブラリのインストール

```
> py -m pip install slackbot python-dotenv
```

--

### Step2: APIキーの取得

botアカウントを作成

[https://my.slack.com/services/new/bot]

> 今回は時短のため用意済み

--

### Step3: テンプレートのダウンロード

テンプレートは作成済み

[https://github.com/UECdeLAB/slackbot_template]

ダウンロードしてAPIキーを書き換えればOK

--

### 動作確認

SlackでDMの下にある`App`から**bot_...** を追加

**@bot... こんにちは**とslackbot練習チャンネルで！

---

## 自分流にアレンジ!

### 材料

+ 正規表現
+ コマンドのパース
+ データの永続化
+ ...

--

### 正規表現

文字列を表現する記法

```
*: 任意の文字列
[0-9]{4}:数字4文字
```

これで応答するメンションを制御

--

### コマンドのパース

取得した文字列から木構造を生成

機能ごとに違う関数を呼び出して処理を行う

```
@bot show -> showList()
@bot add -> addElement()
@bot del -> deleteElement()
```

--

### データの永続化

ファイルにデータを書き出す

botを停止してもデータが継続されるように

データベースを使うとデータの管理が簡単に

---

### アイデア

+ メンションリストBot
+ 定期MTG通知Bot
+ ラボ入退室管理Bot
+ TODO管理Bot
+ 進捗報告生成Bot
+ GoogleForm自動報告Bot

---

## Let's ハッカソン!