import discord
import os
import asyncio
from discord.ext import commands
from bot_things import  motd, emcolor, ercolor, footerd, getprefix, get_prefix, prefix

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        #     await ctx.message.delete()
        #     embed=discord.Embed(
        #         title='Error',
        #         description=f'`{error}`\n`{prefix}help` for a list of commands.',
        #         colour=emcolor
        #     )
        #     footerd(embed)
        #     await ctx.send(f"```{error}\nUse {prefix}help for info about commands.```", delete_after=35)

        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(
                title='Error',
                description=f'`{error}`',
                colour=emcolor
            )
            footerd(embed)
            await ctx.send('```MissingRequiredArgument: Atleast one required argument is missing.```')

        if isinstance(error, commands.BadArgument):
            embed=discord.Embed(
                title='Error',
                description=f'`{error}`',
                colour=emcolor
            )
            footerd(embed)
            await ctx.send(f'```BadArgument: Atleast one invalid argument was given```')

        if isinstance(error, discord.ext.commands.MissingPermissions):
            embed=discord.Embed(
                title='Error',
                description=f'`{error}`',
                colour=emcolor
            )
            footerd(embed)
            await ctx.send(f'```{error}```')

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
