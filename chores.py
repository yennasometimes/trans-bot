from utils import getName, readJson, writeJson

from utils import bot

import discord


class Chores:

    def __init__(self):
        print("Chores are ready")

    @bot.command()
    async def checkChores(ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        data = readJson(getName(member))
        await ctx.send(f'{getName(member)}s chores are {", ".join(data["Chores"])}')

    @bot.command()
    async def addChore(ctx, *, member: discord.Member = None, newChore: str = None):
        if member is None:
            member = ctx.author
        if newChore is None:
            await ctx.send("Please Provide a chore")

        newChore = newChore.split()
        newChore = " ".join(newChore[1:])

        data = readJson(getName(member))
        data["Chores"].append(newChore)

        writeJson(data, getName(member))
        await ctx.send(f'{getName(member)}s chores are now {", ".join(data["Chores"])}')

    @bot.command()
    async def removeChore(ctx, *, member: discord.Member = None, newChore: str = None):
        if member is None:
            member = ctx.author
        if newChore is None:
            await ctx.send("Please Provide a chore")
            return

        newChore = newChore.split()
        newChore = " ".join(newChore[1:])

        data = readJson(getName(member))

        if newChore not in ", ".join(data["Chores"]):
            await ctx.send("They do not have that chore")
            return

        data["Chores"].remove(newChore)

        writeJson(data, getName(member))
        await ctx.send(f'{getName(member)}s chores are now {", ".join(data["Chores"])}')
