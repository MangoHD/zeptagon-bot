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
            emb=discord.Embed(description=f'Successfully changed slowmode to `{seconds}` seconds.', color=emcolor)
            emb.set_footer(text=footer)
            emb.add_field(name="_ _", value=fieldfooter)
            emb.set_author(name='Success', icon_url=ctx.author.avatar_url)
            await ctx.send(f'Successfully changed slowmode to `{seconds}` seconds.')
        except Exception as e:
            emb=discord.Embed(title='Error', description='Bot has missing permissions to do this.', color=emcolor)
            emb.set_footer(text=footer)
            emb.add_field(name="_ _", value=fieldfooter)
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
                e = await member.send(embed=kickdm)
            except:
                pass
            await member.kick(reason=reason)
            await ctx.channel.send(embed=kickmessage)
        except:
            await ctx.send(embed=nokickperms)
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
                e = await member.send(embed=bandm)
            except:
                pass
            await member.ban(reason=reason)
            await ctx.channel.send(embed=banmessage)
        except:
            await ctx.send(embed=nobanperms)
            await e.delete()

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_guild_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{ctx.author.mention}, I have unbanned **{user}**.")
                return

    #MUTE COMMAND
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @commands.bot_has_guild_permissions(administrator=True)
    async def mute(self, ctx,member : discord.Member,*,reason = None):
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
            role = discord.utils.get(self, ctx.guild.roles, name=f'{mutessd}')
            await member.add_roles(role)
            await ctx.channel.send(embed=em)
            try:
                await member.send(embed=ems)
            except:
                await ctx.send(f"**{member.name}#{member.discriminator}** has their **DM**s closed.")
        except:
            await ctx.send(embed=emd)
    #UNMUTE COMMANDS
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @commands.bot_has_guild_permissions(administrator=True)
    async def unmute(self, c,member : discord.Member,*,reason= None):
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

def setup(bot):
    bot.add_cog(Moderation(bot))
