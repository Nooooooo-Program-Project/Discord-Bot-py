# ----------------------------------------

# Copyright (c) 2024 Nooooooo Program Project
# Licensed under the Apache License 2.0

# やり方は README.md をご確認ください。

# ----------------------------------------

import discord # pip install discord.py[voice]
import TOKEN
from Quake import Quake_info
from discord import app_commands, Interaction

# メッセージの内容を受信するためにintents
intents = discord.Intents.default()
intents.message_content = True

# Discordクライアントを作成
client = discord.Client(intents=intents)

# app commandのツリーを初期化
tree = app_commands.CommandTree(client)

# --------- Botが起動した時に発火するイベント ---------#
@client.event
async def on_ready():
  
  print(f'{client.user.name} ({client.user.id}) がログインしました。') # Botがログインした際にメッセージを出力

  await client.change_presence(status = discord.Status.online, activity = discord.Activity(name="discord.py Discord Bot", type=discord.ActivityType.playing))

  try:
    tree_cmd = await tree.sync() # スラッシュコマンドの同期

    print(f"{len(tree_cmd)}のコマンドを同期をしました。")

  except Exception as error:

    print("コマンドの同期に失敗しました。\n"+
          "エラー内容\n"+
         f"{error}"
    )

# --------- メッセージを受信した時に発火するイベント ---------#
@client.event
async def on_message(message):
    
  if message.author.bot: # Botからのメッセージを無視
      return

  if message.content.startswith('おはよう'): # ユーザーが「おはよう」と送信すると「〇〇さん、おはようございます！」と返信
      await message.reply(f"{message.author.name}さん、おはようございます！")

  if message.content.startswith('こんにちは'): # ユーザーが「こんにちは」と送信すると「〇〇さん、こんにちは！」と返信
      await message.reply(f"{message.author.name}さん、こんにちは！")

  if message.content.startswith('こんばんは'): # ユーザーが「こんばんは」と送信すると「〇〇ささん、こんばんは！」と返信
      await message.reply(f"{message.author.name}さん、こんばんは！")

  if message.content.startswith('おやすみ'): # ユーザーが「おやすみ」と送信すると「〇〇さん、おやすみなさい！」と返信
      await message.reply(f"{message.author.name}さん、おやすみなさい！")

# --------- コマンド イベント ---------#

@tree.command(name="quake",description="地震情報を表示します")
async def quake(interaction: Interaction):

  try:

    em_color, quake_text = await Quake_info() # Quake_info 関数を実行し、em_colorとquake_textを取得
    embed = discord.Embed(
      title="地震情報", # Embedのタイトル
      color=em_color, # Embedの色
      description=quake_text, # Embedの内容
      timestamp=interaction.created_at # メッセージのタイムスタンプ
    )
    embed.set_author(name="Date: P2P地震情報") # Embed作成者情報
    await interaction.response.send_message(embed=embed)

  except Exception as error: # エラーが発生した場合

    embed = discord.Embed(
      title="地震情報 | エラー", # Embedのタイトル
      color=0xff0000, # Embedの色
      description="エラーが発生しました。", # Embedの内容
      timestamp=interaction.created_at # メッセージのタイムスタンプ
    )
    embed.add_field( # Embedのフィールド
      name="エラー内容", # フィールドのタイトル
      value=str(error) # フィールドの内容
    )
    await interaction.response.send_message(embed=embed) # メッセージを送信

# クライアントを実行してDiscordに接続する
client.run(TOKEN.Discord_TOKEN)