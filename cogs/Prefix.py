
import os
import json
import asyncio
import discord
from discord.ext import commands
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

class PrefixCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_server=True)
    async def prefix(self, ctx, sett, prefix = None):

        if sett == 'set' or 'Set':

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            prefixes[str(ctx.guild.id)] = prefix

            with open("prefixes.json", "w") as f:
                json.dump(prefixes,f)

            e = discord.Embed(
                description='<:tickYes:787334378630938672> Successfully changed prefix to `{}`.'.format(prefix),
                color=emcolor
            )
            e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            footerd(e)

            await ctx.send(embed=e)
        elif sett == 'view' or 'list' or None:
            
            def gprefix():
                with open("prefixes.json", "r") as f:
                    prefixes = json.load(f)

                if str(ctx.guild.id) not in prefixes:
                    return prefix

            e = discord.Embed(
                description='Current prefix is `' + gprefix() + '`.',
                color=emcolor
            )

            
def setup(bot):
    bot.add_cog(PrefixCommand(bot))