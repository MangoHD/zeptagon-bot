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

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        global snipe_message_content
        global snipe_message_author
        
        snipe_message_content = message.content
        snipe_message_author = message.author
        await asyncio.sleep(60)
        snipe_message_author = None
        snipe_message_content = None

    @commands.command()
    async def snipe(self, ctx):
        if snipe_message_content == None:
            await ctx.channel.send("Theres nothing to snipe.")
        elif snipe_message_content != None:
            embed = discord.Embed(description=f"{snipe_message_content}")
            embed.set_author(name= f"{snipe_message_author}", icon_url = f'{snipe_message_author.avatar_url}')
            await ctx.channel.send(embed=embed)
            return
        else:
            await ctx.send("There's nothing to snipe.")

def setup(bot):
    bot.add_cog(Snipe(bot))
