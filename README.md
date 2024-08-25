# Discord Bot

# 説明

こんにちは！Nooooooo Program ProjectのNoooooooと言います！
主にDiscord.pyを使ってBot開発をしています。
このコードは、手軽にDiscord Botを動かしてみたい方のために開発されました！
PythonとDiscord.pyをインストールし、以下の手順を行い、コードを実行するだけで、簡単にBotを起動させることができます！
初めてBotを起動させた瞬間の喜びは、きっと忘れられない思い出になるでしょう！

# 目的

なぜ、本コードを公開したかと言うと、**プログラミングの面白さを知ってもらうため**です。
初めてコードを実行し、上手くいったときの嬉しさ、感動は忘れられない思い出となると思います！
そこで、1人でも多くの方にこの気持ちを体験してほしい！という気持ちから本コードの公開に至りました。
プログラミングというのは、ただの技術ではなく、自分で考えて形にする物です！
世界に1つだけの機能を作り出すこともできるかもしれません。
プログラミングは無限大です！

**できた！** という達成感を味わうことで、新しい趣味に繋がるかもしれません！

# 機能内容

本コードには、以下の機能が搭載されています！

- 挨拶に返事をする機能(オウム返し)

- P2P地震情報から地震情報を取得して表示するコマンド

# 定義

- 本コードとは、本フォルダ内すべてのコードを指します。

- 開発者とは、Noooooooのことを指します。


# 開発者からのお願い
Botを動かす前に、**開発者からのお願い**があります。
必ずお読みください。

- **本コードを絶対に悪用しないでください。**

- **ライセンスを厳守してください。**

- **本コードの使用によって生じた問題について、開発者は一切の責任を負いません。**

**本コードを悪用したり、ライセンス違反などした場合、公開を停止することがありますので、ご注意ください。**


# 注意

本コードはWindowsで行うことを前提として説明しています。
Windows以外だとやり方など異なる場合があります。

本コードはVisual Studio Codeで行うことを前提として説明してます。
Visual Studio Code以外だとやり方など異なる場合があります。

**Botを常時稼働させる場合はデスクトップパソコンでの稼働を推奨します。
ノートパソコンは常時稼働させるように設計されていません。
最悪の場合、発火や火災の可能性も考えられます。
詳しくは「ノートパソコン 常時稼働 危険性」と検索して、ご確認ください。**

# 用意
続いて、**用意**についてです！
Botを動かすには、以下の用意をしておく必要があります。

- パソコンがあること
Botを動かすには、必ずパソコンが必要になります。

- Pythonがパソコンに入っていること
今回はDiscord.pyを使用するため、Pythonが必要になります。

- Discord Botのアカウントを作り、サーバーに参加させておくこと
Discord Botがサーバーにいないと何もできません！！

