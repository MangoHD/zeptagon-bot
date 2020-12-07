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
from boto.s3.connection import S3Connection
from PIL import Image
from io import BytesIO
from discord.ext import commands


prefix = ["Z/","z/"]
zept = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive= True)

@zept.event
async def on_ready():
    print("[ LOGS ] :: Made by mutefx#0002, Special thanks to Cylo Hangout")
    print("[ LOGS ] :: File loaded.")
    print("[ LOGS ] :: Token found.")
    print("[ LOGS ] :: Bot started.")
    print(f"[ LOGS ] :: Current prefix is {prefix}")
    print(f"[ LOGS ] :: Logged in as {zept.user.name}#{zept.user.discriminator}.")

# -------------------- Rich Presence ---------------------- #

async def presence():
    await zept.wait_until_ready()

    while not dyv.is_closed():
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help | Dyv"))
        await asyncio.sleep(7)
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(dyv.guilds)} servers | Dyv"))
        await asyncio.sleep(7)
        await zept.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{motd} | Dyv'))
        await asyncio.sleep(7)

zept.loop.create_task(presence())
