import discord
import os
import asyncio
import datetime
import random
import json
from discord.ext import commands
from bot_things import  motd, emcolor, ercolor, footerd, getprefix, get_prefix

def prefix(message):
    with open("./configs/prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return 'z!'

    else:
        prefix = prefixes[str(message.guild.id)]
        return prefix

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['commands'])
    @commands.guild_only()
    async def help(self, ctx, page = 'None'):
        if page == 'None':
            emb = discord.Embed(
                title='Help Commands',
                description='Current prefix is `{}`'.format(prefix(ctx.message)),
                color=emcolor,
                timestamp=datetime.datetime.utcnow()
            )

            fields = [
                {'name': '🎈 Fun', 'value': f"`{prefix(ctx.message)}help fun`\nA list of some fun and random commands you could use."},
                {'name': '📷 Image', 'value': f"`{prefix(ctx.message)}help image`\nImage commands, there's lots here too."},
                {'name': '➕ Math', 'value': f"`{prefix(ctx.message)}help math`\nYou need help in math? Here's the calculator."},
                {'name': '🎉 Giveaway', 'value': f"`{prefix(ctx.message)}help giveaway`\nGiveaway commands are used a lot. How can we not have it?"},
                {'name': '✨ Miscellaneous', 'value': f"`{prefix(ctx.message)}help misc`\nMiscellaneous commands are also here."},
                {'name': '🔧 Moderation', 'value': f"`{prefix(ctx.message)}help mod`\nModeration, used to help moderate your server."},
                {'name': '📨 Utilities', 'value': f"`{prefix(ctx.message)}help utils`\nUtility commands, ping command, bot-info, etc.."},
                {'name': '⚙ Configuration', 'value': f"`{prefix(ctx.message)}help config`\nConfiguration commands for the server, includes custom server prefixes."}
            ]

            for field in fields:
                if field['value']:
                    emb.add_field(name=field['name'], value=field['value'], inline=False)

            footerd(emb)

            await ctx.send(embed=emb)
        
        elif page == 'giveaway':
            e = discord.Embed(
                title='Giveaway Commands',
                description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
                f"`{prefix(ctx.message)}gstart` - Asks some questions and starts a giveaway.\n"
                f"`{prefix(ctx.message)}greroll [msg-id]` - Re-rolls a giveaway.\n"
                f"`{prefix(ctx.message)}gend [msg-id]` - Ends a giveway before the supposed time.",
                color=emcolor,
                timestamp=datetime.datetime.utcnow()
            )

            footerd(e)

            await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Help(bot))
