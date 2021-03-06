import discord
from manager import BanPickManager

token_path = "token.txt"
with open(token_path) as f:
    TOKEN = f.read()
    TOKEN = TOKEN.strip()

client = discord.Client()
manager = BanPickManager()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.channel.name != 'banpick':
        return

    msg = manager.controller(message.content)

    await message.channel.send(msg)

    return

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)