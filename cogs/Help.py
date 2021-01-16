import discord
import os
import asyncio
import datetime
import random
import json
from discord.ext import commands
from bot_things import  motd, emcolor, ercolor, footerd, getprefix, get_prefix, prefix

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="help", aliases=["commands"], invoke_without_command=True)
    @commands.guild_only()
    async def help(self, ctx):
        await ctx.trigger_typing()    
        emb = discord.Embed(
            title='Help Commands',
            description='Current prefix is `{}`'.format(prefix(ctx.message)),
            color=emcolor,
            timestamp=datetime.datetime.utcnow())
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

    @help.command(aliases=['giveaways', 'gw', 'gws'])
    async def giveaway(self, ctx):
        await ctx.trigger_typing()
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

    @help.command(aliases=['utilities'])
    async def utils(self, ctx):
        await ctx.trigger_typing()
        e = discord.Embed(
            title='Utility Commands',
            description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
            f"`{prefix(ctx.message)}ping` - Checks the bot's ping.\n"
            f"`{prefix(ctx.message)}pingweb [http]` - Pings a website and checks the status.\n"
            f"`{prefix(ctx.message)}invite` - Invite link for the bot.\n",
            color=emcolor,
            timestamp=datetime.datetime.utcnow()
        )
        footerd(e)
        await ctx.send(embed=e)

    @help.command()
    async def config(self, ctx):
        await ctx.trigger_typing()
        e = discord.Embed(
            title='Configuration Commands',
            description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
            f"`{prefix(ctx.message)}setprefix <prefix>` - Sets a custom prefix for your server.\n"
            f"`{prefix(ctx.message)}muterole <@role>` - Sets the muterole for your server.\n",
            color=emcolor,
            timestamp=datetime.datetime.utcnow()
        )
        footerd(e)
        await ctx.send(embed=e)

    @help.command(aliases=['calculator', 'maths', 'calc'])
    async def math(self, ctx):
        await ctx.trigger_typing()
        e = discord.Embed(
            title='Math Commands',
            description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
            f"`{prefix(ctx.message)}randomnum [min] [max]` - Picks a random number between the minimum and maximum\n"
            f"`{prefix(ctx.message)}add [num] [num]` - Adds the given numbers.\n"
            f"`{prefix(ctx.message)}substract [num] [num]` - Substracts the given numbers.\n"
            f"`{prefix(ctx.message)}multiply [num] [num]` - Multiplies the given numbers.\n"
            f"`{prefix(ctx.message)}divide [num] [num]` - Divides the given numbers.\n",
            color=emcolor,
            timestamp=datetime.datetime.utcnow()
        )
        footerd(e)
        await ctx.send(embed=e)

    @help.command(aliases=['moderation', 'admin', 'mods'])
    async def mod(self, ctx):
        await ctx.trigger_typing()
        e = discord.Embed(
            title='Moderation Commands',
            description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
            f"`{prefix(ctx.message)}addrole [user] [role]` - Gives a user a role.\n"
            f"`{prefix(ctx.message)}removerole [user] [role]` - Removes a user's a role.\n"
            f"`{prefix(ctx.message)}slowmode [time] <channel>` - Sets slowmode for a channel.\n"
            f"`{prefix(ctx.message)}purge [amount]` - Deletes an amount of messages for the current channel.\n"
            f"`{prefix(ctx.message)}nuke <channel>` - Deletes all messages in a channel.\n"
            f"`{prefix(ctx.message)}ban [user] <reason>` - Bans a user.\n"
            f"`{prefix(ctx.message)}kick [user] <reason>` - Kicks a user.\n"
            f"`{prefix(ctx.message)}warn [user] [reason]` - Warns a user with a specified reason.\n"
            f"`{prefix(ctx.message)}warns <user>` - Checks warnings for a user.\n"
            f"`{prefix(ctx.message)}clearwarns [user]` - Removes a user's warnings.\n"
            f"`{prefix(ctx.message)}mute [user] <mins>` - Mutes a user for an amount of minutes.\n"
            f"`{prefix(ctx.message)}unmute [user]` - Unmutes a user that is muted.\n"
            f"`{prefix(ctx.message)}setup` - Sets up the muterole for the current server.",
            color=emcolor,
            timestamp=datetime.datetime.utcnow()
        )
        footerd(e)
        await ctx.send(embed=e)

    @help.command(aliases=['pics', 'pictures', 'img', 'images'])
    async def image(self, ctx):
        await ctx.trigger_typing()
        e = discord.Embed(
            title='Image Commands',
            description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
            f"`{prefix(ctx.message)}meme` - Sends a random reddit meme.\n"
            f"`{prefix(ctx.message)}ytcomment [comment]` - Makes a youtube comment.\n"
            f"`{prefix(ctx.message)}tweet [msg]` - Makes a tweet.\n"
            # f"`{prefix(ctx.message)}wanted <@user>` - Adds a wanted overlay to someone.\n"
            # f"`{prefix(ctx.message)}triggered <@user>` - Adds a triggered overlay to someone.\n"
            f"`{prefix(ctx.message)}gay` - Rainbow overlay over someone.\n"
            f"`{prefix(ctx.message)}fox` - Random Fox Image.\n"
            f"`{prefix(ctx.message)}cat` - Random Cat Image.\n"
            f"`{prefix(ctx.message)}panda` - Random Panda Image.\n"
            f"`{prefix(ctx.message)}dog` - Random Dog Image.\n"
            f"`{prefix(ctx.message)}koala` - Random Koala Image.\n"
            f"`{prefix(ctx.message)}bird` - Random Bird Image.\n",
            color=emcolor,
            timestamp=datetime.datetime.utcnow()
        )
        footerd(e)
        await ctx.send(embed=e)

    @help.command(aliases=['miscellaneous', 'msc', 'miscs'])
    async def misc(self, ctx):
        await ctx.trigger_typing()
        e = discord.Embed(
            title='Miscellaneous Commands',
            description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
            f"`{prefix(ctx.message)}poll [options..]` - Creates a poll with the given questions.\n"
            f"`{prefix(ctx.message)}serverinfo` - Statistics for the current server.\n"
            f"`{prefix(ctx.message)}whois <user>` - Information for a user.\n"
            f"`{prefix(ctx.message)}messages <user>` - Checks amount of messages a user sent. (bugged)\n"
            f"`{prefix(ctx.message)}invites <user>` - Checks how many people were invited by a user.\n"
            f"`{prefix(ctx.message)}avatar <user>` - A user's avatar.\n"
            f"`{prefix(ctx.message)}fetchav [id]` - Fetches an avatar from a user that is not in the server.\n"
            f"`{prefix(ctx.message)}fetchuser [id]` - Fetches basic information for a user that is not in the server.\n",
            color=emcolor,
            timestamp=datetime.datetime.utcnow()
        )
        footerd(e)
        await ctx.send(embed=e)

    @help.command(aliases=['funny', 'funn', 'stuff'])
    async def fun(self, ctx):
        await ctx.trigger_typing()
        e = discord.Embed(
            title='Fun Commands',
            description=f'Current prefix is `{prefix(ctx.message)}`.\n\n'
            f"`{prefix(ctx.message)}8ball [question]` - Magic 8Ball.\n"
            f"`{prefix(ctx.message)}gifsearch [query]` - Finds the gif online.\n"
            f"`{prefix(ctx.message)}imgsearch [query]` - Finds an image online.\n"
            f"`{prefix(ctx.message)}encode [text]` - Encodes a message to Base64.\n"
            f"`{prefix(ctx.message)}decode [text]` - Decodes a message from Base64.\n"
            f"`{prefix(ctx.message)}spacetext [text]` - Adds spaces between letters.\n"
            f"`{prefix(ctx.message)}ascii [text]` - Makes a large text.\n"
            f"`{prefix(ctx.message)}regional [text]` - Makes a text in regional indicator font.\n"
            f"`{prefix(ctx.message)}hack <user>` - Hacks a user. (fake)\n"
            f"`{prefix(ctx.message)}findip <user>` - Finds a user's IP (fake)\n"
            f"`{prefix(ctx.message)}clap [text]` - Adds claps between words.\n"
            f"`{prefix(ctx.message)}1337 [text]` - 1337 speak.\n"
            f"`{prefix(ctx.message)}embed [query]` - Makes an embed with given queries.\n"
            f"`{prefix(ctx.message)}unfunny` - Tells someone how unfunny they are.\n"
            f"`{prefix(ctx.message)}dice` - Rolls a virtual dice\n"
            f"`{prefix(ctx.message)}flipcoin` - Flips a virtual coin.\n"
            f"`{prefix(ctx.message)}iq <user>` - How smart a user is.\n"
            f"`{prefix(ctx.message)}howgay <user>` - How gay someone is.\n"
            f"`{prefix(ctx.message)}howsimp <user>` - How much of a simp someone is.\n",
            color=emcolor,
            timestamp=datetime.datetime.utcnow()
        )
        footerd(e)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Help(bot))
