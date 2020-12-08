import discord
import os
import asyncio
import datetime
import random
from discord.ext import commands

getprefix = [os.environ['BOT_PREFIX'], os.environ['BOT_PREFIX2']]
prefix = os.environ['BOT_PREFIX']
motd = os.environ['BOT_MOTD']
footer = os.environ['BOT_FOOTER']
emcolor = 0x777777
ercolor = 0xff0000
fieldfooter = "Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)"

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    snipe_message_content = None
    snipe_message_author = None
    snipe_message_id = None

    @commands.Cog.listener()
    async def on_message_delete(message):

        global snipe_message_content
        global snipe_message_author
        global snipe_message_id

        snipe_message_content = message.content
        snipe_message_author = message.author
        snipe_message_id = message.id
        await asyncio.sleep(120)

        if message.id == snipe_message_id:
            snipe_message_author = None
            snipe_message_content = None
            snipe_message_id = None

    @commands.command()
    @commands.guild_only()
    async def snipe(self, ctx):
        emb = discord.Embed(
            description = snipe_message_content,
            color=emcolor
        )
        emb.set_author(name=snipe_message_author, icon_url=snipe_message_author.avatar_url)
        emb.add_field(name="_ _", value=fieldfooter)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Snipe(bot))
