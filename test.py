# This example requires the 'message_content' intent.
import os

from dotenv import load_dotenv, dotenv_values

import discord

from discord.ext import commands

from dotenv import load_dotenv, dotenv_values

import random

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='.', intents=intents)


class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'@{ctx.author} slapped {to_slap} because *{argument}*'


@bot.command()
async def test(ctx, *, member: discord.Member):
    ctx.member
    await ctx.send(f'{member} is called {member.nick}')


bot.run(os.getenv("KEY"))
