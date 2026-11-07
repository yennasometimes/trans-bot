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


#  Flip a coin command
@bot.tree.command(description="Flips a coin", guild=guildID)
async def flip(ctx: discord.Interaction):
    await ctx.response.send_message(random.choice(["Heads!", "Tails!"]))


#  Random number command
@bot.tree.command(description="Generates a random integer", guild=guildID)
@discord.app_commands.describe(a="Lower bound; upper bound if b is left empty", b="Upper bound")
async def randomnum(ctx: discord.Interaction, a: int, b: int = None):
    if b is None:
        await ctx.response.send_message(random.randint(int(1), int(a)))
        return 
    await ctx.response.send_message(random.randint(int(a), int(b)))


#  Points commands
@bot.tree.command(description="Points commands", guild=guildID)
@discord.app_commands.describe(action="What you want to do", points="How much points to modify", member="Who will be affected")
async def points(ctx: discord.Interaction, action: Literal["balance", "award", "remove", "transfer"], points: int = None, member: discord.User = None):
    match action:
        case "balance":
            if member is None:
                member = ctx.user
            points = readJson(getName(member.id))["Points"]
            await ctx.response.send_message(f'{getName(member.id)} has {points} points.')
        
        case "award":
            if member is None:
                member = ctx.user
            dict = readJson(getName(member.id))
            dict["Points"] += points
            writeJson(dict, getName(member.id))
            await ctx.response.send_message(f'{getName(member.id)} now has {dict["Points"]} points.')

        case "remove":
            if member is None:
                member = ctx.user
            dict = readJson(getName(member.id))
            dict["Points"] += points
            writeJson(dict, getName(member.id))
            await ctx.response.send_message(f'{getName(member.id)} now has {dict["Points"]} points.')
        
        case "transfer":
            if member is None:
                await ctx.response.send_message('Please add the person to give points to.')
                return
            sender = readJson(getName(ctx.user.id))
            receiver = readJson(getName(member.id))
            if sender["Points"] - points < 0:
                await ctx.response.send_message(f'You only have {sender["Points"]} points.')
                return
            senderPoints = sender["Points"] - points
            sender["Points"] = senderPoints
            receiver["Points"] += points
            writeJson(sender, getName(ctx.user.id))
            writeJson(receiver, getName(member.id))
            await ctx.response.send_message(f'{getName(member.id)} now has {receiver["Points"]} points and {getName(ctx.user.id)} now has {senderPoints} points.')

        case _:
            await ctx.response.send_message("Please check your syntax.")


load_dotenv()
bot.run(os.getenv("KEY"))