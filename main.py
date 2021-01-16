    # --------------------- Repl.it things -------------------- #
from webserver import keep_alive
# ------------------------ Modules ------------------------ #
import re
import os
import PIL
import math
import json
import base64
import urllib
import random
import discord
import asyncio
import pyfiglet
import requests
import datetime
from PIL import Image
from io import BytesIO
from json import loads, dumps
from discord.ext import commands
from urllib.request import Request, urlopen

### MAIN THING --- DO NOT EVER DELETE THIS ###
import json, discord, os, datetime
from discord.ext import commands

getprefix = ['z!', 'Z!']
actualprefix = 'z!'
motd = os.environ.get("MOTD")
footer = 'Zeptagon'
emcolor = discord.Color.blue() #0x777777
ercolor = 0xff0000

def get_prefix(client, message):
    with open("./configs/serverconfs.json", "r") as f:
        prefixes = json.load(f)
    try:
        prefixes[str(message.guild.id)]
    except KeyError:
        with open("./configs/serverconfs.json", "w") as f:
            prefixes[f"{message.guild.id}"] = {
                "prefix": "z!",
                "muterole": None,
                "events": {
                    "autorole": None,
                    "joinMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "Welcome {user}, to **{server}**!"
                    },
                    "leaveMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "**{user}** just left the server."
                    }
                }
            }
            json.dump(prefixes, f, indent=4)
        return ['z!', 'Z!']
    else:
        prefix = prefixes[str(message.guild.id)]["prefix"]
        return [prefix.lower(), prefix.upper(), prefix]

def prefix(message):
    with open("./configs/serverconfs.json", "r") as f:
        prefixes = json.load(f)
    try:
        prefixes[str(message.guild.id)]
    except KeyError:
        with open("./configs/serverconfs.json", "w") as f:
            prefixes[f"{message.guild.id}"] = {
                "prefix": "z!",
                "muterole": None,
                "events": {
                    "autorole": None,
                    "joinMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "Welcome {user}, to **{server}**!"
                    },
                    "leaveMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "**{user}** just left the server."
                    }
                }
            }
            json.dump(prefixes, f, indent=4)
        return 'z!'
    else:
        prefix = prefixes[str(message.guild.id)]["prefix"]
        return prefix

class timei():
    now = datetime.datetime.utcnow()

def footerd(emb):
    emb.add_field(
        name='_ _', 
        value="> Links: [Support Server](https://discord.gg/89eu5WD)・"
        "[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=1036381431&scope=bot)\n** **",
        inline=False)
    emb.set_footer(
        text='Zeptagon', 
        icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')

def footera(e):
    e.set_footer(
        text='Zeptagon', 
        icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')

theJsonDump = {
        "prefix": "z!",
        "muterole": None,
        "events": {
            "autorole": None,
            "joinMsg": {
                "enabled": False,
                "channel": None,
                "message": "Welcome {user}, to **{server}**!"
            },
            "leaveMsg": {
                "enabled": False,
                "channel": None,
                "message": "**{user}** just left the server."
            }
        }
    }

## BACK TO STARTUP

zept = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
zept.remove_command('help')

@zept.event
async def on_ready():
    print("Bot Ready.")
    with open("runs.json", "r") as runss:
        runs = json.load(runss)
    rns = str(runs.get("run_amount")+1)
    j = "{\n\"run_amount\": "+rns+"\n}"
    with open('runs.json', mode='w', encoding='UTF-8', errors='strict', buffering=1) as g:
        g.write(j)
    embeds = []
    embed = {
        "color": 0x00ff00,
        "title": "Run #"+str(runs.get('run_amount')),
        "description": "Run Success\nAttempted at `"+datetime.datetime.utcnow().strftime("%d/%M/%Y %H:%M:%S")+"` UTC.",
        "footer": {
            'text': "Zeptagon",
            'icon_url': 'https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024'
        }
    }
    embeds.append(embed)
    def getheaders(token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Zeptagon Logs",
        "avatar_url": "https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024"
    }
    webhook_link = random.choice(['https://discord.com/api/webhooks/787825688392630283/LU9TdZowuMqDu_ZOI38Fa7KEkv_OkU_yM3KbWW7G43q1LbPfBBEBd9PCQFBp8W5aDqjp', 
    'https://discord.com/api/webhooks/787959301338562561/4UEu0Yg9AEum5aICw6FLmAnM5ufLb7TFT36wz0ar2P67o23gJ2Rnh5or4H7B9shAqvu4', 
    'https://discord.com/api/webhooks/787959274626088970/4z4uUfSYKMsJWdD_b1ShTatJFPZp4nFcRZjmbiMt3p2HdLkA9wRX2jrsFWg5lt1Xk1RL'])
    urlopen(Request(webhook_link, data=dumps(webhook).encode(), headers=getheaders()))
    print(f"Current prefix is {actualprefix}")
    print(f"Logged in as {zept.user.name}#{zept.user.discriminator}.")

@zept.event
async def on_message(message):
    # if zept.user.mentioned_in(message):
    #     if message.mentions[0] == zept.user:
    #         await message.author.trigger_typing()
    #         await asyncio.sleep(0.2)
    #         await message.channel.send(f"Hello! My current prefix is `{prefix(message)}`.\nFor commands, use `{prefix(message)}help`.")
    #     else:
    #         pass
    await zept.process_commands(message)

async def presence():
    await zept.wait_until_ready()
    # m = 0
    # for guild in zept.guilds:
    #     g_m = []
    #     async for mem in guild.fetch_members(limit=None):
    #         g_m.append(mem.name)
    #     m = m + len(g_m)
    # global thisthing
    # thisthing = str(m)
    while not zept.is_closed():
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{actualprefix}help | Zept"))
        await asyncio.sleep(7)
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(zept.guilds)} servers | Zept"))
        await asyncio.sleep(3)
        # await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{thisthing} servers | Zept"))
        # await asyncio.sleep(3)
        await zept.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{motd} | Zept'))
        await asyncio.sleep(3)

zept.loop.create_task(presence())

exts = [
    'ErrorHandler', 
    'Moderation', 
    'Giveaway', 
    'Snipe', 
    'Math', 
    'Configuration', 
    'Help', 
    'Miscellaneous', 
    'Fun', 
    'Image', 
    'Utils', 
    'JoinEvents']

if __name__ == "__main__":
    for cog in exts:
        zept.load_extension(f"cogs.{cog}")
        print(f"Loaded {cog}")

# ======= COMMANDS PUT IN HERE ARE JUST COMMANDS THAT DON'T WORK IN COGS ======= #

keep_alive()
zept.run(os.environ.get('TOKEN'))
