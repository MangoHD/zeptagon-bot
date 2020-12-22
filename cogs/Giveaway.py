import discord
import os
import asyncio
import datetime
import random
from discord.ext import commands
from discord import Embed, Color
from bot_things import prefix, motd, emcolor, ercolor, footerd, footera, getprefix, get_prefix, timei

class GiveawayCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gcreate'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def gstart(self, ctx):
        answers = []
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        await ctx.channel.send(embed=discord.Embed(
            description=f'Let\'s start!\nPlease mention where you want to giveaway to be. Example: {ctx.channel.mention}',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=Color.red()))
        else:
            answers.append(msg.content)
        try:
            yes = False
            c_id = int(answers[0][2:-1])
            for channel in ctx.guild.text_channels:
                if channel.id == c_id:
                    yes = True
                else:
                    pass
            if yes == False:
                return await ctx.channel.send(embed=Embed(
                    description=f'<:tickNo:787334378639458344> You didn\'t mention the channel properly. Example: {ctx.channel.mention}.',
                    color=Color.red()))
        except:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> You didn\'t mention the channel properly. Example: {ctx.channel.mention}.',
                color=Color.red()))
        await ctx.channel.send(embed=discord.Embed(
            description=f'Ok, set channel as <#{c_id}>.\nPlease enter the time for the giveaway before it rolls. (for example: `15s 2m 3h 4d`)',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=Color.red()))
        else:
            answers.append(msg.content)
        def convert(time):
            pos = ['s', 'm', 'h', 'd']
            time_dict = {'s': 1, 'm': 60, 'h': 3600, 'd': 3600 * 24}
            unit = time[-1]
            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
            return val * time_dict[unit]
        def __convert__(time):
            jsd = time.split(' ')
            isd = []
            for i in jsd:
                pos = ['s', 'm', 'h', 'd']
                tdic = {'s': 'seconds', 'm': 'minutes', 'h': 'hours', 'd': 'days'}
                unit = i[-1]
                if unit not in pos:
                    return -1
                try:
                    val = int(i[:-1])
                except:
                    return -2
                isd.append(f"{str(val)} {tdic[unit]}")
            return ' '.join(isd)
        time = convert(answers[1])
        if time == -1:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> You didn\'t enter the time properly. Example: `15s 2m 3h 4d`.',
                color=Color.red()))
        elif time == -2:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> You didn\'t enter the time properly. Please enter an integer (numbers) next time.',
                color=Color.red()))
        await ctx.channel.send(embed=discord.Embed(
            description=f'Ok, time has been set to **{__convert__(answers[1])}**\nPlease enter the prize for the giveaway.',
            color=Color.red()))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=Color.red()))
        else:
            answers.append(msg.content)
        def check2(message):
            try:
                int(message.content)
                return True
            except ValueError:
                return False
        await ctx.channel.send(embed=discord.Embed(
            description=f'Ok, the prize is set to **{answers[2]}**.\nPlease how much winners needed for this giveaway. (max: 25)',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=Color.red()))
        else:
            answers.append(msg.content)
        try:
            wnrs = int(answers[3])
        except:
            return await ctx.channel.send(embed=Embed(
                description=f'<:tickNo:787334378639458344> Invalid answer. The **amount of winners** must be an integer (number).',
                color=Color.red()))
        channel = self.bot.get_channel(c_id)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        prize = answers[2]
        if int(answers[3]) < 25:
            win_amount = int(answers[3])
        else:
            win_amount = 25
        msg = await channel.send("<a:dicegif:786111161036701736>")
        embed = discord.Embed(
            description=f"🏅 Winners: {str(wnrs)}\n⌛ Time Remaining: {answers[1]}\n🔰 Host: {ctx.author.mention}\nReact to 🎉 to enter the giveaway!\n\nIf the giveaway does not end automatically,\nuse `{prefix(ctx.message)}gend {msg.id}`",
            colour=discord.Color.blue(),
            timestamp=end)
        embed.set_footer(text="Ends at", icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        embed.set_author(name=str(prize), icon_url="https://cdn.discordapp.com/attachments/743425064921464833/767981650070994984/86c9a4dde5bb348b53f2fb7ff099e9d5-square-wrapped-gift-box-by-vexels.png")
        footerd(embed)
        await msg.edit(content="<:present:767981864132018176> **GIVEAWAY** <:present:767981864132018176>", embed=embed)
        await msg.add_reaction("🎉")
        await ctx.send(ctx.author.mention, embed=discord.Embed(description=f"<:tick:769432064557842442> Successfully started giveaway in {channel.mention}", color=discord.Color.green()))
        await asyncio.sleep(time)
        msg2 = await channel.fetch_message(msg.id)
        users = await msg2.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winners = []
        for i in range(win_amount):
            i = i
            winners.append(random.choice(users).mention)
        embed2 = discord.Embed(
            description=f"🔰 Host: {ctx.author.mention}\n🎟 Valid Entries: {len(users)}\n🏅 Winner(s): \n"+'\n'.join(winners)+"\n",
            colour=0x777777,
            timestamp=timei.now)
        footerd(embed2)
        embed2.set_footer(text="Ended at", icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        if msg.content != "<:CH_present:767981864132018176> **GIVEAWAY ENDED** <:CH_present:767981864132018176>":
            await channel.send(f"🎊 **Congratulations** {', '.join(winners)}! You have won **{prize}**!")
            await msg.edit(content="<:present:767981864132018176> **GIVEAWAY ENDED** <:present:767981864132018176>", embed=embed2)
        else:
            pass

    @commands.command(aliases=['greroll'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def reroll_giveaway(self, ctx, id_: int = None):
        if id_ == None:
            return await ctx.send(f"You need to provide a message id to reroll.\nUsage: `{prefix(ctx.message)}greroll [msg-id]`")
        else:
            try:
                for channel in ctx.guild.text_channels:
                    try:
                        msg2 = await channel.fetch_message(int(id_))
                    except:
                        pass
            except:
                await ctx.send(embed=discord.Embed(description = "<:tickNo:787334378639458344> Error: ID was entered incorrectly.", color=discord.Color.red()))
            #answers = []
            #def check2(message):
            #    try:
            #        int(message.content)
            #        return True
            #    except ValueError:
            #        return False
            #await ctx.send(
            #    embed=discord.Embed(
            #        description=f'Are you sure to reroll [THIS](https://discordapp.com/channels/{ctx.guild.id}/{msg2.channel.id}/{id_}) giveaway? (`yes` or `no`)',
            #        color=emcolor
            #    ).set_author(
            #        name='Reroll Giveaway'
            #    )
            #)
            #try:
            #    msg = await self.bot.wait_for('message', timeout=45.0, check=check2)
            #except asyncio.TimeoutError:
            #    await ctx.channel.send(embed=discord.Embed(
            #        title='Error',
            #        description=f'You did not answered fast enough. Try again by typing `{prefix}greroll`',
            #        color=emcolor))
            #    return
            #else:
            #    answers.append(msg.content)
            #if answers[0] == 'yes':
            users = await msg2.reactions[0].users().flatten()
            users.pop(users.index(self.bot.user))
            winner = random.choice(users)
            await msg2.channel.send(f"🎊 **Congratulations** {winner.mention}! You are the new winner!")
            emb = discord.Embed(
                description=f"<:tick:769432064557842442> Successfully re-rolled giveaway in {msg2.channel.mention}",
                color=discord.Color.green()
            )
            await ctx.send(embed=emb)
                    
            #elif answers[0] == 'no':
            #    await ctx.send( embed=discord.Embed(description='<:tickNo:787334378639458344> Command Cancelled.', color=discord.Color.red()))
            #    return
            #else:
            #    await ctx.send(embed=discord.Embed(description='<:tickNo:787334378639458344> Invalid answer. Command Cancelled.', color=discord.Color.red()))

    @reroll_giveaway.error
    async def greroll_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Invalid message ID.\nUsage: `{prefix(ctx.message)}greroll [msg-id]`")

    @commands.command(aliases=['gend'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def end_giveaway(self, ctx, id_: int = None):
        if id_ == None:
            return await ctx.send(f"You need to provide a message id to end.\nUsage: `{prefix(ctx.message)}gend [msg-id]`")
        else:
            try:
                for channel in ctx.guild.text_channels:
                    try:
                        msg2 = await channel.fetch_message(int(id_))
                    except:
                        pass
            except:
                await ctx.send(embed=discord.Embed(description = "<:tickNo:787334378639458344> Error: ID was entered incorrectly.", color=discord.Color.red()))
            users = await msg2.reactions[0].users().flatten()
            users.pop(users.index(self.bot.user))
            winner = random.choice(users)
            if msg2.content == "<:CH_present:767981864132018176> **GIVEAWAY ENDED** <:CH_present:767981864132018176>":
                await ctx.send(embed=discord.Embed(description = "<:tickNo:787334378639458344> Error: The giveaway was already ended.", color=discord.Color.red()))
            else:
                await msg2.channel.send(f"🎊 **Congratulations** {winner.mention}! You have won the giveaway!")
                users = await msg2.reactions[0].users().flatten()
                users.pop(users.index(self.bot.user))
                emb = discord.Embed(
                    description=f"<:tick:769432064557842442> Successfully ended giveaway in {msg2.channel.mention}",
                    color=discord.Color.green())
                embed2 = discord.Embed(
                    description=f"🔰 Host: {ctx.author.mention}\n🎟 Valid Entries: {len(users)}\n🏅 Winner: \n"+winner.mention+"\n",
                    colour=0x777777,
                    timestamp=timei.now)
                footerd(embed2)
                embed2.set_footer(text="Ended at", icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
                await msg2.edit(content="<:CH_present:767981864132018176> **GIVEAWAY ENDED** <:CH_present:767981864132018176>", embed=embed2)
                await ctx.send(embed=emb)

    @end_giveaway.error
    async def gend_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"Invalid message ID.\nUsage: `{prefix(ctx.message)}gend [msg-id]`")

def setup(bot):
    bot.add_cog(GiveawayCommands(bot))