- Privileged Gateway Intents がオンになっていること
[Discord Developer Portal (Discord Developer Portalサイトへ飛びます)](https://discord.com/developers/applications)にアクセスし、次の手順で Privileged Gateway Intents をオンにしてください。

1. 稼働するBotを選択します。

2. 左側の「Settings」メニューから「Bot」を選択し、少し下にスクロールします。

3. Privileged Gateway Intents セクションで、以下の3つの項目をオンにします。
- **Presence Intent**
- **Server Members Intent**
- **Message Content Intent**


# 環境
続いて、**環境**についてです！
Botを動かすには、**環境**を構築する必要があります。

開発者が行ったときの各バージョンは以下の通りです。

Python: 3.12.3
Discord.py: 2.3.2


# ステップ1　Pythonをダウンロードしよう！
まず、Botを稼働させるにはDiscord.pyというPyhonライブラリを使うため、Pythonが必要です。

こちらから[Python (Pythonの公式サイトへ飛びます)](https://www.python.org/downloads/)をダウンロードしてください！


# ステップ2　Discord.py をダウンロードしよう！
ここからBotを簡単に動かすことができるDiscord.pyというPythonライブラリをダウンロードします。

**注意**
- 必ずPythonがパソコンに入っている状態でダウンロードを行ってください。

コマンドプロンプトに「 `pip install discord.py` 」と入力して実行し、ダウンロードしてください。


# ステップ3　ソースコードエディタをダウンロードしよう！
Botを動かすには、ソースコードエディタというソフトが必要です。

開発者のおすすめはMicrosoftの**Visual Studio Code**というソースコードエディタです！

こちらから[Visual Studio Code (Visual Studio Codeの公式サイトへ飛びます)](https://code.visualstudio.com/)をダウンロードしてください！

※ダウンロードして初めて開いたときは表示言語が英語になっているはずです。
そのため、まず表示言語を日本語にする必要があります。

1. Visual Studio Codeのサイドバー(左側のバー)にある「Extensions」を選択してください。
   Extensionsを選択すると、検索できるボックスが表示されます。

2. 検索ボックスに「Japanese Language Pack」と検索してください。
   検索結果から「Japanese Language Pack for Visual Studio Code」を選択してください。

3. 「Japanese Language Pack for Visual Studio Code」 の画面が表示されますので、「install」を押して
   インストールしてください。

4. インストールが完了したら反映させるために再起動をします。
    インストール完了後に画面右下に「Change Language and Restart」と表示されるので選択してください。

これで言語を英語から日本語にすることができたと思います。


# ステップ4　コードがるフォルダを開こう！

Visual Studio Codeで左上の「ファイル」を選択し、「フォルダーを開く」を選択し、本コードがあるフォルダを選択します。


# ステップ5　BotのTOKENを入れよう！
さぁ、ここからいよいよコードに改変をしていきます。

**注意**
- TOKEN を絶対に他の人に見せたりしないでください。
Botが乗っ取られる可能性があります。

`PY-Discord-Bot/TOKEN.py`へ行き、BotのTOKENを入れてください。

`Discord_TOKEN = "ここにTOKENを入力"`


# ステップ6　Bot起動！
いよいよBotを起動する時が来ました。

`PY-Discord-Bot/main.py`へ行き、F5を押し、「Python ファイル」を選択し、実行してください。

`BotName (BotID) がログインしました。
6のコマンドを同期をしました。`

とログに出れば起動成功です！おめでとうございます！
本来、`BotName`には稼働させているBotの名前、`BotID`には稼働させているBotのIDが表示されます。


# ステップ7　Botのステータスを設定しよう！

## Botのステータスを設定してみましょう。
`PY-Discord-Bot/main.py`へ行き、31行目に以下のようなコードがあります。

`await client.change_presence(status = discord.Status.online, activity = discord.Activity(name="discord.py Discord Bot", type=discord.ActivityType.playing))`

まず `discord.Status.online` を設定しましょう。

このコードはBotのオンラインステータスを設定するところです。

- ステータスを オンライン にしたい場合

`discord.Status.online`

- ステータスを 退席中 にしたい場合

`discord.Status.idle`

- ステータスを取り込み中にしたい場合

`discord.Status.dnd`

に書き換えることで、Botのステータスを変えることができます。


## カスタムステータスを設定してみましょう。
このコードはBotのカスタムステータスを設定するところです。

**discord.py Discord Bot** のところを好きな文章に変えてください。

これらを変更することで、Botのカスタムステータスを設定することができます。


## Botのステータスのプレイ中となっている部分を設定してみましょう。
このコードはBotのステータスのプレイ中となっている部分を設定するところです。

- プレイ中 にしたい場合

`discord.ActivityType.playing`

- 再生中 にしたい場合

`discord.ActivityType.listening`

- 視聴中 にしたい場合

`discord.ActivityType.watching`

- 参戦中です にしたい場合

`discord.ActivityType.competing`

に書き換えることで、Botのステータスのプレイ中となっている部分を設定することができます。


## 配信ステータスと配信中にしたい場合の設定
`await client.change_presence(status = discord.Status.online, activity = discord.Activity(name="discord.py Discord Bot", type=discord.ActivityType.playing))`

から

`await client.change_presence(activity = discord.Streaming(name="discord.py Discord Bot", url="https://www.twitch.tv/Nooooooo_0328"))`

に変更することで、Botの各ステータスを配信ステータス設定と配信中に設定することができます。

※カスタムステータスの変更は先程説明したやり方と同じです。

URLのTwitchIDの部分に関しては、ご自身のTwitchIDに書き換えても大丈夫です。


# Welcome to the world of programming!!


# 質問

以下のDiscord サーバー( Noachanの雑談サーバー )に参加して質問してみてください。
なお、質問内容は「 Discord.py 」に**関する**ことのみ、お答えいたします。

[参加はこちら](https://discord.gg/Z8aqnkfZCU) 