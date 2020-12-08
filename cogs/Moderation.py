import discord
import os
import asyncio
from discord.ext import commands

getprefix = [os.environ['BOT_PREFIX'], os.environ['BOT_PREFIX2']]
prefix = os.environ['BOT_PREFIX']
motd = os.environ['BOT_MOTD']
footer = os.environ['BOT_FOOTER']
emcolor = 0x777777
ercolor = 0xff0000
fieldfooter = "Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=755010248929968158&permissions=8&scope=bot)"

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

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles = True)
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        try:
            await user.add_roles(role)
            await ctx.send(f"{ctx.author.mention}, given **{user.display_name}** the **{role.name}** role.")
        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount: int):
        try:
            if amount < 500:
                await ctx.channel.purge(limit=amount)
                await ctx.send("Deleted {} messages.".format(amount))
            else:
                await ctx.send("Unable to delete messages. Maximum is **500** messages.")
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
        kickmessage.add_field(name="_ _", value=fieldfooter)
        kickmessage.set_footer(text=footer)

        kickdm = discord.Embed(
            title='Kicked',
            description=f"You have been kickned from **{ctx.author.guild}** by **{ctx.author.name}#"
                        f"{ctx.author.discriminator}**.",
            colour=emcolor
        )

        kickdm.add_field(name='Reason:', value=reason, inline=False)
        kickdm.set_thumbnail(
            url=ctx.author.avatar_url)
        kickdm.add_field(name="_ _", value=fieldfooter)
        kickdm.set_footer(text=footer)

        nokickperms = discord.Embed(
            title="Invalid!",
            description='Error: `No permissions to kick user. Try putting my role above the user\'s role`\n\n'
                        '`Unable to kick user.`',
            colour=emcolor
        )

        nokickperms.set_thumbnail(
            url=ctx.author.avatar_url)
        nokickperms.add_field(name="_ _", value=fieldfooter)
        nokickperms.set_footer(text=footer)

        try:
            try:
                #e = await member.send(embed=kickdm)
                e = await member.send(f"You have been kicked from **{ctx.guild.name}**.\n\nResponsible Moderator: **{ctx.author}**")
            except:
                pass
            await member.kick(reason=reason)
            #await ctx.channel.send(embed=kickmessage)
            await ctx.send(f"I have kicked **{ctx.author}**.\n\nResponsible Moderator: **{ctx.author}**")
        except Exception as e:
            #await ctx.send(embed=nokickperms)
            await ctx.send("```{}```".format(e))
            await e.delete()

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
        banmessage.add_field(name="_ _", value=fieldfooter)
        banmessage.set_footer(text=footer)

        bandm = discord.Embed(
            title='Banned',
            description=f"You have been banned from **{ctx.author.guild}** by **{ctx.author.name}#"
                        f"{ctx.author.discriminator}**.",
            colour=emcolor
        )

        bandm.add_field(name='Reason:', value=reason, inline=False)
        bandm.set_thumbnail(
            url=ctx.author.avatar_url)
        bandm.add_field(name="_ _", value=fieldfooter)
        bandm.set_footer(text=footer)

        nobanperms = discord.Embed(
            title="Invalid!",
            description='Error: `No permissions to ban user. Try putting my role above the user\'s role`\n\n'
                        '`Unable to ban user.`',
            colour=emcolor
        )

        nobanperms.set_thumbnail(url=ctx.author.avatar_url)
        nobanperms.add_field(name="_ _", value=fieldfooter)
        nobanperms.set_footer(text=footer)
        try:
            try:
                #e = await member.send(embed=bandm)
                e = await member.send(f"You have been banned from **{ctx.guild.name}**.\n\nResponsible Moderator: **{ctx.author}**")
            except:
                pass
            await member.ban(reason=reason)
            #await ctx.channel.send(embed=banmessage)
            await ctx.send(f"I have banned **{ctx.author}**.\n\nResponsible Moderator: **{ctx.author}**")
        except:
            #await ctx.send(embed=nobanperms)
            await ctx.send("```{}```".format(e))
            await e.delete()

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        try:
            userid = int(member)
            user = await discord.utils.get(discord.Member, id=userid)
            try:
                await ctx.guild.unban(user)
                await ctx.send(f"{ctx.author.mention}, I have unbanned **{user}**.\n\nResponsible Moderator: **{ctx.author}**")
                return
            except Exception as e:
                await ctx.send(f"```{e}```")
        except:
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


    @commands.command()
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, member : discord.Member, *, reason = "No Reason Provided"):

        for role in ctx.guild.roles:
            if 'muted' or 'Muted' in role.name:
                global muterole
                muterole = role

        try:
            await member.add_roles(muterole)
            await ctx.channel.send(f"I have muted **{member}**.\n\nResponsible Moderator: **{ctx.author}**")
        except Exception as e:
            await ctx.send(f"```{e}```")

    @commands.command()
    @commands.has_permissions(mute_members=True)
    async def unmute(self, c,member : discord.Member,*,reason= None):

        try:
            await member.remove_roles(muterole)
            await ctx.channel.send(f"I have unmuted **{member}**.\n\nResponsible Moderator: **{ctx.author}**")
        except Exception as e:
            await ctx.send(f"```{e}```")

def setup(bot):
    bot.add_cog(Moderation(bot))
