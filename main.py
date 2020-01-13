import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjY1ODEyNzUxNDYxMTIyMDUw.XhrKJw.Ivn59QhQ9dBUoq0gtVJedLnIA4A'

# 接続に必要なオブジェクトを生成
client = discord.Client()

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

    if message.channel:
        await message.channel.send('にゃーん')

    return

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)