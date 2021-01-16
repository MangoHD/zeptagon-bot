import discord
import os
import json
import asyncio
import datetime
import random
from discord.ext import commands
from discord import Embed, Color
from bot_things import prefix, motd, emcolor, ercolor, footerd, footera, getprefix, get_prefix, timei, theJsonDump

def joinMsgCheck(member):
    with open("./configs/serverconfs.json", "r") as f:
        conf = json.load(f)
    try:
        check = conf[str(member.guild.id)]["events"]["joinMsg"]["enabled"]
        return check
    except KeyError:
        with open("./configs/serverconfs.json", "w") as f:
            conf[f"{member.guild.id}"] = theJsonDump
            json.dump(conf, f, indent=4)
        check = conf[str(member.guild.id)]["events"]["joinMsg"]["enabled"]
        return check
        
def leaveMsgCheck(member):
    with open("./configs/serverconfs.json", "r") as f:
        conf = json.load(f)
    try:
        check = conf[str(member.guild.id)]["events"]["leaveMsg"]["enabled"]
        return check
    except KeyError:
        with open("./configs/serverconfs.json", "w") as f:
            conf[f"{member.guild.id}"] = theJsonDump
            json.dump(conf, f, indent=4)
        check = conf[str(member.guild.id)]["events"]["leaveMsg"]["enabled"]
        return check

def checkChannel(_type: str, member):
    with open("./configs/serverconfs.json", "r") as f:
        conf = json.load(f)
    try:
        check = conf[str(member.guild.id)]["events"][f"{_type}Msg"]["channel"]
        return check
    except KeyError:
        with open("./configs/serverconfs.json", "w") as f:
            conf[f"{member.guild.id}"] = theJsonDump
            json.dump(conf, f, indent=4)
        check = conf[str(member.guild.id)]["events"][f"{_type}Msg"]["channel"]
        return check

