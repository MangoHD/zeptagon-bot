# ------------------------ Modules ------------------------ #

import discord
import asyncio
import random
import datetime
import os
import json
import PIL
import math
import pyfiglet
import requests
import re
import base64
import dyv_math as mfmath
from boto.s3.connection import S3Connection
from PIL import Image
from io import BytesIO
from discord.ext import commands


prefix = ["Z/","z/"]
zept = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive= True)

@zept.event
async def on_ready():
    print("[ LOGS ] :: Made by mutefx#0002, Special thanks to Cylo Hangout")
    print("[ LOGS ] :: File loaded.")
    print("[ LOGS ] :: Token found.")
    print("[ LOGS ] :: Bot started.")
    print(f"[ LOGS ] :: Current prefix is {prefix}")
    print(f"[ LOGS ] :: Logged in as {zept.user.name}#{zept.user.discriminator}.")

# -------------------- Rich Presence ---------------------- #

async def presence():
    await zept.wait_until_ready()

    while not zept.is_closed():
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}help | Dyv"))
        await asyncio.sleep(7)
        await zept.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(dyv.guilds)} servers | Dyv"))
        await asyncio.sleep(7)
        await zept.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{motd} | Dyv'))
        await asyncio.sleep(7)

zept.loop.create_task(presence())

@zept.command()
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
@commands.bot_has_guild_permissions(manage_channels = True)
async def setdelay(ctx, seconds: int,*,channel : discord.TextChannel = None):
    if channel == None:
        channel = ctx.channel
    await channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Ive Set the slowmode delay in {channel.mention} to {seconds} seconds!")

@zept.command(pass_context=True)
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_roles = True)
@commands.bot_has_guild_permissions(manage_roles = True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Hey {ctx.author.name}, I already give {user.mention} role called: {role.mention}")
@zept.command(aliases=['clear'])
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_messages = True)
@commands.bot_has_guild_permissions(manage_messages = True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title=f'Success',
        description=f"**{ctx.author.mention} I've has purged {amount} messages! <a:BlackVerifyCheck:774476123878457354>**",
        color=ctx.author.colour
    
    )
    
    embed.set_author(name=f"Purged",icon_url = f'{client.user.avatar_url}')
    embed.set_footer(text = f'Cycl-Bot Build V4.1')
    await ctx.send(embed=embed)
#channel.
@zept.command(aliases=['cchannel'])
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
@commands.bot_has_guild_permissions(manage_channels = True)
async def createchannel(ctx,*,channel):
    await ctx.guild.create_text_channel(f'{channel}')
    embed = discord.Embed(
        title=f'Success',
        description=f"**I've make the text channel, Channel name : {channel} <a:BlackVerifyCheck:774476123878457354>**",
        color=ctx.author.colour
    
    )
    
    embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
    embed.set_footer(text = f'Cycl-Bot Build V4.1')
    await ctx.send(embed=embed)
@zept.command(aliases=['ccreatevc'])
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
@commands.bot_has_guild_permissions(manage_channels = True)
async def createvc(ctx,*,channel):
    await ctx.guild.create_voice_channel(f'{channel}')
    embed = discord.Embed(
        title=f'Success',
        description=f"**I've make the voice channel, Channel name : {channel} <a:BlackVerifyCheck:774476123878457354>**",
        color=ctx.author.colour
    
    )
    
    embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
    embed.set_footer(text = f'Cycl-Bot Build V4.1')
    await ctx.send(embed=embed)
@zept.command(aliases=['deletech'])
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
@commands.bot_has_guild_permissions(manage_channels = True)
async def deletechannel(ctx,*,channel : discord.TextChannel):
    await channel.delete()
    embed = discord.Embed(
        title=f'Success',
        description=f"**I've delete the voice channel, Channel name : {channel} <a:BlackVerifyCheck:774476123878457354>**",
        color=ctx.author.colour
    
    )
    
    embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
    embed.set_footer(text = f'Cycl-Bot Build V4.1')
    await ctx.send(embed=embed)
@zept.command(aliases=['deletevc'])
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
@commands.bot_has_guild_permissions(manage_channels = True)
async def deletevoichannel(ctx,*,channel : discord.VoiceChannel):
    await channel.delete()
    embed = discord.Embed(
        title=f'Success',
        description=f"**I've delete the coice channel, Channel name : {channel} <a:BlackVerifyCheck:774476123878457354>**",
        color=ctx.author.colour
    
    )
    
    embed.set_author(name=f"{ctx.author.name}",icon_url = f'{ctx.author.avatar_url}')
    embed.set_footer(text = f'Cycl-Bot Build V4.1')
    await ctx.send(embed=embed)
