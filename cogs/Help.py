import discord
import os
import asyncio
import datetime
import random
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

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['commands'])
    @commands.guild_only()
    async def help(ctx, page):
        emb = discord.Embed(
            title='Help Commands',
            color=emcolor
        )
        footerd(emb)

def setup(bot):
    bot.add_cog(Help(bot))
