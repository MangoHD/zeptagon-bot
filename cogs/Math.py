import discord
import os
import dyv_math as mfmath
from discord.ext import commands

getprefix = ['z!', 'Z!']
prefix = 'z!'
motd = 'Newly made bot :D'
footer = 'Zeptagon'
emcolor = 0x777777
ercolor = 0xff0000
def footerd(emb):
    emb.add_field(name='_ _', value='Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)')
    emb.set_footer(text='Zeptagon', icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['math_multiply', 'multiply'])
    @commands.guild_only()
    async def math_multiply_cmd(self, ctx, arg5 : int, arg6 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.multiply(arg5, arg6, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(embed=emb)

    @commands.command(aliases=['math_divide', 'divide'])
    @commands.guild_only()
    async def math_divide_cmd(self, ctx, arg7 : int, arg8 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.divide(arg7, arg8, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(embed=emb)

    @commands.command(aliases=['math_add', 'add'])
    @commands.guild_only()
    async def math_add_cmd(self, ctx, arg9 : int, arg10 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.add(arg9, arg10, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(embed=emb)

    @commands.command(aliases=['math_substract', 'substract'])
    @commands.guild_only()
    async def math_substract_cmd(self, ctx, arg11 : int, arg12 : int, n1 : int = '0', n2 : int = '0'):
        emb = discord.Embed(
            description=f'{mfmath.substract(arg11, arg12, n1, n2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(embed=emb)

    @commands.command(aliases=['math_square', 'square'])
    @commands.guild_only()
    async def math_square_cmd(self, ctx, arg34_1 : int, arg34_2 : int):
        emb = discord.Embed(
            description=f'{mfmath.square(arg34_1, arg34_2)}',
            color=emcolor
        )
        emb.set_author(name='Calculator', icon_url=ctx.author.avatar_url)
        footerd(emb)
        await ctx.channel.send(embed=emb)

def setup(bot):
    bot.add_cog(Math(bot))
