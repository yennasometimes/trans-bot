# This example requires the 'message_content' intent.
import os

from dotenv import load_dotenv

import discord

from typing import Literal

import random

from utils import readJson, getName, writeJson

from utils import bot

from utils import guildID


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    
    try:  # Try Except block to sync commands to Discord
        synced = await bot.tree.sync(guild=guildID)
        print(f"Synced {len(synced)} commands to guild {guildID.id}")

    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.tree.command(description="Flips a coin", guild=guildID)
async def flip(ctx: discord.Interaction):
    await ctx.response.send_message(random.choice(["Heads!", "Tails!"]))


@bot.tree.command(description="Generates a random integer", guild=guildID)
@discord.app_commands.describe(a="Lower bound; upper bound if b is left empty", b="Upper bound")
async def randomnum(ctx: discord.Interaction, a: int, b: int = None):
    if b is None:
        await ctx.response.send_message(random.randint(int(1), int(a)))
        return 
    await ctx.response.send_message(random.randint(int(a), int(b)))


@bot.tree.command(description="Points commands", guild=guildID)
@discord.app_commands.describe(action="What you want to do", points="How much points to modify", member="Who will be affected")
async def points(ctx: discord.Interaction, action: Literal["balance", "award", "remove", "transfer"] = None, points: int = None, member: discord.User = None):
    match action:
        case "balance":
            if member is None:
                member = ctx.user
            points = readJson(getName(member))["Points"]
            await ctx.response.send_message(f'{getName(member)} has {points} points.')

        
        case "award":
            if member is None:
                member = ctx.user
            dict = readJson(getName(member))
            dict["Points"] += points
            writeJson(dict, getName(member))
            await ctx.response.send_message(f'{getName(member)} now has {dict["Points"]} points.')

        
        case "remove":
            if member is None:
                member = ctx.user
            dict = readJson(getName(member))
            dict["Points"] += points
            writeJson(dict, getName(member))
            await ctx.response.send_message(f'{getName(member)} now has {dict["Points"]} points.')

        
        case "transfer":
            if member is None:
                await ctx.response.send_message("Please add the roomate to give points to.")
                return

            sender = readJson(getName(ctx.user))
            receiver = readJson(getName(member))

            if sender["Points"] - points < 0:
                await ctx.response.send_message(f'You only have {sender["Points"]} points.')
                return

            senderPoints = sender["Points"] - points
            sender["Points"] = senderPoints

            receiver["Points"] += points

            writeJson(sender, getName(ctx.user))
            writeJson(receiver, getName(member))
            await ctx.response.send_message(f'{getName(member)} now has {receiver["Points"]} points and {getName(ctx.user)} now has {senderPoints} points.')


        case _:
            await ctx.response.send_message("Please check your syntax.")


@bot.tree.command(description="Chore commands", guild=guildID)
@discord.app_commands.describe(action="What you want to do", chore="Chore to modify", member="Who will be affected")
async def chores(ctx: discord.Interaction, action: Literal["view", "add", "remove", "transfer"] = None, chore: str = None, member: discord.User = None):
    match action:
        case "view":
            if member is None:
                member = ctx.user
            data = readJson(getName(member))
            await ctx.response.send_message(f'{getName(member)}s chores are {", ".join(data["Chores"])}.')
        

        case "add":
            if member is None:
                member = ctx.user
            
            data = readJson(getName(member))
            data["Chores"].append(chore)

            writeJson(data, getName(member))
            await ctx.response.send_message(f'{getName(member)}s chores are now {", ".join(data["Chores"])}.')
        

        case "remove":
            if member is None:
                member = ctx.user

            data = readJson(getName(member))

            if chore not in ", ".join(data["Chores"]):
                await ctx.response.send_message("They do not have that chore.")
                return

            data["Chores"].remove(chore)

            writeJson(data, getName(member))
            await ctx.response.send_message(f'{getName(member)}s chores are now {", ".join(data["Chores"])}.')
        

        case "transfer":
            if member is None:
                await ctx.response.send_message("Please input the roomate to transfer your chore to.")
                return

            sender = readJson(getName(ctx.user))
            receiver = readJson(getName(member))

            if chore not in sender["Chores"]:
                await ctx.response.send_message("You do not have that chore.")
                return
            
            if chore in receiver["Chores"]:
                await ctx.response.send_message("They already have that chore.")
                return

            sender["Chores"].remove(chore)
            receiver["Chores"].append(chore)

            writeJson(sender, getName(ctx.user))
            writeJson(receiver, getName(member))
            await ctx.response.send_message(f'Chore transferred from {getName(ctx.user)} to {getName(member)}.')


        case _:
            await ctx.response.send_message("Please check your syntax.")


load_dotenv()
bot.run(os.getenv("KEY"))