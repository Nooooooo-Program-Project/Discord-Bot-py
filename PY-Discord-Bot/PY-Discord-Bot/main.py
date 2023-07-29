# ----------------------------------------

#Copyright (c) 2023 Nooooooo Program Project
#Licensed under the Apache License 2.0

# ----------------------------------------


import discord # pip install discord.py[voice]
import TOKEN
from discord import app_commands

# メッセージの内容を受信するためにintents
intents = discord.Intents.default()
intents.message_content = True

# Discordクライアントを作成
client = discord.Client(intents=intents)

# app commandのツリーを初期化
tree = app_commands.CommandTree(client)

# Botが起動した時に発火するイベント
@client.event
async def on_ready():
  print(f'{client.user.name} ({client.user.id}) がログインしました。') # Botがログインした際にメッセージを出力

  try:
    tree_cmd = await tree.sync() # スラッシュコマンドの同期

    print(f"INFO {len(tree_cmd)}のコマンドを同期をしました。")

  except Exception as error:

    print("ERROR コマンドの同期に失敗しました。\n"+
                "エラー内容\n"+
               f"**{error}**"
    )

# メッセージを受信した時に発火するイベント
@client.event
async def on_message(message):
    
  if message.author.bot: # Botからのメッセージを無視
      return

  if message.content.startswith('テスト'): # ユーザーが「テスト」と送信すると「test!」と返信
      await message.reply("test!")

# スラッシュコマンド 1
@tree.command(name="test_command_1", description="コマンド説明 1")
async def test_command_1(interaction: discord.Interaction):
  await interaction.response.send_message(f'{interaction.user.mention} さん、こんにちは！') # メッセージを送信

# スラッシュコマンド 2
@tree.command(name="test_command_2", description="コマンド説明 2")
async def test_command_2(interaction: discord.Interaction):
  await interaction.response.send_message(f'{interaction.user.mention} さん、こんにちは！', ephemeral=True) # 実行者のみ見えるメッセージを送信

# クライアントを実行してDiscordに接続する
client.run(TOKEN.Discord_TOKEN)