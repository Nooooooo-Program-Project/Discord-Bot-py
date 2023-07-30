# ----------------------------------------

# Copyright (c) 2023 Nooooooo Program Project
# Licensed under the Apache License 2.0

# やり方は README.md をご確認ください。

# ----------------------------------------

import discord # pip install discord.py[voice]
import asyncio
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

  await client.change_presence(status = discord.Status.online, activity = discord.Activity(name="discord.py Discord Bot", type=discord.ActivityType.playing))

  try:
    tree_cmd = await tree.sync() # スラッシュコマンドの同期

    print(f"{len(tree_cmd)}のコマンドを同期をしました。")

  except Exception as error:

    print("コマンドの同期に失敗しました。\n"+
          "エラー内容\n"+
         f"{error}"
    )

# メッセージを受信した時に発火するイベント
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

# スラッシュコマンド 1
@tree.command(name="test_command_1", description="コマンド説明 1")
async def test_command_1(interaction: discord.Interaction):
  await interaction.response.send_message(f'{interaction.user.mention} さん、こんにちは！') # メッセージを送信

# スラッシュコマンド 2
@tree.command(name="test_command_2", description="コマンド説明 2")
async def test_command_2(interaction: discord.Interaction):
  await interaction.response.send_message(f'{interaction.user.mention} さん、こんにちは！', ephemeral=True) # 実行者のみ見えるメッセージを送信

# スラッシュコマンド 3
@tree.command(name="join", description="ボイスチャンネルに接続します")
@app_commands.rename(channel="接続するボイスチャンネルを選択")
async def join(interaction: discord.Interaction, channel: discord.VoiceChannel):

  voice_client = channel.guild.voice_client

  try:

    if voice_client is not None and voice_client.channel != channel:
        await voice_client.move_to(channel)
    elif voice_client is None:
        
        await channel.connect() # 選択したボイスチャネルに接続
    else:
        embed=discord.Embed(
          title="ボイスチャンネルに接続出来ませんでした。",
          color=0xff0000,
          timestamp=interaction.created_at
        )
        embed.add_field(
          name="エラーの原因",
          value="既に接続しているため"
        )
        embed.set_author(name="❗ エラー")
        await interaction.response.send_message(embed=embed, ephemeral=True) # ボイスチャンネルに既に接続しているのにコマンドを実行した場合に送信

    embed = discord.Embed(
        color=0x00ff00,
        description=f"{channel.mention} に接続しました。",
        timestamp=interaction.created_at
    )
    await interaction.response.send_message(embed=embed, ephemeral=True) # ボイスチャンネルに接続した場合に送信

  except Exception as error:
    embed=discord.Embed(
      title="ボイスチャンネルに接続出来ませんでした。",
      color=0x00ff00,
      timestamp=interaction.created_at
    )
    embed.add_field(
      name="エラー内容",
      value=error
    )
    embed.set_author(name="❗ エラー")
    await interaction.response.send_message(embed=embed, ephemeral=True) # 例外(エラー)が発生した場合に送信

# スラッシュコマンド 4
@tree.command(name="leave", description="ボイスチャンネルから切断します")
async def leave(interaction: discord.Interaction):

  if interaction.guild.voice_client is None: # Botがボイスチャネルに接続してない場合

      embed=discord.Embed(
        title="ボイスチャンネルから切断出来ませんでした。",
        color=0xff0000,
        timestamp=interaction.created_at
      )
      embed.add_field(
        name="エラーの原因",
        value="ボイスチャンネルに接続していないため"
      )
      embed.set_author(name="❗ エラー")
      await interaction.response.send_message(embed=embed, ephemeral=True) # ボイスチャンネルに接続してないのにコマンドを実行した場合に送信
      return

  await interaction.guild.voice_client.disconnect() # Botが参加しているボイスチャネルから切断

  embed = discord.Embed(
      color=0xff0000,
      description=f"切断しました。",
      timestamp=interaction.created_at
  )
  await interaction.response.send_message(embed=embed, ephemeral=True) # ボイスチャンネルから切断した場合に送信

# スラッシュコマンド 5
@tree.command(name="mp3", description="mp3を再生します")
async def mp3(interaction: discord.Interaction):

  embed = discord.Embed(
      color=0x00ff00,
      description="再生を開始します",
      timestamp=interaction.created_at
  )
  await interaction.response.send_message(embed=embed) # 読み上げを開始する時に送信

  voice_channel = interaction.user.voice.channel # コマンド実行者が参加しているボイスチャネルを取得
  vc = await voice_channel.connect() # コマンド実行者が参加しているボイスチャネルに接続

  sources = [discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('voice.mp3'))] # 再生するファイル名  |  mp3
  for source in sources:
      vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
      while vc.is_playing():
          await asyncio.sleep(3) # 読み上げ終了後、3秒待機
  await vc.disconnect() #ボイスチャネルから切断

  embed = discord.Embed(
      color=0x00ff00,
      description="再生が完了しました。",
      timestamp=interaction.created_at
  )
  await interaction.channel.send(embed=embed) # 読み上げ終了した時に送信

# スラッシュコマンド 6
@tree.command(name="wav", description="wavを再生します")
async def mp3(interaction: discord.Interaction):

  embed = discord.Embed(
      color=0x00ff00,
      description="再生を開始します",
      timestamp=interaction.created_at
  )
  await interaction.response.send_message(embed=embed) # 読み上げを開始する時に送信

  voice_channel = interaction.user.voice.channel # コマンド実行者が参加しているボイスチャネルを取得
  vc = await voice_channel.connect() # コマンド実行者が参加しているボイスチャネルに接続

  sources = [discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('voice.wav'))] # 再生するファイル名  |  wav
  for source in sources:
      vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
      while vc.is_playing():
          await asyncio.sleep(3) # 読み上げ終了後、3秒待機
  await vc.disconnect() #ボイスチャネルから切断

  embed = discord.Embed(
      color=0x00ff00,
      description="再生が完了しました。",
      timestamp=interaction.created_at
  )
  await interaction.channel.send(embed=embed) # 読み上げ終了した時に送信

# クライアントを実行してDiscordに接続する
client.run(TOKEN.Discord_TOKEN)