class JoinStuffs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if joinMsgCheck(member) == True:
            with open("./configs/serverconfs.json", "r") as f:
                conf = json.load(f)
            try:
                asd = conf[f"{str(member.guild.id)}"]["events"]["joinMsg"]
                cnl = await member.guild.fetch_channel(int(asd["channel"]))
                if "{user}" in asd["message"]:
                    a = asd["message"].replace("{user}", f"{member.mention}")
                else:
                    a = asd["message"]
                if "{server}" in a:
                    b = a.replace("{server}", f"{member.guild.name}")
                else:
                    b = a
                await cnl.send(f"{b}")
            except Exception as _er:
                try:
                    asd = conf[f"{str(member.guild.id)}"]["events"]["joinMsg"]
                    cnl = await member.guild.fetch_channel(int(asd["channel"]))
                    await cnl.send("```{}```".format(_er))
                except KeyError:
                    with open("./configs/serverconfs.json", "w") as f:
                        conf[f"{member.guild.id}"] = theJsonDump
                        json.dump(conf, f, indent=4)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if leaveMsgCheck(member) == True:
            with open("./configs/serverconfs.json", "r") as f:
                conf = json.load(f)
            try:
                asd = conf[f"{str(member.guild.id)}"]["events"]["leaveMsg"]
                cnl = await member.guild.fetch_channel(int(asd["channel"]))
                if "{user}" in asd["message"]:
                    a = asd["message"].replace("{user}", f"{member.mention}")
                else:
                    a = asd["message"]
                if "{server}" in a:
                    b = a.replace("{server}", f"{member.guild.name}")
                else:
                    b = a
                await cnl.send(f"{b}")
            except Exception as _er:
                try:
                    asd = conf[f"{str(member.guild.id)}"]["events"]["leaveMsg"]
                    cnl = await member.guild.fetch_channel(int(asd["channel"]))
                    await cnl.send("```{}```".format(_er))
                except KeyError:
                    with open("./configs/serverconfs.json", "w") as f:
                        conf[f"{member.guild.id}"] = theJsonDump
                        json.dump(conf, f, indent=4)

    @commands.command(aliases=["joinmsg"])
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    async def joinmessage(self, ctx, args = None, *, __args__ = None):
        if args == None:
            return await ctx.send("Please provide an option to use.\nAvailable: `set`, `enable`, `disable`, `channel`.\nUsage: `{}joinmessage [option] <args..>`".format(prefix(ctx.message)))
        elif args == 'set':
            if joinMsgCheck(ctx) is True:
                if checkChannel("join", ctx) is None:
                    return await ctx.send("Join messages channel is not set. To set it up using `{}joinmessage channel [channel]`.".format(prefix(ctx.message)))
                else:
                    with open("./configs/serverconfs.json", "r") as f:
                        conf = json.load(f)
                    try:
                        conf[str(ctx.guild.id)]["events"]["joinMsg"]["message"] = f"{__args__}"
                        with open("./configs/serverconfs/json", "w") as f:
                            json.dump(conf, f, indent=4)
                        if "{user}" in __args__:
                            a = __args__.replace("{user}", f"{ctx.author.mention}")
                        else:
                            a = __args__
                        if "{server}" in a:
                            b = a.replace("{server}", f"{ctx.guild.name}")
                        else:
                            b = a
                        await ctx.send(f"Set welcome message to `{__args__}`.\n\nPreview: {b}")
                    except KeyError:
                        with open("./configs/serverconfs.json", "w") as f:
                            conf[f"{ctx.guild.id}"] = theJsonDump
                            json.dump(conf, f, indent=4)
                            conf[str(ctx.guild.id)]["events"]["joinMsg"]["message"] = f"{__args__}"
                            json.dump(conf, f, indent=4)
                        if "{user}" in __args__:
                            a = __args__.replace("{user}", f"{ctx.author.mention}")
                        else:
                            a = __args__
                        if "{server}" in a:
                            b = a.replace("{server}", f"{ctx.guild.name}")
                        else:
                            b = a
                        await ctx.send(f"Set welcome message to `{__args__}`.\n\nPreview: {b}")
            else:
                return await ctx.send("The welcome messages for this server is not enabled. To turn it on, type `{}joinmessage enable`".format(prefix(ctx.message)))

        elif args == 'enable':
            with open("./configs/serverconfs.json", "r") as f:
                conf = json.load(f)
            try:
                conf[str(ctx.guild.id)]["events"]["joinMsg"]["enabled"] = True
                with open("./configs/serverconfs.json", "w") as f:
                    json.dump(conf, f, indent=4)
                return await ctx.send("Successfully enabled join messages for this server.\nNote: The join messages channel has not been set. To set it up, use `{}joinmessage channel [channel]`".format(prefix(ctx.message)))
            except KeyError:
                with open("./configs/serverconfs.json", "w") as f:
                    conf[f"{ctx.guild.id}"] = theJsonDump
                    json.dump(conf, f, indent=4)
                    conf[str(ctx.guild.id)]["events"]["joinMsg"]["enabled"] = True
                    json.dump(conf, f, indent=4)
                return await ctx.send("Successfully enabled join messages for this server.\nNote: The join messages channel has not been set. To set it up, use `{}joinmessage channel [channel]`".format(prefix(ctx.message)))

        elif args == 'disable':
            with open("./configs/serverconfs.json", "r") as f:
                conf = json.load(f)
            try:
                conf[str(ctx.guild.id)]["events"]["joinMsg"]["enabled"] = False
                with open("./configs/serverconfs.json", "w") as f:
                    json.dump(conf, f, indent=4)
                return await ctx.send("Successfully disabled join messages for this server.\nNote: The join messages channel has not been set. To set it up, use `{}joinmessage channel [channel]`".format(prefix(ctx.message)))
            except KeyError:
                with open("./configs/serverconfs.json", "w") as f:
                    conf[f"{ctx.guild.id}"] = theJsonDump
                    json.dump(conf, f, indent=4)
                    conf[str(ctx.guild.id)]["events"]["joinMsg"]["enabled"] = False
                    json.dump(conf, f, indent=4)
                return await ctx.send("Successfully disabled join messages for this server.\nNote: The join messages channel has not been set. To set it up, use `{}joinmessage channel [channel]`".format(prefix(ctx.message)))

        elif args == "channel":
            try:
                channel = int(__args__[2:-1])
                __ch__ = await self.bot.fetch_channel(channel)
                try:
                    with open("./configs/serverconfs.json", "r") as f:
                        conf = json.load(f)
                    conf[str(ctx.guild.id)]["events"]["joinMsg"]["channel"] = int(channel)
                    with open("./configs/serverconfs.json", "w") as f:
                        json.dump(conf, f, indent=4)
                    await ctx.send("Set join messages channel as {}.".format(__ch__.mention))
                except KeyError:
                    with open("./configs/serverconfs.json", "w") as f:
                        conf[f"{ctx.guild.id}"] = theJsonDump
                        json.dump(conf, f, indent=4)
                        conf[str(ctx.guild.id)]["events"]["joinMsg"]["channel"] = int(channel)
                        json.dump(conf, f, indent=4)
                    await ctx.send("Set join messages channel as {}.".format(__ch__.mention))
            except ValueError:
                try:
                    __ch__ = await self.bot.fetch_channel(int(__args__))
                    with open("./configs/serverconfs.json", "r") as f:
                        conf = json.load(f)
                    conf[str(ctx.guild.id)]["events"]["joinMsg"]["channel"] = int(__ch__.id)
                    with open("./configs/serverconfs.json", "w") as f:
                        json.dump(conf, f, indent=4)
                    await ctx.send("Set join messages channel as {}.".format(__ch__.mention))
                except KeyError:
                    with open("./configs/serverconfs.json", "w") as f:
                        conf[f"{ctx.guild.id}"] = theJsonDump
                        json.dump(conf, f, indent=4)
                        conf[str(ctx.guild.id)]["events"]["joinMsg"]["channel"] = int(__ch__.id)
                        json.dump(conf, f, indent=4)
                    await ctx.send("Set join messages channel as {}.".format(__ch__.mention))

def setup(bot):
    bot.add_cog(JoinStuffs(bot))