#mods
@zept.command(aliases=['nukes'])
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels = True)
@commands.bot_has_guild_permissions(manage_channels = True)
async def nuke(ctx,*,channel : discord.TextChannel = None):
    if channel == None:
        channel = ctx.channel
    await channel.purge(limit=99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    embed = discord.Embed(
        title=f'Success',
        description=f"**{ctx.author.mention}, Done nuke The channel! <a:BlackVerifyCheck:774476123878457354>**",
        color=ctx.author.colour
    
    )
    
    embed.set_author(name=f"Nuked",icon_url = ctx.author.avatar_url)
    embed.set_footer(text = f'Cycl-Bot Build V4.1')
    await channel.send(embed=embed)

@zept.command()
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(kick_members = True)
@commands.bot_has_guild_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= None):
    if reason == None:
        reason = "No reason provided"
    #kick error
    emd = discord.Embed(
        description=f"**{ctx.author.mention}! <:OkNo:783666946573991987>**\n `No permissions to kick user. Try putting my role above the user's role`",
        color=ctx.author.colour
    
    )
    emd.set_author(name=f"Error Unknown Failure :",icon_url = f'{ctx.author.avatar_url}')
    #kick Dm
    ems = discord.Embed(
        description=f"**You got kicked on {ctx.guild.name}!**\n\n**{ctx.author.name} Has kicked you <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    ems.set_author(name=f"Kicked",icon_url = ctx.author.avatar_url)
    #Kick Message
    em = discord.Embed(
        description=f"**{ctx.author.mention} Has kicked member named : {member.name} <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    em.set_author(name=f"Kicked",icon_url = ctx.author.avatar_url)
    
    try:
        await member.kick(reason=reason)
        await ctx.channel.send(embed=em)
        try:
            await member.send(embed=ems)
        except:
            await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
    except:
        await ctx.send(embed=emd)
#ban Commad
@zept.command()
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(ban_members = True)
@commands.bot_has_guild_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= None):
    if reason == None:
        reason = "No reason provided"
    #kick error
    emd = discord.Embed(
        description=f"**{ctx.author.mention}! <:OkNo:783666946573991987>**\n `No permissions to ban user. Try putting my role above the user's role`",
        color=ctx.author.colour
    
    )
    emd.set_author(name=f"Error Unknown Failure :",icon_url = f'{ctx.author.avatar_url}')
    #kick Dm
    ems = discord.Embed(
        description=f"**You got banned on {ctx.guild.name}!**\n\n**{ctx.author.name} Has banned you <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    ems.set_author(name=f"Banned",icon_url = ctx.author.avatar_url)
    #Kick Message
    em = discord.Embed(
        description=f"**{ctx.author.mention} Has banned member named : {member.name} <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    em.set_author(name=f"Banned",icon_url = ctx.author.avatar_url)
    
    try:
        await member.ban(reason=reason)
        await ctx.channel.send(embed=em)
        try:
            await member.send(embed=ems)
        except:
            await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
    except:
        await ctx.send(embed=emd)

@zept.command()
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(ban_members = True)
@commands.bot_has_guild_permissions(ban_members = True)
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{ctx.author.metion} Has Unbanned {user}!")
            return

#MUTE COMMAND
@zept.command()
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(administrator=True)
@commands.bot_has_guild_permissions(administrator=True)
async def mute(ctx,member : discord.Member,*,reason = None):
    if reason == None:
        reason = "No Reason Provided"

    emd = discord.Embed(
        description=f"**{ctx.author.mention}! <:OkNo:783666946573991987>**\n `No permissions to mute user. Try giving me manage roles perms!`",
        color=ctx.author.colour
    
    )
    emd.set_author(name=f"Error Unknown Failure :",icon_url = f'{client.user.avatar_url}')
    emd.set_footer(icon_url = "https://media.discordapp.net/attachments/739065668896292877/783989643196629002/cyclbot.png" , text = f'Cycl-Bot Build V4.1')
    #kick Dm
    ems = discord.Embed(
        description=f"**You got muted on {ctx.guild.name}!**\n**{ctx.author.name} Has muted you <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    ems.set_author(name=f"Muted",icon_url = "https://media.discordapp.net/attachments/739065668896292877/783989643196629002/cyclbot.png")
    ems.set_footer(icon_url = "https://media.discordapp.net/attachments/739065668896292877/783989643196629002/cyclbot.png" , text = f'Cycl-Bot Build V4.1')
    #Kick Message
    em = discord.Embed(
        description=f"**{ctx.author.mention} Has muted member named : {member.name} <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    em.set_author(name=f"Muted",icon_url = "https://media.discordapp.net/attachments/739065668896292877/783989643196629002/cyclbot.png")
    em.set_footer(icon_url = "https://media.discordapp.net/attachments/739065668896292877/783989643196629002/cyclbot.png" , text = f'Cycl-Bot Build V4.1')
    mutessd = ['Muted','muted']
    try:
        role = discord.utils.get(ctx.guild.roles, name=f'{mutessd}')
        await member.add_roles(role)
        await ctx.channel.send(embed=em)
        try:
            await member.send(embed=ems)
        except:
            await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
    except:
        await ctx.send(embed=emd)
#UNMUTE COMMANDS
@zept.command()
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(administrator=True)
@commands.bot_has_guild_permissions(administrator=True)
async def unmute(ctx,member : discord.Member,*,reason= None):
    mutessd = ['Muted','muted']
    if reason == None:
        reason = "No Reason Provided"
    role = discord.utils.get(ctx.guild.roles, name=mutessd)
    emd = discord.Embed(
        description=f"**{ctx.author.mention}! <:OkNo:783666946573991987>*\n `No permissions to unmute user. Try giving me manage roles perms!`",
        color=ctx.author.colour
    
    )
    emd.set_author(name=f"Error Unknown Failure :",icon_url = f'{client.user.avatar_url}')
    emd.set_footer(text = f'Cycl-Bot Build V4.1')
    #kick Dm
    ems = discord.Embed(
        description=f"**You got unmuted on {ctx.guild.name}!**\n**{ctx.author.name} Has unmuted you <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    ems.set_author(name=f"Unmuted",icon_url = ctx.author.avatar_url)
    ems.set_footer(text = f'Cycl-Bot Build V4.1')
    #Kick Message
    em = discord.Embed(
        description=f"**{ctx.author.mention} Has unmuted member named : {member.name} <a:BlackVerifyCheck:774476123878457354>\n\n Reason = {reason}**",
        color=ctx.author.colour
    
    )
    
    em.set_author(name=f"Unmuted",icon_url = ctx.author.avatar_url)
    em.set_footer(text = f'Cycl-Bot Build V4.1')
    
    try:
        await member.remove_roles(role)
        await ctx.channel.send(embed=em)
        try:
            await member.send(embed=ems)
        except:
            await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
    except:
        await ctx.send(embed=emd)
