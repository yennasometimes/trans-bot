import discord

import os

from discord.ext import commands
import json

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


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


def getName(member: discord.Member):
    return (nicksToUsers[member.name])


def readJson(name: str) -> dict:
    with open(f'UserInfo/{name}.json', mode="r", encoding="utf-8") as read_file:
        return json.load(read_file)


def writeJson(jsonData: dict, name: str):
    with open(os.getcwd() + f'/UserInfo/{name}.json', mode="w", encoding="utf-8") as write_file:
        json.dump(jsonData, write_file)