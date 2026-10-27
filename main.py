import discord
import os
from dotenv import load_dotenv
import random
from discord.ext import commands
from commands import ping, weather, clear, cube
from anti_spam import anti_spam

intents = discord.Intents.default()
intents.message_content = True
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = commands.Bot(intents=intents, command_prefix="!", activity=discord.Game("Zeon"), status=discord.Status.idle)

@bot.event
async def on_ready():
    print(f'Zeon started: {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    await anti_spam(message)
    await bot.process_commands(message)


bot.add_command(ping)
bot.add_command(weather)
bot.add_command(clear)
bot.add_command(cube)



bot.run(BOT_TOKEN)
