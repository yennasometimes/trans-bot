import discord
import os
from discord.ext import commands
import json


usersToNames = {
    "799405045505589300": "Ace",
    "1274554541345476660": "Alice",
    "1115027628403998821": "Cass",
    "889683436846084096": "Duncan",
    "1156194217719238729": "Felix",
    "769694825682829383": "Jacoby",
    "785554065466851388": "Jamie",
    "742055762448089200": "Jax",
    "695653492370440232": "Jay",
    "957990327912894504": "Kate",
    "1562240338477842495": "Melanie",
    "757639188421148893": "Nixon",
    "689960778786275342": "Onyx",
    "622934258901581836": "Robbie",
    "812008850223792139": "Tanmay",
    "604053007277097064": "Tejas",
    "341290788220829697": "Salvi",
    "753969299718406247": "Yenna"
}


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!$', intents=intents)

guildID = discord.Object(id=1568507855269658796)
# 1568507855269658796 testing server
# 1496328699077857331 suite server
# 1541636515061571584 2067 server

def getName(member):
    return (usersToNames[str(member.ID)])


def readJson(name: str) -> dict:
    with open(f'UserInfo/{name}.json', mode="r", encoding="utf-8") as read_file:
        return json.load(read_file)


def writeJson(jsonData: dict, name: str):
    with open(os.getcwd() + f'/UserInfo/{name}.json', mode="w", encoding="utf-8") as write_file:
        json.dump(jsonData, write_file)