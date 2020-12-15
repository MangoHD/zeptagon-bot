import discord
import os
import asyncio
import datetime
import random
from discord.ext import commands
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['commands'])
    @commands.guild_only()
    async def help(self, ctx, page: int = 1):
        emb = discord.Embed(
            title='Help Commands',
            description='Current prefix is ',
            color=emcolor
        )

        fields = [
            {'name': 'Giveaway', 'value': f"`{prefix}help giveaway`\nMainly focused on giveaway commands. How can we not have it?"},
            {'name': 'Fun', 'value': f"`{prefix}help fun`"},
            {'name': 'Miscellaneous', 'value': f"`{prefix}help misc`"},
            {'name': 'Image', 'value': f"`{prefix}help image`"},
            {'name': 'Moderation', 'value': f"`{prefix}help mod`"},
            {'name': 'Math', 'value': f"`{prefix}help math`"},
            {'name': 'Utilities', 'value': f"`{prefix}help utils`"},
            {'name': 'Configuration', 'value': f"`{prefix}help config`"}
        ]

        for field in fields:
            if field['value']:
                emb.add_field(name=field['name'], value=field['value'], inline=False)

        footerd(emb)

        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Help(bot))
