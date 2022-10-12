import discord
from discord import app_commands
from discord.ext import commands

with open("token.txt") as f:
    token = f.readline()

def runDiscordBot():
    bot = discord.Client(intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready.")

    @bot.event
    async def on_message(msg: discord.Message):
        contents = msg.content
        user = msg.author
        channel = msg.channel
        print("New message")
        print(f"\tuser = {user}")
        print(f"\tmessage = {contents}")
        print(f"\tchannel = {channel}\n")
    
    bot.run(token)
