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
    "753969299718406247": "Yenna",
    "dusklord121": "Ben",
    "swethort": "Melanie"
}

guildID = discord.Object(id=1496328699077857331)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!$', intents=intents)


def getName(member: str):
    return (nicksToUsers[member])


def readJson(name: str) -> dict:
    with open(f'UserInfo/{name}.json', mode="r", encoding="utf-8") as read_file:
        return json.load(read_file)


def writeJson(jsonData: dict, name: str):
    with open(os.getcwd() + f'/UserInfo/{name}.json', mode="w", encoding="utf-8") as write_file:
        json.dump(jsonData, write_file)