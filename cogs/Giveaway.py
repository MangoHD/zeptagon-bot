import discord
import os
import asyncio
import datetime
import random
from discord.ext import commands
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

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
            description=f'Please mention where you want to giveaway to be. Example: {ctx.channel.mention}',
            color=emcolor
        ))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.message.delete()
            #await a1.delete()
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=emcolor
            ))
            return
        else:
            answers.append(msg.content)
        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.channel.send(
                f"**Error:** You didn't mention the channel properly. Example: {ctx.channel.mention}. You can  try again by typing `{prefix}gstart`")
            return
        await ctx.channel.send(embed=discord.Embed(
            description=f'Please enter the time for the giveaway before it rolls. (for example: `15s 2m 3h 4d`)',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=emcolor))
            return
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
        time = convert(answers[1])
        if time == -1:
            await ctx.channel.send(
                f"**Error:** You didn't enter the time properly. Example: `15s 2m 3h 4m`. You can  try again by typing `{prefix}giveaway`")
            return
        elif time == -2:
            await ctx.channel.send(
                f"**Error:** You didn't enter the time properly. Please enter an integer (numbers) next time. You can  try again by typing `{prefix}giveaway`")
            return
        await ctx.channel.send(embed=discord.Embed(
            description=f'Please enter the prize for the giveaway.',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=emcolor))
            return
        else:
            answers.append(msg.content)
        def check2(message):
            try:
                int(message.content)
                return True
            except ValueError:
                return False
        await ctx.channel.send(embed=discord.Embed(
            description=f'Please how much winners needed for this giveaway. (max: 25)',
            color=emcolor))
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check2)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=discord.Embed(
                title='Error',
                description=f'You did not answered fast enough. Try again by typing `{prefix}gstart`',
                color=emcolor))
            return
        else:
            answers.append(msg.content)
        
        
        channel = self.bot.get_channel(c_id)
        
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        prize = answers[2]
        if int(answers[3]) < 25:
            win_amount = int(answers[3])
        else:
            win_amount = 25
        embed = discord.Embed(
            description=f"🏅 Winners: {answers[3]}\n⌛ Time Remaining: {answers[1]}\n🔰 Host: {ctx.author.mention}\nReact to 🎉 to enter the giveaway!",
            colour=discord.Color.blue(),
            timestamp=end)
        embed.set_footer(text="Ends at", icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        embed.add_field(name="_ _", value='Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)')
        msg = await channel.send("<:CH_present:767981864132018176> **GIVEAWAY** <:CH_present:767981864132018176>", embed=embed)
        await msg.add_reaction("🎉")
        gwmsg = await ctx.send(ctx.author.mention, embed=discord.Embed(description=f"<:tick:769432064557842442> Successfully started giveaway in {channel.mention}", color=discord.Color.green()))
        await asyncio.sleep(time)
        msg2 = await channel.fetch_message(msg.id)
        users = await msg2.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winners = []
        for i in range(win_amount):
            i = i
            winners.append(random.choice(users).mention)
        embed2 = discord.Embed(
            description=f"🔰 Host: {ctx.author.mention}\n🎟 Valid Entries: {len(users)}\n🏅 Winners: \n"+'\n'.join(winners)+"\n",
            colour=emcolor,
            timestamp=end)
        embed2.set_author(name=prize, icon_url="https://cdn.discordapp.com/attachments/743425064921464833/767981650070994984/86c9a4dde5bb348b53f2fb7ff099e9d5-square-wrapped-gift-box-by-vexels.png")
        embed2.add_field(name="_ _", value='Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)')
        embed2.set_footer(text="Ended at", icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        if gwmsg.content != "<:CH_present:767981864132018176> **GIVEAWAY ENDED** <:CH_present:767981864132018176>":
            await channel.send(f"🎊 **Congratulations** {', '.join(winners)}! You have won **{prize}**!")
            await msg.edit(content="<:CH_present:767981864132018176> **GIVEAWAY ENDED** <:CH_present:767981864132018176>", embed=embed2)
        else:
            pass

    @commands.command(aliases=['greroll'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def reroll_giveaway(self, ctx, id_: int):
        try:
            for channel in ctx.guild.channels:
                try:
                    msg2 = await channel.fetch_message(id_)
                except:
                    pass
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
        except Exception as er:
            await ctx.send(f'```{er}```')

    @commands.command(aliases=['gend'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def end_giveaway(self, ctx, id_: int):
        try:
            for channel in ctx.guild.channels:
                try:
                    msg2 = await channel.fetch_message(id_)
                except:
                    await ctx.channel.send("**Error:** ID was entered incorrectly.")
                    return
        except:
            pass
        users = await msg2.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        if msg2.content != "<:CH_present:767981864132018176> **GIVEAWAY ENDED** <:CH_present:767981864132018176>":
            await msg2.channel.send(f"🎊 **Congratulations** {winner.mention}! You have won the giveaway!")
            emb = discord.Embed(
                description=f"<:tick:769432064557842442> Successfully ended giveaway in {msg2.channel.mention}",
                color=discord.Color.green())
            await ctx.send(embed=emb)
        else:
            await ctx.send(embed=discord.Embed(description = "<:tickNo:787334378639458344> Error: The giveaway was already ended.", color=discord.Color.red()))

def setup(bot):
    bot.add_cog(GiveawayCommands(bot))
