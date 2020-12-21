import discord
import os
import random
import dyv_math as mfmath
from discord.ext import commands
from bot_things import prefix, motd, emcolor, ercolor, footerd, getprefix, get_prefix

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['randomnumber','random_number','randomnum'])
    @commands.guild_only()
    async def randnum(self, ctx, min : int, max : int):
        var32_1 = discord.Embed(
            title='Random Number Generator!',
            description=f'Requested by {ctx.author.mention}\n\nMinimum = `{min}`\nMaximum = `{max}`\n\nRandom Number is: `{random.randint(min, max)}`',
            colour=emcolor
        )
        footerd(var32_1)
        await ctx.channel.send("", embed=var32_1)

    @commands.command(aliases=['math_multiply', 'multiply'])
    @commands.guild_only()
    async def math_multiply_cmd(self, ctx, arg5 : int, arg6 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.multiply(arg5, arg6, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(mfmath.multiply(arg5, arg6, n1, n2))

    @commands.command(aliases=['math_divide', 'divide'])
    @commands.guild_only()
    async def math_divide_cmd(self, ctx, arg7 : int, arg8 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.divide(arg7, arg8, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(mfmath.divide(arg7, arg8, n1, n2))

    @commands.command(aliases=['math_add', 'add'])
    @commands.guild_only()
    async def math_add_cmd(self, ctx, arg9 : int, arg10 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.add(arg9, arg10, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(mfmath.add(arg9, arg10, n1, n2))

    @commands.command(aliases=['math_substract', 'substract'])
    @commands.guild_only()
    async def math_substract_cmd(self, ctx, arg11 : int, arg12 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.substract(arg11, arg12, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(mfmath.substract(arg11, arg12, n1, n2))

    @commands.command(aliases=['math_square', 'square'])
    @commands.guild_only()
    async def math_square_cmd(self, ctx, arg34_1 : int, arg34_2 : int):
        emb = discord.Embed(
            description=f'{mfmath.square(arg34_1, arg34_2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(mfmath.square(arg34_1, arg34_2))

def setup(bot):
    bot.add_cog(Math(bot))