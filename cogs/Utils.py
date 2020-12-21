import os
import random
import asyncio
import discord
import aiohttp
import requests
from discord.ext import commands
from bot_things import  motd, emcolor, ercolor, footerd, footera, getprefix, get_prefix, prefix

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send(f"Bot's ping is `{round(self.bot.latency * 1000)}ms`")

    @commands.command()
    @commands.guild_only()
    async def pingweb(self, ctx, website = None):
        if website is None:
            pass
        else:
            try:
                r = requests.get(website).status_code
            except Exception as _e:
                await ctx.send("```Error: {}```".format(_e))
            if r == 404:
                await ctx.send(f'Site is down, responded with a status code of `{r}`.')
            else:
                await ctx.send(f'Site is up, responded with a status code of `{r}`.')

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):
        embed = discord.Embed(
            title='Invite Zeptagon',
            description="[All Perms Invite](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)\n"
                "[Recommended Invite](https://discord.com/oauth2/authorize?client_id=785496485659148359&scope=bot&permissions=2113400023&response_type=code)\n"
                "[Community Discord](https://discord.gg/TgKBwvszAB)"
                "\n\nDeveloped by [mutefx#0001](http://bit.ly/sub2mango)",
            colour=emcolor)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/icons/781696194837479485/a_75497839f28b083f48e5d6abd07bb63e.gif?size=1024")
        footera(embed)
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Utilities(bot))