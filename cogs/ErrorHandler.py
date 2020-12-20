import discord
import os
import asyncio
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

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        #     await ctx.message.delete()
        #     embed=discord.Embed(
        #         title='Error',
        #         description=f'`{error}`\n`{prefix}help` for a list of commands.',
        #         colour=emcolor
        #     )
        #     footerd(embed)
        #     await ctx.send(f"```{error}\nUse {prefix}help for info about commands.```", delete_after=35)

        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(
                title='Error',
                description=f'`{error}`',
                colour=emcolor
            )
            footerd(embed)
            await ctx.send('```MissingRequiredArgument: Atleast one required argument is missing.```')

        if isinstance(error, commands.BadArgument):
            embed=discord.Embed(
                title='Error',
                description=f'`{error}`',
                colour=emcolor
            )
            footerd(embed)
            await ctx.send(f'```BadArgument: Atleast one invalid argument was given```')

        if isinstance(error, discord.ext.commands.MissingPermissions):
            embed=discord.Embed(
                title='Error',
                description=f'`{error}`',
                colour=emcolor
            )
            footerd(embed)
            await ctx.send(f'```{error}```')

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
