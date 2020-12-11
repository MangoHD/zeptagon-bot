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

    snipe_message_content = None
    snipe_message_author = None
    snipe_message_id = None

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        global snipe_message_content
        global snipe_message_author
        global snipe_message_id

        snipe_message_content = message.content
        snipe_message_author = message.author
        snipe_message_id = message.id
        await asyncio.sleep(75)

        if message.id == snipe_message_id:
            snipe_message_author = None
            snipe_message_content = None
            snipe_message_id = None

    @commands.command()
    @commands.guild_only()
    async def snipe(self, ctx):
        if snipe_message_content != None:
            emb = discord.Embed(
                description = snipe_message_content,
                color=emcolor
            )
            emb.set_author(name=snipe_message_author, icon_url=snipe_message_author.avatar_url)
            footerd(emb)
            await ctx.send(embed=emb)
        else:
            await ctx.send("There's nothing to snipe.")

        snipe_message_content = None
        snipe_message_author = None
        snipe_message_id = None

def setup(bot):
    bot.add_cog(Snipe(bot))
