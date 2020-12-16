import discord
import os
import asyncio
import datetime
import random
import json
import re
from discord.ext import commands
from bot_things import  motd, emcolor, ercolor, footerd, getprefix, get_prefix, footera, prefix

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['av'])
    @commands.guild_only()
    async def avatar(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        e = discord.Embed(
            title=f'Avatar for {user}',
            description=f'[Direct Link]({user.avatar_url})'
        )
        e.set_image(url=user.avatar_url)
        footera(e)
        await ctx.send(embed=e)

    @commands.command(aliases=['fetchav', 'fetch_av', 'fetch_avatar'])
    @commands.guild_only()
    async def fetchavatar(self, ctx, id_: int = None):
        if id_ == None:
            await ctx.send(f"You need to provide someone to fetch their avatar.\nUsage: `{prefix(ctx.message)}fetchav [user-id]`")
            return

        user = await self.bot.fetch_user(id_)

        e = discord.Embed(
            title=f'Avatar for {user}',
            description=f'[Direct Link]({user.avatar_url})'
        )
        e.set_image(url=user.avatar_url)
        footera(e)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Miscellaneous(bot))