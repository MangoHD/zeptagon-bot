import discord
import os
import asyncio
import datetime
import random
from discord.ext import commands
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        global snipe_message_content
        global snipe_message_author
        
        snipe_message_content = message.content
        snipe_message_author = message.author
        await asyncio.sleep(60)
        snipe_message_author = None
        snipe_message_content = None

    @commands.command()
    async def snipe(self, ctx):
        if snipe_message_content == None:
            await ctx.channel.send("Theres nothing to snipe.")
        elif snipe_message_content != None:
            embed = discord.Embed(description=f"{snipe_message_content}")
            embed.set_author(name= f"{snipe_message_author}", icon_url = f'{snipe_message_author.avatar_url}')
            await ctx.channel.send(embed=embed)
            return
        else:
            await ctx.send("There's nothing to snipe.")

def setup(bot):
    bot.add_cog(Snipe(bot))
