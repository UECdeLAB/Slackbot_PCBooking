---
theme : "sky"
transition: "slide"
---

# Python勉強会

> Auther: Takato Ikezawa

---

# インストール

--

Pythonを動かすためには

+ 実行環境, エディタを入れる
+ 統合開発環境を入れる
+ Webで動かす

--

### 自分のエディタを使いたい人

1. Pythonをダウンロード
   + Python 3.9.
2. エディタのインストール
   + VSCode など
3. 設定
   + 拡張機能を入れる || 手動でセットアップ

--

### 楽をしたい人

Anacondaをインストール

--

### とりあえずPythonを実行したい人

Paizaを使用する

https://paiza.io/ja/projects/new?language=python3

---

## Pythonとは

+ 豊富な言語資産
+ 低い学習コスト
+ 何でもできる汎用性

--

## プログラム

+ コンピューターで実行できる手順書
+ コンピューターが理解できる形式で書かれている
  + 機械語 : 0x90,0x90...
  + インタプリンタ
+ 本質はデータをどのような手順で操作するか

```python
print("Hello world!")
```

--

## 変数

+ プログラム上で扱うデータ
+ 数、文字列、オブジェクト...
+ 演算と代入で加工をしていく

```python
100,0x11,"Hello",File
+_/*, <<,>>,||
```
--

## 関数

+ 処理の単位
+ ひとまとまりの処理について
  + 名前を付ける
  + データの存在範囲を決める
  + 再利用可能にする

```python
def sayHello(name):
    print("Hello, this is "+name)
    print("good weather")
    return "OK"
```

--

## 配列

+ 変数のかたまり
+ 大量のデータを扱う為のデータ形式

```python
array = [1,2,3,4,5,6,7]
print(sum(array))
```

--

## 制御構文

+ if文
  + 条件分岐
+ for文
  + ループを行う

---

## Class

+ 変数と関数をまとめるためのモノ
+ 現実のものと対応付けることで分かりやすく
+ データを効率的に扱える

```
class File:
    data = []
    name = "FileName.txt"
    created = "2021-02-24 14:13:44"

    def read():
        return data
    
    def write(data):
        self.data = data
```

---

## ライブラリ

+ 言語の資産
+ エンジニアが再利用可能なコードを配布してくれている
  + 機械学習
  + 画像解析
  + ネットワーク通信


---

## 文字列処理

+ 文字列
    + 文字の配列
    + 処理する関数
    + 付随するデータ

--

+ 結合
  + `"python"+"勉強会"`
+ 繰り返し
  + `"a"*3`
+ 置換
  + `"Hello".replace("l","L"))`

---

## アルゴリズム

+ 要はプログラムのこと
+ 特に効率よく問題を解くことのできるプログラム
  + eg. 100人の最大の身長は？
    + 全員で比べるか
    + 最大値を比較するか

---

## 演習

1. 変数の使い方
    + 計算をしてみよう
      + 12345679*81
      + 2の20乗
      + タワー表記の計算(3↑↑3)
    + 文字列処理をしてみよう
      + 学年+名前+一言
      + xを100個連続してみよう
      + "PRINTF"を小文字に変換してみよう
      + "100"+"20"を計算してみよう

--

答え合わせ:計算編

```
print(12345679*81)
print(2**20)
print(3**3**3)
```

--

答え合わせ:文字列処理編

```
print("池澤"+"B3"+"セキュリティ専攻")
print("x"*100)
print("PRINTF".lower())
print(int("100")+int("20"))
```

---

2. 関数
    + 引数を足し合わせる関数
    + 三角形の面積を計算する関数
    + 総乗を計算する関数

--

答え合わせ:引数を足し合わせる

```
def add(x,y):
    return x+y
    
print(add(1,2))
print(add("aaa","bbb"))
```

--

答え合わせ:三角形の面積を計算する関数

```
def rectArea(border,height):
    return border*height/2
    
print(rectArea(1,2))
```

--

答え合わせ:総乗を計算する関数

```
def mul(n):
    ret = 1
    for i in range(n):
        ret = ret * (i+1)
    return ret
    
print(mul(10))
```

---

3. クラス
    + 3D CADメンバーを設計
      + 要素
        + 名前
        + 学年
        + 勤務時間...
      + 動作
        + MTGに参加する...

--

答え合わせ:3D CADメンバー

```
class CADMember:
    name = "池澤 隆人"
    grade = "B3"
    workingHours = 24.5
    tasks = []

    def joinMTG(self):
        print(self.name+"がMTGに参加しました")
    def addTask(self,task):
        print("新しいタスクだよ！")
        self.tasks.append(task)
        print(self.tasks)
    def finishAllTask(self):
        print("お疲れ様!")
        self.tasks.clear()
        
member = CADMember()

member.joinMTG()
member.addTask("NE250J Spreadsheet Management")
member.addTask("ACD2B HeatMap")

```

---

4. ライブラリの仕様
   + mathライブラリ
     + sinを計算してみる
   + randomライブラリ
     + 乱数を計算してみる
     + じゃんけん関数の作成

--

答え合わせ:sinを計算してみる

```
import math;

print(math.sin(math.pi/2))
print(math.sin(math.pi/4))
print(1/math.sqrt(2))
```

--

答え合わせ:乱数を計算してみる

```
import random;

print(random.random())
```

--

答え合わせ:乱数を計算してみる

```
import random;

print(random.random())
```

--

答え合わせ:じゃんけんをする関数

```
import random;

#じゃんけんをする関数
def RCP123(hand):
    cpuHand = selectHand(random.random())# CPUの手を乱数で決める
    print(hand+" vs "+cpuHand)
    # 簡単に文字列で場合分け
    if(hand==cpuHand):
        return "あいこ"
    if((hand=="グー" and cpuHand=="チョキ") or (hand=="チョキ" and cpuHand=="パー") or (hand=="グー" and cpuHand=="チョキ")):
        return "勝ち"
    else:
        return "負け"

#数字に応じてじゃんけんの手を決める
def selectHand(val):
    min=0
    max=1
    border = (max-min)/3
    if(val<border):
        return "グー"
    elif (val < 2*border):
        return "チョキ"
    else:
        return "パー"
        
print(RCP123("グー"))
```

---

5. アルゴリズム
    + 最小を計算する
    + 素数を計算する

--

答え合わせ:最小を計算する

```
array = [10,2,43,34,6,3,8,-1,3]
min = 100000 #とても大きい数
for x in array:
    if(min>x):
        min = x

print(min)
```

--

答え合わせ:素数を計算する

```
import math;
# エラトステネスのふるい
# 小さい素数で合成数を表から消していく
# [1,2,3,4,5,6,7] => [1,2,3,5,7]...
def hurui(n):
    table = [0]*(n+1) #ゼロ埋めした配列
    # 最初の素数じゃないものはあらかじめ省く
    table[0]=1
    table[1]=1
    root = math.floor(math.sqrt(n+1))
    for i in range(root):
        if(table[i]==0):
            j = 2*i
            while(j<=n):
                table[j]=1
                j=j+i
                
    for i in range(n+1):
        if(table[i]==0):
            print(i)

hurui(30)
```