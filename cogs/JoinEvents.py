import discord
import os
import asyncio
import datetime
import random
from discord.ext import commands
from discord import Embed, Color
from bot_things import prefix, motd, emcolor, ercolor, footerd, footera, getprefix, get_prefix, timei

class JoinStuffs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
def setup(bot):
    bot.add_cog(JoinStuffs(bot))