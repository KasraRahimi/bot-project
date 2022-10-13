import discord
from discord.ext import commands

with open("token.txt") as f:
    token = f.readline()

def runDiscordBot():
    bot = commands.Bot(intents=discord.Intents.all(), command_prefix="pomo-")

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready.")

    @bot.command()
    async def hello(ctx: commands.Context):
        await ctx.send("Hi, I'm currently not functional")
    bot.run(token)
