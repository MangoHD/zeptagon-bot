# --------------------- Repl.it things -------------------- #
from webserver import keep_alive

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
import urllib
from urllib.request import Request, urlopen
from PIL import Image
from io import BytesIO
from json import loads, dumps
from discord.ext import commands

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

getprefix = ['zp!', 'Zp!', 'zP!', 'ZP!']
prefix = 'zp!'
motd = 'Newly made bot :D'
footer = 'Zeptagon'
emcolor = 0x777777
ercolor = 0xff0000
def footerd(emb):
    emb.add_field(name='_ _', value='Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)')
    emb.set_footer(text='Zeptagon', icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')

zept = commands.Bot(command_prefix=getprefix, case_insensitive=True)
zept.remove_command('help')

@zept.event
async def on_ready():
    print("Uptime ready.")

async def presence():
    await zept.wait_until_ready()
    while not zept.is_closed():
        r = requests.get('https://9123929-8727348-1892398499-123487-8439809164-42578285.mamplayz13.repl.co')
        if 'Webserver alive, Discord bot alive' in r.text:
            embeds = []
            embed = {
                "color": 0x32cd32,
                "title": "Bot Status",
                "description": f"Bot online, webserver online, with a status code of `{r.status_code}`",
                "footer": {
                    'text': "Zeptagon",
                    'icon_url': 'https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024'
                }
            }
            embeds.append(embed)
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
        else:
            embeds = []
            embed = {
                "color": 0xff0000,
                "title": "Bot Status",
                "description": f"Bot down, with a status code of `{r.status_code}`",
                "footer": {
                    'text': "Zeptagon",
                    'icon_url': 'https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024'
                }
            }
            embeds.append(embed)
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
        
        await asyncio.sleep(300)

zept.loop.create_task(presence())

keep_alive()
zept.run(os.environ.get('DISCORD_BOT_SECRET'))