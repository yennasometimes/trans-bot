# This example requires the 'message_content' intent.
import os

from dotenv import load_dotenv

import discord

from discord.ext import commands


import json

load_dotenv()

nicksToUsers = {
    "ace_managment": "Ace",
    "alphariusfake": "Cassandra",
    ".axolotter": "Jax",
    "typowriter2060": "Jamie",
    "zzero123": "Jay",
    "yennasometimes": "Yenna",
    "dusklord121": "Ben",
    "swethort": "Melanie"
}

testUserData = {
    "Chores": ["Sample", "List", "Of", "Chores"],
    "Points": 5000
}


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print("Ready!")


@bot.command()
async def assign(ctx, member: discord.Member, arg2):

    await ctx.send(f'{ctx.author.nick} assigned {arg2} to {member.nick}')


@bot.command()
async def test(ctx):
    writeJson(testUserData, "Yenna")


@bot.command()
async def awardPoints(ctx, newPoints: int, member: discord.Member = None):
    if member is None:
        member = ctx.author
    dict = readJson(getName(member))
    dict["Points"] += newPoints
    writeJson(dict, getName(member))
    await ctx.send(f'{getName(member)} now has {dict["Points"]} points')


@bot.command()
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


@bot.command()
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


@bot.command()
async def checkPoints(ctx, member: discord.Member = None):
    if member is None:
        points = readJson(getName(ctx.author))["Points"]
        await ctx.send(f'{getName(ctx.author)} has {points} points')
        return
    else:
        points = readJson(getName(member))["Points"]
        await ctx.send(f'{getName(member)} has {points} points')


def getName(member: discord.Member):
    return (nicksToUsers[member.name])


def readJson(name: str) -> dict:
    with open(f'UserInfo/{name}.json', mode="r", encoding="utf-8") as read_file:
        return json.load(read_file)


def writeJson(jsonData: dict, name: str):
    with open(os.getcwd() + f'/UserInfo/{name}.json', mode="w", encoding="utf-8") as write_file:
        json.dump(jsonData, write_file)


bot.run(os.getenv("KEY"))
