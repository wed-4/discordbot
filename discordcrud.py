import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
    print("discordボット型メンバー管理システム")

client.run("a")