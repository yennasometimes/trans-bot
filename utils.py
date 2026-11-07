import discord

import os

from discord.ext import commands

import json


usersToNames = {
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
bot = commands.Bot(command_prefix='!$', intents=intents)

guildID = discord.Object(id=1568507855269658796)
# 1568507855269658796 testing server
# 1496328699077857331 suite server
# 1541636515061571584 2067 server

def getName(member):
    return (usersToNames[str(member.name)])


def readJson(name: str) -> dict:
    with open(f'UserInfo/{name}.json', mode="r", encoding="utf-8") as read_file:
        return json.load(read_file)


def writeJson(jsonData: dict, name: str):
    with open(os.getcwd() + f'/UserInfo/{name}.json', mode="w", encoding="utf-8") as write_file:
        json.dump(jsonData, write_file)