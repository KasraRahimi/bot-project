import discord

PREFIX = "pomo "

def response(msg: str, user, channel):
    
    if msg.lower() == PREFIX + "hello":
        username = str(user).split("#")[0]
        return f"Hello, {username}"
    
    if msg.lower() == PREFIX + "bye":
        return f"Oh ok ;-; bye ig"

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

        if user == bot.user:
            return

        if contents[:5] == PREFIX:
            await channel.send(response(contents, user, channel))
    
    bot.run(token)
