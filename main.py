# This example requires the 'message_content' intent.
import os

from dotenv import load_dotenv

import discord

import random

from utils import readJson, getName, writeJson

from utils import guildID

from utils import bot


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    
    try:  # Try Except block to sync commands to Discord
        synced = await bot.tree.sync(guild=guildID)
        print(f"Synced {len(synced)} commands to guild {guildID.id}")

    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.tree.command(description="Flips a coin.", guild=guildID)
async def flip(ctx: discord.Interaction):
    await ctx.response.send_message(random.choice(["Heads!", "Tails!"]))


@bot.tree.command(description="Generates a random integer between 2 values. Leave the second one blank to roll a die.", guild=guildID)
async def rnum(ctx: discord.Interaction, a: int, b: int = None):
    if b is None:
        await ctx.response.send_message(random.randint(int(1), int(a)))
        return 
    await ctx.response.send_message(random.randint(int(a), int(b)))


@bot.tree.command(description="Awards points to a user. Leave blank to award yourself points.", guild=guildID)
async def awardpoints(ctx: discord.Interaction, newpoints: int, member: discord.Member = None):
    if member is None:
        member = ctx.author
    dict = readJson(getName(member))
    dict["Points"] += newpoints
    writeJson(dict, getName(member))
    await ctx.response.send_message(f'{getName(member)} now has {dict["Points"]} points')


@bot.tree.command(description="Removes points from a user. Leave blank to remove your points.", guild=guildID)
async def removepoints(ctx: discord.Interaction, newpoints: int, member: discord.Member = None):
    if member is None:
        member = ctx.author
    dict = readJson(getName(member))
    if dict["Points"] - newpoints < 0:
        newpoints = 0
    else:
        newpoints = dict["Points"] - newpoints
    dict["Points"] = newpoints
    writeJson(dict, getName(member))
    await ctx.response.send_message(f'{getName(member)} now has {dict["Points"]} points')


@bot.tree.command(description="Transfers points from you to a user.", guild=guildID)
async def givepoints(ctx: discord.Interaction, newpoints: int, member: discord.Member = None):
    if member is None:
        await ctx.response.send_message("Please add the roomate to give points to.")
        return

    sender = readJson(getName(ctx.author))
    receiver = readJson(getName(member))

    if sender["Points"] - newpoints < 0:
        await ctx.response.send_message(f'You only have {sender["Points"]} points')
        return

    senderPoints = sender["Points"] - newpoints
    sender["Points"] = senderPoints

    receiver["Points"] += newpoints

    writeJson(sender, getName(ctx.author))
    writeJson(receiver, getName(member))
    await ctx.response.send_message(f'{getName(member)} now has {receiver["Points"]} points and {getName(ctx.author)} has {senderPoints}')


@bot.tree.command(description="Checks the balance of a user. Leave blank for your balance", guild=guildID)
async def bal(ctx: discord.Interaction, member: discord.Member = None):
    if member is None:
        points = readJson(getName(ctx.author))["Points"]
        await ctx.response.send_message(f'{getName(ctx.author)} has {points} points')
        return
    else:
        points = readJson(getName(member))["Points"]
        await ctx.response.send_message(f'{getName(member)} has {points} points')


@bot.tree.command(description="Checks the chores that a user has to do. Leave blank for your chores.", guild=guildID)
async def checkchores(ctx: discord.Interaction, member: discord.Member = None):
    if member is None:
        member = ctx.author
    data = readJson(getName(member))
    await ctx.response.send_message(f'{getName(member)}s chores are {", ".join(data["Chores"])}')


@bot.tree.command(description="Adds a chore to someone's list. Leave blank to add to yours.", guild=guildID)
async def addchore(ctx: discord.Interaction, newchore: str = None, member: discord.Member = None):
    if member is None:
        member = ctx.author
    if newchore is None:
        await ctx.response.send_message("Please Provide a chore")

    data = readJson(getName(member))
    data["Chores"].append(newchore)

    writeJson(data, getName(member))
    await ctx.response.send_message(f'{getName(member)}s chores are now {", ".join(data["Chores"])}')


@bot.tree.command(description="Removes a chore from someone's list. Leave blank to remove from yours.")
async def removechore(ctx: discord.Interaction, newchore: str = None, member: discord.Member = None):
    if member is None:
        member = ctx.author
    if newchore is None:
        await ctx.response.send_message("Please Provide a chore")
        return

    data = readJson(getName(member))

    if newchore not in ", ".join(data["Chores"]):
        await ctx.response.send_message("They do not have that chore")
        return

    data["Chores"].remove(newchore)

    writeJson(data, getName(member))
    await ctx.response.send_message(f'{getName(member)}s chores are now {", ".join(data["Chores"])}')

load_dotenv()
bot.run(os.getenv("KEY"))