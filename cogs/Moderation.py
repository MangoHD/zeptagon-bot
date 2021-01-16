import discord
import os
import asyncio
import json
from discord.ext import commands
from discord import Embed, Color
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['slowmode'])
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def setdelay(self, ctx, seconds: int, *, channel: discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel
        try:
            await channel.edit(slowmode_delay=seconds)
            await ctx.send(f'Successfully changed slowmode to `{seconds}` seconds.')
        except Exception as e:
            await ctx.send(f"```{e}```")

    @setdelay.error
    async def setdelay_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Channel not found.")

    @commands.command(pass_context=True, aliases=['giveallroles'])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    async def addallroles(self, ctx, *, role: discord.Role):
        f = 0
        async for _member in ctx.guild.fetch_members(limit=None):
            try:
                await _member.add_roles(role)
                f = f + 1
            except:
                pass
        await ctx.send("Successfully added roles to **{}** users.".format(f))

    @addallroles.error
    async def addallroles_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Role not found.")

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    async def removeallroles(self, ctx, *, role: discord.Role):
        f = 0
        async for _member in ctx.guild.fetch_members(limit=None):
            try:
                await _member.remove_roles(role)
                f = f + 1
            except:
                pass
        await ctx.send("Successfully added roles to **{}** users.".format(f))

    @removeallroles.error
    async def removeallroles_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Role not found.")

    @commands.command(pass_context=True, aliases=['addrole'])
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def giverole(self, ctx, user: discord.Member, *, role: discord.Role):
        if user.top_role > ctx.author.top_role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        if user.top_role < role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        if ctx.author.top_role < role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        try:
            await user.add_roles(role)
            await ctx.send(f"{ctx.author.mention}, given **{user.display_name}** the **{role.name}** role.")
        except Exception as e:
            await ctx.send(f'```{e}```')

    @giverole.error
    async def giverl_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Either user or role is not found.\nUsage: `{prefix(ctx.message)}giverole [user] [role]`")

    @commands.command(pass_context=True, aliases=['remrole'])
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def removerole(self, ctx, user: discord.Member, *, role: discord.Role):
        admin = ("administrator" in user.guild_permissions)
        if admin:
            return await ctx.send("You cannot remove a server admin's role.")
        if user.top_role > ctx.author.top_role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        if user.top_role < role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        if ctx.author.top_role < role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        try:
            await user.remove_roles(role)
            await ctx.send(f"{ctx.author.mention}, removed **{user.display_name}**'s **{role.name}** role.")
        except Exception as e:
            await ctx.send(f'```{e}```')

    @removerole.error
    async def remvrl_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Either user or role is not found.\nUsage: `{prefix(ctx.message)}removerole [user] [role]`")

    @commands.command(aliases=['clear'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount: int):
        try:
            if amount < 501:
                await ctx.channel.purge(limit=amount+1)
                await ctx.send("Deleted {} messages.".format(amount))
            else:
                await ctx.send("Unable to delete messages. I am only able to remove **500** or less messages.")
        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, *, channel: discord.TextChannel = None):
        if channel == None:
            new_channel = await ctx.channel.clone()
            await ctx.channel.delete()
            await new_channel.send("Channel nuked.\nhttps://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
        else:
            new_channel = await channel.clone()
            await channel.delete()
            await ctx.channel.send(f"Nuked {new_channel.mention} <:tick:781706203117912085>")
            await new_channel.send("Channel nuked.\nhttps://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")

    @commands.command(aliases=['kick'])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick_user(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
        if member is ctx.author:
            return await ctx.send("You cannot kick yourself.")
        if member == ctx.guild.owner:
            return await ctx.send("You cannot kick the server owner.")
        admin = ("administrator" in member.guild_permissions)
        if admin:
            return await ctx.send("You cannot kick a server admin.")
        if member.top_role > ctx.author.top_role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        try:
            try:
                #e = await member.send(embed=kickdm)
                f = await member.send(f"You have been kicked from **{ctx.guild.name}**.\nReason: `{reason}`\nModerator: **{ctx.author}**")
                thing = 'User notified with a DM'
            except:
                thing = 'User\'s DMs are closed.'
            await member.kick(reason=reason)
            #await ctx.channel.send(embed=kickmessage)
            await ctx.send(f"I have kicked **{member}**. ({thing})\nReason: `{reason}`")
        except Exception as e:
            #await ctx.send(embed=nokickperms)
            await ctx.send("```{}```".format(e))
            await f.delete()

    @kick_user.error
    async def kick_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
        admin = ("administrator" in member.guild_permissions)
        if admin:
            return await ctx.send("You cannot ban a server admin.")
        elif member is ctx.author:
            return await ctx.send("You cannot ban yourself.")
        elif member is ctx.guild.owner:
            return await ctx.send("You cannot ban the server owner.")
        elif member.top_role > ctx.author.top_role:
            return await ctx.send("You're not high enough in the hierarchy to do that.")
        try:
            try:
                e = await member.send(f"You have been banned from **{ctx.guild.name}**.\nReason: `{reason}`\nModerator: **{ctx.author}**")
                thing = 'User notified with a DM'
            except:
                thing = 'User\'s DMs are closed.'
            await member.ban(reason=reason)
            #await ctx.channel.send(embed=banmessage)
            await ctx.send(f"I have banned **{ctx.author}**. ({thing})\nReason: `{reason}`")
        except:
            #await ctx.send(embed=nobanperms)
            await ctx.send("```{}```".format(e))
            await e.delete()

    @ban.error
    async def ban_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        try:
            if '#' in str(member):
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        try:
                            await ctx.guild.unban(user)
                            await ctx.send(f"{ctx.author.mention}, I have unbanned **{user}**.")
                            return
                        except Exception as e:
                            await ctx.send(f"```{e}```")
            else:
                userid = int(member)
                user = await self.bot.fetch_user(userid)
                try:
                    await ctx.guild.unban(user)
                    await ctx.send(f"{ctx.author.mention}, I have unbanned **{user}**.")
                    return
                except Exception as e:
                    await ctx.send(f"```{e}```")
        except Exception as e:
            await ctx.send("```{}```".format(e))

    @unban.error
    async def unb_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.\nExample Usage: `{prefix(ctx.message)}unban mutefx#0001`")

    @commands.command(pass_context = True)
    @commands.guild_only()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, member: discord.Member, *, how_long: int = None):
        try:
            if member is ctx.author:
                return await ctx.send("You cannot mute yourself.")
            elif member is ctx.guild.owner:
                return await ctx.send("You cannot mute the server owner.")
            elif "administrator" in member.guild_permissions:
                return await ctx.send("You cannot mute a server admin.")
            elif member.top_role > ctx.author.top_role:
                return await ctx.send("You're not high enough in the hierarchy to do that.")
            elif how_long == None:
                how_long = 999999
                dur = 'Indefinitely'
            else:
                # def convert(time):
                #     pos = ['s', 'm', 'h', 'd']
                #     time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
                #     unit = time[-1]
                #     if unit not in pos:
                #         return -1
                #     try:
                #         val = int(time[:-1])
                #     except:
                #         return -2
                #     return val * time_dict[unit]
                # _thing = convert(how_long) / 3600
                # _hrs = int(_thing)
                # _mins = (_thing*60) % 60
                # _sec = (_thing*3600) % 60
                # dur = f"{_hrs} hours {_mins} minutes {_sec} seconds"
                if int(how_long) < 1:
                    await ctx.send("Cannot be lower than 1 minute.")
                elif int(how_long) > 1079:
                    await ctx.send("Cannot be longer than 7 days. (10080 minutes)")
                else:
                    try:
                        _hrs = int(how_long)
                        dur = f"{_hrs} minutes"
                    except:
                        await ctx.send(f"Invalid Usage: `{how_long}` must be a number.\nUsage: `{prefix(ctx.message)}mute [@user] <minutes>`")
            try:
                try:
                    with open('./configs/serverconfs.json', "r") as pp:
                        mconf = json.load(pp)
                    mtrole = ctx.guild.get_role(mconf[f"{ctx.guild.id}"]["muterole"])
                    await member.add_roles(mtrole)
                    await ctx.send(f"I have muted **{member.name}**.\nDuration: {dur}")
                    await asyncio.sleep(how_long)
                    await member.remove_roles(mtrole)
                except:
                    await ctx.send(f"I can't find the `muterole`. You can either `{prefix(ctx.message)}muterole <@role>` or use the `{prefix(ctx.message)}setup` command.")
            except Exception as _re:
                await ctx.send(f"```{_re}```")
        except Exception as _e:
            await ctx.send("```{}```".format(_e))
            print(_e)

    @mute.error
    async def mte_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.\nUsage: `{prefix(ctx.message)}mute [user] <minutes>`")

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member: discord.Member):
        with open('./configs/serverconfs.json', "r") as pp:
            mconf = json.load(pp)
        mtrole = ctx.guild.get_role(mconf[f"{ctx.guild.id}"]["muterole"])
        try:
            try:
                await member.remove_roles(mtrole)
            except:
                return await ctx.send(f"User is not muted.")
            await ctx.send(f"I have unmuted **{member.name}**.")
        except Exception as e:
            await ctx.send(f"```{e}```")

    @unmute.error
    async def unm_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.")
    
    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def warn(self, ctx, user: discord.Member = None, *, reason=None):
        if reason is None:
            await ctx.send(f"You must provide a reason for the warn.\nUsage: `{prefix(ctx.message)}warn [user] [reason]`")
        elif user is None:
            await ctx.send(f"You must provide the user to warn.\nUsage: `{prefix(ctx.message)}warn [user] [reason]`")
        else:
            if user is ctx.author:
                return await ctx.send("You cannot warn yourself.")
            elif user is ctx.guild.owner:
                return await ctx.send("You cannot warn the server owner.")
            elif "administrator" in user.guild_permissions:
                return await ctx.send("You cannot warn a server admin.")
            elif user.top_role > ctx.author.top_role:
                return await ctx.send("You're not high enough in the hierarchy to do that.")
            with open("./configs/warns.json", "r") as f:
                pp = json.load(f)
            try:
                guild = pp[str(ctx.guild.id)]
                warns = list(guild[f"{user.id}"])
            except KeyError:
                with open("./configs/warns.json", "w") as ra:
                    pp[str(ctx.guild.id)] = {str(user.id): []}
                    json.dump(pp, ra, indent=4)
                    guild = pp[str(ctx.guild.id)]
                    warns = list(guild[f"{user.id}"])
            warns.append("{}".format(reason))
            pp[str(ctx.guild.id)][f"{user.id}"] = warns
            with open("./configs/warns.json", "w") as ra:
                try:
                    json.dump(pp, ra, indent=4)
                except KeyError:
                    pp[str(ctx.guild.id)] = {str(user.id): [str(reason)]}
                    json.dump(pp, ra, indent=4)
            try:
                await user.send(f"You have been warned in **{ctx.guild.name}** for `{reason}`.")
                s = "User has been notified with a DM"
            except:
                s = "User has not been DMed"
            await ctx.send(f"<:tickYes:787334378630938672> **{user}** has been warned. ({s})")

    @warn.error
    async def warn_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.")

    @commands.command(pass_context=True)
    @commands.guild_only()
    async def warns(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        with open("./configs/warns.json", "r") as f:
            pp = json.load(f)
        try:
            guild = pp[str(ctx.guild.id)]
            wew = list(guild[str(user.id)])
        except KeyError:
            with open("./configs/warns.json", "w") as ra:
                pp[str(ctx.guild.id)] = {str(user.id): []}
                json.dump(pp, ra, indent=4)
        guild = pp[str(ctx.guild.id)]
        warns = []
        u = 0
        for w in guild[str(user.id)]:
            u = u + 1
            warns.append(f"{str(u)}. {w}")
        if warns is []:
            d = "No Warns"
        else:
            d = '\n'.join(warns)
        if d is "":
            d = "No Warns"
        e = Embed(
            title=f"Warns for {user}",
            description="{}".format(d),
            color=emcolor)
        footerd(e)
        await ctx.send(embed=e)

    @warns.error
    async def warns_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.")
    
    @commands.command(aliases=["clearwarns"])
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def clearwarn(self, ctx, *, user: discord.Member = None):
        if user is None:
            await ctx.send(f"You must provide the user to clear their warns.\nUsage: `{prefix(ctx.message)}clearwarns [user]`")
        else:
            if user is ctx.guild.owner:
                return await ctx.send("The server owner cannot be warned or clear their warns..")
            if "administrator" in user.guild_permissions:
                return await ctx.send("You cannot clear an admin's warns.")
            if user.top_role > ctx.author.top_role:
                return await ctx.send("You're not high enough in the hierarchy to do that.")
            with open("./configs/warns.json", "r") as d:
                conf = json.load(d)
            warns = list(conf[f"{str(ctx.guild.id)}"][str(user.id)])
            conf[str(ctx.guild.id)][str(user.id)] = []
            with open("./configs/warns.json", "w") as f:
                try:
                    json.dump(conf, f, indent=4)
                    try:
                        await user.send(f"Your warnings on **{ctx.guild.name}** was removed.")
                        notif = "User notified with a DM"
                    except:
                        notif = "User was not notified with a DM"
                    await ctx.send(f"Cleared warnings for **{user}**. ({notif})")
                except KeyError:
                    return await ctx.send("User does not have any warns.")
            
    @clearwarn.error
    async def delwarn_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"User not found.")

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_guild=True)
    async def setup(self, ctx):
        prgrs = 0.0
        def thingy(rol):            
            with open('./configs/serverconfs.json', "r") as p:
                thing = json.load(p)
            thing[str(ctx.guild.id)]["muterole"] = int(rol.id)
            with open('./configs/serverconfs.json', "w") as f:
                json.dump(thing, f, indent=2)
        a = await ctx.send(f"Setting up things... (Progress: `{prgrs}%`)")
        await ctx.send(f"Finding `muterole`...")
        try:
            global muterole
            muterole = discord.utils.get(ctx.guild.roles, name='Muted')
            await ctx.send(f"Muterole found! (**{muterole.name}**)")
        except:
            try:
                muterole = discord.utils.get(ctx.guild.roles, name='muted')
                await ctx.send(f"Muterole found! (**{muterole.name}**)")
            except:
                await ctx.send("Muterole not found. Creating new role...")
                try:
                    role = await ctx.guild.create_role(name="Muted")
                    await asyncio.sleep(0.1)
                    prgrs = 23.4
                    await a.edit(content=f"Setting up things... (Progress: `{prgrs}%`)")
                    await ctx.send(f"Muterole created! (**{role.name}**)")
                    await asyncio.sleep(0.16)
                    await ctx.send(f"Setting Permissions for **{role.name}**...")
                    await asyncio.sleep(0.16)
                    try:
                        for channel in ctx.guild.channels:
                            await channel.set_permissions(role, send_messages=False)
                            await asyncio.sleep(0.16)
                        prgrs = 78.6
                        await a.edit(content=f"Setting up things... (Progress: `{prgrs}%`)")
                        await ctx.send(f"Permissions created for **{len(ctx.guild.channels)}** channels.")
                    except Exception as e:
                        await ctx.send(f"```{e}```")
                    await ctx.send("Assigning the created muterole as the muterole in the database...")
                    thingy(role)
                    await asyncio.sleep(0.2)
                    prgrs = 100.0
                    await a.edit(content=f"Set up things. (Progress: `{prgrs}%`)")
                    return await ctx.send("Saved! Setup finished. <:tick:769432064557842442>")
                except Exception as e:
                    await ctx.send(f"```{e}```")
        await asyncio.sleep(0.16)
        await ctx.send(f"Setting Permissions for **{muterole.name}**...")
        await asyncio.sleep(0.16)
        try:
            for channel in ctx.guild.channels:
                await channel.set_permissions(muterole, send_messages=False)
                await asyncio.sleep(0.16)
            prgrs = 78.6
            await a.edit(content=f"Setting up things... (Progress: `{prgrs}%`)")
            await ctx.send(f"Permissions created for **{len(ctx.guild.channels)}** channels.")
        except Exception as e:
            await ctx.send(f"```{e}```")
        await ctx.send("Assigning the created muterole as the muterole in the database...")
        thingy(muterole)
        await asyncio.sleep(0.2)
        prgrs = 100.0
        await a.edit(content=f"Set up things. (Progress: `{prgrs}%`)")
        await ctx.send("Saved! Setup finished. <:tick:769432064557842442>")
        #else:
        #    await ctx.send("Command canceled. <:x_:781706203544813588>")


def setup(bot):
    bot.add_cog(Moderation(bot))
