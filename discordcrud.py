import discord
import asyncio
from sqlalchemy import create_engine

client = discord.Client()

help = ["help：このヘルプを表示します。",
        "showlist：メンバー情報一覧を表示します。",
        "add：メンバー情報を追加します。",
        "edit：メンバー情報を編集します。",
        "delete：メンバー情報を削除します。",
        ]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
    print("discordボット型メンバー管理システム")
    engine = create_engine("sqlite3://localhost:8080/member?charset=UTF-8")

@client.event
async def commandstr():
    if message.author.bot:
        return

    if message.content == "help":
        for i in range(len(help)):
            await message.channel.send(help[i])

    
client.run("a")