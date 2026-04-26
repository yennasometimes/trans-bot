# This example requires the 'message_content' intent.
import os

from dotenv import load_dotenv

import discord

from discord.ext import commands

import Points.points

from utils import readJson, writeJson, getName, bot

load_dotenv()


@bot.event
async def on_ready():
    print("Ready!")


@bot.command()
async def assign(ctx, member: discord.Member, arg2):

    await ctx.send(f'{ctx.author.nick} assigned {arg2} to {member.nick}')


bot.run(os.getenv("KEY"))
