
import os
import json
import asyncio
import discord
from discord.ext import commands
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

class PrefixCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx, sett = 'list', *, prefix = 'None!!!'):
        if sett == 'set':

            if prefix == 'None!!!':
                await ctx.send("```MissingRequiredArgument: Atleast one argument is missing.```")

            else:
                with open("./configs/prefixes.json", "r") as f:
                    prefixes = json.load(f)

                prefixes[str(ctx.guild.id)] = prefix

                with open("./configs/prefixes.json", "w") as f:
                    json.dump(prefixes, f)

                e = discord.Embed(
                    description='<:tickYes:787334378630938672> Successfully changed prefix to `{}`.'.format(prefix),
                    color=discord.Color.green()
                )
                #e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                #footerd(e)

                await ctx.send(embed=e)

        if sett == 'list':
            with open("./configs/prefixes.json", "r") as f:
                prefixes = json.load(f)

            e = discord.Embed(
                description='Current prefix is `' + prefixes.get(f"{str(ctx.guild.id)}") + '`.',
                color=emcolor
            )
            #e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            #footerd(e)
            await ctx.send(embed=e)
            
def setup(bot):
    bot.add_cog(PrefixCommand(bot))