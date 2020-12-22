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

    @commands.command(aliases=['poll'])
    @commands.has_permissions(manage_messages=True)
    async def poll_cmd(self, ctx, title, q1, q2, q3 = '-none', q4 = '-none', q5 = '-none', q6 = '-none'):
        if q3 == '-none':
            emb0 = discord.Embed(
                title=title,
                description=f"\n\n1️⃣ {q1}\n2️⃣ {q2}\n\nPoll By: {ctx.author.mention}",
                colour=emcolor)
            emb0.set_thumbnail(url=ctx.author.avatar_url)
            emb0.set_footer(text=f"Requested By {ctx.author.name}#{ctx.author.discriminator}")
            msg0 = await ctx.channel.send(embed=emb0)
            await msg0.add_reaction('1️⃣')
            await msg0.add_reaction('2️⃣')
            return
        if q4 == '-none':
            emb0 = discord.Embed(
                title=title,
                description=f"\n\n1️⃣ {q1}\n2️⃣ {q2}\n3️⃣ {q3}\n\nPoll By: {ctx.author.mention}",
                colour=emcolor)
            emb0.set_thumbnail(url=ctx.author.avatar_url)
            footerd(emb0)
            msg0 = await ctx.channel.send(embed=emb0)
            await msg0.add_reaction('1️⃣')
            await msg0.add_reaction('2️⃣')
            await msg0.add_reaction('3️⃣')
            return
        if q5 == '-none':
            emb0 = discord.Embed(
                title=title,
                description=f"\n\n1️⃣ {q1}\n2️⃣ {q2}\n3️⃣ {q3}\n4️⃣ {q4}\n\nPoll By: {ctx.author.mention}",
                colour=emcolor)
            emb0.set_thumbnail(url=ctx.author.avatar_url)
            footerd(emb0)
            msg0 = await ctx.channel.send(embed=emb0)
            await msg0.add_reaction('1️⃣')
            await msg0.add_reaction('2️⃣')
            await msg0.add_reaction('3️⃣')
            await msg0.add_reaction('4️⃣')
            return
        if q6 == '-none':
            emb0 = discord.Embed(
                title=title,
                description=f"\n\n1️⃣ {q1}\n2️⃣ {q2}\n3️⃣ {q3}\n4️⃣ {q4}\n5️⃣ {q5}\n️\nPoll By: {ctx.author.mention}",
                colour=emcolor)
            emb0.set_thumbnail(url=ctx.author.avatar_url)
            footerd(emb0)
            msg0 = await ctx.channel.send(embed=emb0)
            await msg0.add_reaction('1️⃣')
            await msg0.add_reaction('2️⃣')
            await msg0.add_reaction('3️⃣')
            await msg0.add_reaction('4️⃣')
            await msg0.add_reaction('5️⃣')
            return
        emb0 = discord.Embed(
            title=title,
            description=f"\n\n1️⃣ {q1}\n2️⃣ {q2}\n3️⃣ {q3}\n4️⃣ {q4}\n5️⃣ {q5}\n️6️⃣ {q6}\n\nPoll By: {ctx.author.mention}",
            colour=emcolor)
        emb0.set_thumbnail(url=ctx.author.avatar_url)
        footerd(emb0)
        msg0 = await ctx.channel.send(embed=emb0)
        await msg0.add_reaction('1️⃣')
        await msg0.add_reaction('2️⃣')
        await msg0.add_reaction('3️⃣')
        await msg0.add_reaction('4️⃣')
        await msg0.add_reaction('5️⃣')
        await msg0.add_reaction('6️⃣')
        return

    @commands.command(aliases=['serverinfo'])
    @commands.guild_only()
    async def serverstats(self, ctx):
        embed = discord.Embed(
            title='Server Info', 
            description=f'Info for Guild: **{ctx.guild}**', 
            colour=emcolor)
        if ctx.guild.features == []:
            perk_strng = 'No Perks'
        else:
            perk_strng = ', '.join([str(p).replace("_", " ").title() for p in ctx.guild.features if p[1]])
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Guild Name", value=f"{ctx.guild.name}", inline=True)
        embed.add_field(name='Roles', value=f'{len(ctx.guild.roles)}')
        embed.add_field(name='Guild Logo', value=f'[Direct Link]({ctx.guild.icon_url})', inline=True)
        embed.add_field(name='Members', value=f"{ctx.guild.member_count}")
        embed.add_field(name='Owner', value=f'<@!{ctx.message.author.guild.owner_id}>', inline=True)
        embed.add_field(name='Channels', value=f'<:vc:790390770112266280> {len(ctx.guild.text_channels)}\n<:tc:790390769902944286> {len(ctx.guild.voice_channels)}')
        embed.add_field(name="Guild ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Created At", value=ctx.guild.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC"), inline=True)
        embed.add_field(name='Region', value=ctx.guild.region, inline=True)
        embed.add_field(name='VIP Perks', value=perk_strng)
        footerd(embed)
        await ctx.send(embed=embed)

    @commands.command(aliases=['whois'])
    @commands.guild_only()
    async def userinfo(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        e = discord.Embed(
            title='User Info',
            color=emcolor
        )
        if len(user.roles) > 1:
            role_string = ', '.join([f"**`{r.name}`**" for r in user.roles][1:])
        else:
            role_string = 'No Roles'
        if 'Administrator' in [str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]]:
            perm_string = 'All Permissions'
        else:
            perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        fields = [
            {'name': 'Username', 'value': f'{user}'},
            {'name': 'ID', 'value': str(user.id)},
            {'name': "Profile Picture", 'value': f'[Direct Link]({user.avatar_url})'},
            {'name': 'Top Role', 'value': user.top_role.mention},
            {'name': "Role Count", 'value': f'{len(user.roles)}'},
            {'name': "Created At", 'value': user.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC")},
            {'name': "Joined Server At", 'value': user.joined_at.strftime("%d/%m/%Y at %H:%M:%S UTC")},
            {'name': "Roles", 'value': role_string}
        ]
        for field in fields:
            if field['value']:
                try:
                    e.add_field(name=field['name'], value=field['value'], inline=True)
                except Exception as _er:
                    await ctx.send("```{}```".format(_er))
        e.add_field(name="Permissions", value=perm_string, inline=False)
        e.set_thumbnail(url=user.avatar_url)
        e.set_author(name=f'{user}', icon_url=user.avatar_url)
        footerd(e)
        await ctx.send(embed=e)

    @userinfo.error
    async def whois_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found.")

    @commands.command(aliases=['message', 'msgs', 'messagecount', 'msgcount'])
    @commands.guild_only()
    async def messages(self, ctx, user: discord.Member = 'self'):
        if user == 'self':
            user = ctx.author
        thing = 0
        try:
            for channel in ctx.guild.text_channels:
                async for thing2 in channel.history(limit=None):
                    if thing2.author == user:
                        thing = thing + 1
        except Exception as er:
            print(er)

        e = discord.Embed(
            description=f'{user.mention} has `{len(thing)}` total messages.\nNote: The counter only counts the last 25000 messages.',
            color=emcolor)
        footera(e)
        await ctx.send(embed=e)

    @messages.error
    async def msgs_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found.")

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

    @invites.error
    async def invs_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found.")

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

    @avatar.error
    async def av_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found.")

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

    @fetchavatar.error
    async def fetchav_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found.")

    @commands.command(aliases=['fetch_user', 'fetchuser', 'fetchuserinfo'])
    @commands.guild_only()
    async def fetch_userinfo(self, ctx, id_: int = None):
        if id_ == None:
            return await ctx.send(f"You need to provide someone to fetch their profile.\nUsage: `{prefix(ctx.message)}fetchuser [user-id]`")
        user = await self.bot.fetch_user(id_)
        e = discord.Embed(
            title='User Info',
            color=emcolor)
        fields = [
            {'name': 'Username', 'value': f'{user}'},
            {'name': 'ID', 'value': str(user.id)},
            {'name': "Profile Picture", 'value': f'[Direct Link]({user.avatar_url})'},
            {'name': "Created At", 'value': user.created_at.strftime("%d/%m/%Y at %H:%M:%S UTC")}
        ]
        for field in fields:
            if field['value']:
                e.add_field(name=field['name'], value=field['value'], inline=True)
        e.set_thumbnail(url=user.avatar_url)
        e.set_author(name=f'{user}', icon_url=user.avatar_url)
        footerd(e)

        await ctx.send(embed=e)

    @fetch_userinfo.error
    async def fetchuser_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found.")

def setup(bot):
    bot.add_cog(Miscellaneous(bot))