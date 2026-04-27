# This example requires the 'message_content' intent.
import os

from dotenv import load_dotenv

import discord

import random

from utils import readJson, getName, writeJson


from utils import bot

load_dotenv()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()  # Coinflip
async def flip(ctx):
    await ctx.send(random.choice(["Heads!", "Tails!"]))


@bot.command()  # Generates a random integer between 2 given integers, inclusive
async def numgen(ctx, arg1, arg2):
    await ctx.send(random.randint(int(arg1), int(arg2)))


@bot.command()  # Dice system for DnD. Will probably be made into a normal Python code block when the hardware is built
async def d(ctx, arg):
    await ctx.send(random.randint(1, int(arg)))


@bot.command()
async def awardPoints(ctx, newPoints: int, member: discord.Member = None):
    if member is None:
        member = ctx.author
    dict = readJson(getName(member))
    dict["Points"] += newPoints
    writeJson(dict, getName(member))
    await ctx.send(f'{getName(member)} now has {dict["Points"]} points')


@ bot.command()
async def removePoints(ctx, newPoints: int, member: discord.Member = None):
    if member is None:
        member = ctx.author
    dict = readJson(getName(member))
    if dict["Points"] - newPoints < 0:
        newPoints = 0
    else:
        newPoints = dict["Points"] - newPoints
    dict["Points"] = newPoints
    writeJson(dict, getName(member))
    await ctx.send(f'{getName(member)} now has {dict["Points"]} points')


@ bot.command()
async def givePoints(ctx, newPoints: int, member: discord.Member = None):
    if member is None:
        await ctx.send("Please add the roomate to give points too")
        return

    sender = readJson(getName(ctx.author))
    receiver = readJson(getName(member))

    if sender["Points"] - newPoints < 0:
        await ctx.send(f'You only have {sender["Points"]} points')
        return

    senderPoints = sender["Points"] - newPoints
    sender["Points"] = senderPoints

    receiver["Points"] += newPoints

    writeJson(sender, getName(ctx.author))
    writeJson(receiver, getName(member))
    await ctx.send(f'{getName(member)} now has {receiver["Points"]} points and {getName(ctx.author)} has {senderPoints}')


@ bot.command()
async def checkPoints(ctx, member: discord.Member = None):
    if member is None:
        points = readJson(getName(ctx.author))["Points"]
        await ctx.send(f'{getName(ctx.author)} has {points} points')
        return
    else:
        points = readJson(getName(member))["Points"]
        await ctx.send(f'{getName(member)} has {points} points')


@bot.command()
async def checkChores(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    data = readJson(getName(member))
    await ctx.send(f'{getName(member)}s chores are {", ".join(data["Chores"])}')


@bot.command()
async def addChore(ctx, newChore: str = None, member: discord.Member = None):
    if member is None:
        member = ctx.author
    if newChore is None:
        await ctx.send("Please Provide a chore")

    data = readJson(getName(member))
    data["Chores"].append(newChore)

    writeJson(data, getName(member))
    await ctx.send(f'{getName(member)}s chores are now {", ".join(data["Chores"])}')


@bot.command()
async def removeChore(ctx, newChore: str = None, member: discord.Member = None):
    if member is None:
        member = ctx.author
    if newChore is None:
        await ctx.send("Please Provide a chore")
        return

    data = readJson(getName(member))

    if newChore not in ", ".join(data["Chores"]):
        await ctx.send("They do not have that chore")
        return

    data["Chores"].remove(newChore)

    writeJson(data, getName(member))
    await ctx.send(f'{getName(member)}s chores are now {", ".join(data["Chores"])}')

bot.run(os.getenv("KEY"))