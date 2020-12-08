# ------------------------ Modules ------------------------ #

import discord
import asyncio
import random
import datetime
import os
import json
import PIL
import math
import pyfiglet
import requests
import re
import base64
import dyv_math as mfmath
from PIL import Image
from io import BytesIO
from discord.ext import commands

getprefix = [os.environ['BOT_PREFIX'], os.environ['BOT_PREFIX2']]
prefix = os.environ['BOT_PREFIX']
motd = os.environ['BOT_MOTD']
footer = os.environ['BOT_FOOTER']
emcolor = 0x777777
ercolor = 0xff0000
fieldfooter = "Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)"

zept = commands.Bot(command_prefix=getprefix, case_insensitive=True)
zept.remove_command('help')

@zept.event
async def on_ready():
    print("Bot Ready.")
    print(f"Current prefix is {prefix}")
    print(f"Logged in as {zept.user.name}#{zept.user.discriminator}.")

# -------------------- Rich Presence ---------------------- #

async def presence():
    await zept.wait_until_ready()

    while not zept.is_closed():
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help | Zept"))
        await asyncio.sleep(7)
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(zept.guilds)} servers | Zept"))
        await asyncio.sleep(7)
        await zept.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{motd} | Zept'))
        await asyncio.sleep(7)

zept.loop.create_task(presence())

def setup(bot):
    exts = ['ErrorHandler', 'Moderation', 'Giveaway']

    if __name__ == "__main__":
        for cog in exts:
            bot.load_extension(f"cogs.{cog}")

setup(zept)

zept.run(os.environ['TOKEN'])
