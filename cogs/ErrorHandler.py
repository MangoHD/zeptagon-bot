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
        GuildOnly = (isinstance(error, commands.NoPrivateMessage))
        MissingArgs = (isinstance(error, commands.MissingRequiredArgument))
        MissingPerms = (isinstance(error, discord.ext.commands.MissingPermissions))

        if GuildOnly:
            return await ctx.send("Error: commands cannot be used in Direct Messages.".format(cmd=ctx.message.content.split(' ')[0]))

        elif MissingArgs:
            return await ctx.send('**Missing Arguments:** Atleast one required argument is missing.')

        elif MissingPerms:
            return await ctx.send(f'{error}')

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
