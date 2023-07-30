# Discord Bot

# 開発者との約束

- このコードを使い、悪用はしないでください。

- ライセンスを厳守してください。

- **このコードを使って起きた全ての問題の責任は一切追わないものとします。**

**これらの約束を破ったら、やむを得ず、公開を中止する可能性があります。**

# 環境

このコードを実験した時の各バージョンは以下の通りです。

**Python 3.11.1**
**discord.py 2.2.3**

# 用意

- パソコンがあること

- Pythonがパソコンに入っていること

- Discord Botが既にDiscordサーバーに参加していること

# ダウンロード

Pythonのこちらからダウンロードしてください。
https://www.python.org/downloads/

# ステップ1

Discord.py をダウンロードしよう。
**Pythonがパソコンに入っている状態でダウンロードを行ってください。**
**Pythonがパソコンに入ってない場合、ダウンロード出来ません。**
- コマンドプロンプトに「 pip install discord.py[voice] 」と入力し、ダウンロードしてください。

# ステップ2

BotのTOKENを入れよう
**TOKEN は絶対に他の人に見せたり、公開したりしないでください。**
- **TOKEN.py**へ行き、BotのTOKENを入れてください。

# ステップ3

ステータスを設定してみよう
- Botのステータスを設定してみましょう。
**main.py**へ行きやや下にスクロールします。

'''

  await client.change_presence(status = discord.Status.online, activity = discord.Activity(name="discord.py Discord Bot", type=discord.ActivityType.playing))

'''

このようなコードがありますが
- まず **discord.Status.online** を設定しましょう。

このコードはBotのステータスを設定する所です。

-ステータスをオンラインにしたい場合

discord.Status.online

-ステータスを退席にしたい場合

discord.Status.idle

-ステータスを取り込みにしたい場合

discord.Status.dnd

に書き換えてください。
これらを変更することで、Botのステータスを変えることができます。

続いて
- **name="discord.py Discord Bot"** の所を設定しましょう。

このコードはBotのカスタムステータスを設定する所です。

"discord.py Discord Bot" のところを好きな文章に変えてください。

これらを変更することで、Botのカスタムステータスを設定することができます。

続いて
- **discord.ActivityType.playing** を設定しましょう。

このコードはBotのステータスのプレイ中となっている所を設定する所です。

- プレイ中 にしたい場合

discord.ActivityType.playing

- 再生中 にしたい場合

discord.ActivityType.listening

- 視聴中 にしたい場合

discord.ActivityType.watching

- 参戦中です にしたい場合

discord.ActivityType.competing

に書き換えてください。
これらを変更することで、Botのステータスのプレイ中などを設定することができます。

続いて
- 配信ステータス設定と配信中にしたい場合

配信ステータス設定と配信中に設定したい場合は

'''

  await client.change_presence(status = discord.Status.online, activity = discord.Activity(name="discord.py Discord Bot", type=discord.ActivityType.playing))

'''

このコードから

'''
  await client.change_presence(activity = discord.Streaming(name="discord.py Discord Bot", url="https://www.twitch.tv/Nooooooo_0328"))

'''

に変更します。

カスタムステータスの変更は先程説明したやり方と同じです。

urlに関しては、例として開発者のTwitchのプロフィールURLを書いていますが、自分のプロフィールURLに書き換えても問題ありません。

これらを変更することで、Botのステータを配信ステータス設定と配信中に設定することができます。

# ステップ4

Botを起動しよう
- **main.py**を実行してBotを起動しましょう。
ログに
「

ログインしました。
6のコマンドを同期をしました。

」と表示されていれば正常に起動しました。

# ステップ5

VC再生を使ってみよう
- mp3又はwavの音声ファイルを`PY-Discord-Bot`フォルダに追加します。
音声ファイル名は基本なんでもいいです。 **(スペースや日本語など入ってると認識されない可能性あり)**
追加したら、**main.py**へ行き、下にスクロールしスラッシュコマンド5 , スラッシュコマンド6 へ行きます。

- mp3 の場合

mp3の場合、スラッシュコマンド5の __/mp3__ のコマンドコードに変更を加えます。

'''
  sources = [discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('voice.mp3'))] # 再生するファイル名  |  mp3
  for source in sources:
      vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
      while vc.is_playing():
          await asyncio.sleep(3)
  await vc.disconnect()

'''

このようなコードがありますが、`voice.mp3`ここを先程追加した音声ファイル名に変更してください。

mp3コマンドの変更は以上です。

- wav の場合

wavの場合、スラッシュコマンド6の __/wav__ のコマンドコードに変更を加えます。

'''
  sources = [discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('voice.wav'))] # 再生するファイル名  |  wav
  for source in sources:
      vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
      while vc.is_playing():
          await asyncio.sleep(3)
  await vc.disconnect()

'''

このようなコードがありますが、`voice.wav`ここを先程追加した音声ファイル名に変更してください。

wavコマンドの変更は以上です。

# 注意

__/join__ コマンドを使い、Botをボイスチャネルに接続している状態で、__/mp3__, __wav__ コマンドを実行するとエラーになります。
そのため、この場合 __leave__ コマンドを使い、ボイスチャネルからBotを切断してから __/mp3__, __wav__ コマンドを実行してください。


# 質問

以下のサーバー( Nooooooo Program Project Server )に参加して質問してみてください。
なお、質問内容は「 Discord.py 」に**関する**ことのみ、お答えいたします。
**「 Python 」に関する質問はお答え出来ません。**
https://discord.gg/ZmRRppmEtA