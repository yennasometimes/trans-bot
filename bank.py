import discord
from discord.ext import commands
import os
from dotenv import load_dotenv, dotenv_values



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command
async def bal(ctx, arg):
    with open("bank.txt") as f:
        for name in f:
            if name[0,name.index(",")] == arg.lower():

load_dotenv()
bot.run(os.getenv("KEY"))  # Needs to be replaced with dotenv call