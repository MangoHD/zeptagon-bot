import discord
import os
import asyncio
from discord.ext import commands
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

    @commands.command(pass_context=True, aliases=['addrole'])
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.add_roles(role)
            await ctx.send(f"{ctx.author.mention}, given **{user.display_name}** the **{role.name}** role.")
        except Exception as e:
            await ctx.send(f'```{e}```')

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
    async def nuke(self, ctx, channel: discord.TextChannel = None):
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
        kickmessage = discord.Embed(
            title="Kicked",
            description=f"**{ctx.author.mention}** has kicked the user **{member}**.",
            colour=emcolor
        )

        kickmessage.add_field(name='Reason:', value=reason, inline=False)
        kickmessage.set_thumbnail(
            url=ctx.author.avatar_url)
        footerd(kickmessage)

        kickdm = discord.Embed(
            title='Kicked',
            description=f"You have been kickned from **{ctx.author.guild}** by **{ctx.author.name}#"
                        f"{ctx.author.discriminator}**.",
            colour=emcolor
        )

        kickdm.add_field(name='Reason:', value=reason, inline=False)
        kickdm.set_thumbnail(
            url=ctx.author.avatar_url)
        footerd(kickdm)

        nokickperms = discord.Embed(
            title="Invalid!",
            description='Error: `No permissions to kick user. Try putting my role above the user\'s role`\n\n'
                        '`Unable to kick user.`',
            colour=emcolor
        )

        nokickperms.set_thumbnail(
            url=ctx.author.avatar_url)
        footerd(nokickperms)

        try:
            try:
                #e = await member.send(embed=kickdm)
                f = await member.send(f"You have been kicked from **{ctx.guild.name}**.\n\nResponsible Moderator: **{ctx.author}**")
            except:
                pass
            await member.kick(reason=reason)
            #await ctx.channel.send(embed=kickmessage)
            await ctx.send(f"I have kicked **{member}**.\nReason: **{reason}**\n\nResponsible Moderator: **{ctx.author}**")
        except Exception as e:
            #await ctx.send(embed=nokickperms)
            await ctx.send("```{}```".format(e))
            await f.delete()

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='No Reason Provided.'):
        banmessage = discord.Embed(
            title="Banned",
            description=f"**{ctx.author.name}#{ctx.author.discriminator}** has banned the user **{member.name}**.",
            colour=emcolor
        )

        banmessage.add_field(name='Reason:', value=reason, inline=False)
        banmessage.set_thumbnail(
            url=ctx.author.avatar_url)
        footerd(banmessage)

        bandm = discord.Embed(
            title='Banned',
            description=f"You have been banned from **{ctx.author.guild}** by **{ctx.author.name}#"
                        f"{ctx.author.discriminator}**.",
            colour=emcolor
        )

        bandm.add_field(name='Reason:', value=reason, inline=False)
        bandm.set_thumbnail(
            url=ctx.author.avatar_url)
        footerd(bandm)

        nobanperms = discord.Embed(
            title="Invalid!",
            description='Error: `No permissions to ban user. Try putting my role above the user\'s role`\n\n'
                        '`Unable to ban user.`',
            colour=emcolor
        )

        nobanperms.set_thumbnail(url=ctx.author.avatar_url)
        footerd(nobanperms)
        try:
            try:
                #e = await member.send(embed=bandm)
                e = await member.send(f"You have been banned from **{ctx.guild.name}**.\n\nResponsible Moderator: **{ctx.author}**")
            except:
                pass
            await member.ban(reason=reason)
            #await ctx.channel.send(embed=banmessage)
            await ctx.send(f"I have banned **{ctx.author}**.\nReason: **{reason}**\n\nResponsible Moderator: **{ctx.author}**")
        except:
            #await ctx.send(embed=nobanperms)
            await ctx.send("```{}```".format(e))
            await e.delete()

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
                user = await discord.utils.get(discord.Member, id=userid)
                try:
                    await ctx.guild.unban(user)
                    await ctx.send(f"{ctx.author.mention}, I have unbanned **{user}**.\n\nResponsible Moderator: **{ctx.author}**")
                    return
                except Exception as e:
                    await ctx.send(f"```{e}```")
        except Exception as e:
            await ctx.send("```{}```".format(e))

    @commands.command(pass_context = True)
    @commands.guild_only()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, member: discord.Member):
        try:
            try:
                await member.add_roles(discord.utils.get(member.guild.roles, name='Muted'))
            except:
                try:
                    await member.add_roles(discord.utils.get(member.guild.roles, name='muted'))
                except:
                    await ctx.send(f"I can't find the `muterole`. You can either make a role named `Muted` or use the `{prefix}setup` command.")
                    return
            await ctx.send(f"I have muted **{member.name}**.\nResponsible Moderator: **{ctx.author}**")
        except Exception as e:
            await ctx.send(f"```{e}```")
            #await ctx.send(f"I can't find the `muterole`. You can either make a role named `Muted` or use the `{prefix}setup` command.")

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member: discord.Member):
        try:
            try:
                await member.remove_roles(discord.utils.get(member.guild.roles, name='Muted'))
            except:
                try:
                    await member.remove_roles(discord.utils.get(member.guild.roles, name='muted'))
                except:
                    await ctx.send(f"User is not muted.")
                    return
            await ctx.send(f"I have unmuted **{member.name}**.\nResponsible Moderator: **{ctx.author}**")
        except Exception as e:
            await ctx.send(f"```{e}```")

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_guild_permissions(manage_guild=True)
    async def setup(self, ctx):
        prgrs = 0.0

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
                    await ctx.send("Assigning the created muterole as the main muterole...")
                    await asyncio.sleep(0.2)
                    prgrs = 100.0
                    await a.edit(content=f"Set up things. (Progress: `{prgrs}%`)")
                    await ctx.send("Saved! Setup finished. <:tick:769432064557842442>")
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
        await ctx.send("Assigning the created muterole as the main muterole...")
        await asyncio.sleep(0.2)
        prgrs = 100.0
        await a.edit(content=f"Set up things. (Progress: `{prgrs}%`)")
        await ctx.send("Saved! Setup finished. <:tick:769432064557842442>")
        #else:
        #    await ctx.send("Command canceled. <:x_:781706203544813588>")


def setup(bot):
    bot.add_cog(Moderation(bot))
