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

    @commands.command(aliases=['message', 'msgs', 'messagecount', 'msgcount'])
    @commands.guild_only()
    async def messages(self, ctx, user: discord.Member = 'self'):
        if user == 'self':
            user = ctx.author

        thing = []

        try:
            for channel in ctx.guild.channels:
                if channel.type == discord.ChannelType.text:
                    async for thing2 in channel.history():
                        if thing2.author == user:
                            thing.append(thing2.content)
                else:
                    pass
        except Exception as er:
            print(er)

        e = discord.Embed(
            description=f'{user.mention} has `{len(thing)}` total messages.',
            color=emcolor
        )
        footera(e)
        await ctx.send(embed=e)

    @commands.command(aliases=['invs'])
    @commands.guild_only()
    async def invites(self, ctx, user: discord.Member = 'self'):
        if user == 'self':
            user = ctx.author

        total = 0
        for i in await ctx.guild.invites():
            if i.inviter == user:
                total += i.uses

        def thing(c: int):
            if c == 1:
                return 'user'
            else:
                return 'users'

        e = discord.Embed(
            description=f'{user.mention} has invited {total} {thing(total)}.',
            color=emcolor
        )
        footera(e)
        await ctx.send(embed=e)

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

    @commands.command(aliases=['whois'])
    @commands.guild_only()
    async def userinfo(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        e = discord.Embed(
            title='User Info',
            color=emcolor
        )

        fields = [
            {'name': 'Username', 'value': f'{user}'},
            {'name': 'ID', 'value': str(user.id)},
            {'name': "Profile Picture", 'value': f'[Direct Link]({user.avatar_url})'},
            {'name': 'Top Role', 'value': user.top_role.mention},
            {'name': "Roles", 'value': f'{len(user.roles)}'},
            {'name': 'Join Position', 'value': str(sorted(ctx.guild.members, key=lambda m: m.joined_at).index(user) + 1)},
            {'name': "Created At", 'value': user.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC")},
            {'name': "Joined Server At", 'value': user.joined_at.strftime("%d/%m/%Y at %H:%M:%S UTC")}
        ]
        for field in fields:
            if field['value']:
                e.add_field(name=field['name'], value=field['value'], inline=True)

        e.set_author(name=f'{user}', icon_url=user.avatar_url)
        footerd(e)

        await ctx.send(embed=e)

    @commands.command(aliases=['fetch_user', 'fetchuser', 'fetchuserinfo'])
    @commands.guild_only()
    async def fetch_userinfo(self, ctx, id_: int = None):
        if id_ == None:
            await ctx.send(f"You need to provide someone to fetch their avatar.\nUsage: `{prefix(ctx.message)}fetchav [user-id]`")
            return

        user = await self.bot.fetch_user(id_)

        e = discord.Embed(
            title='User Info',
            color=emcolor
        )

        fields = [
            {'name': 'Username', 'value': f'{user}'},
            {'name': 'ID', 'value': str(user.id)},
            {'name': "Profile Picture", 'value': f'[Direct Link]({user.avatar_url})'},
            {'name': 'Top Role', 'value': user.top_role.mention},
            {'name': "Roles", 'value': f'{len(user.roles)}'},
            {'name': 'Join Position', 'value': str(sorted(ctx.guild.members, key=lambda m: m.joined_at).index(user) + 1)},
            {'name': "Created At", 'value': user.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC")},
            {'name': "Joined Server At", 'value': user.joined_at.strftime("%d/%m/%Y at %H:%M:%S UTC")}
        ]
        for field in fields:
            if field['value']:
                e.add_field(name=field['name'], value=field['value'], inline=True)

        e.set_author(name=f'{user}', icon_url=user.avatar_url)
        footerd(e)

        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Miscellaneous(bot))