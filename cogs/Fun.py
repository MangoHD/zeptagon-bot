import os
import re
import io
import base64
import random
import asyncio
import discord
import aiohttp
import requests
import pyfiglet
from bs4 import BeautifulSoup as bs4
from discord.ext import commands
from bot_things import motd, emcolor, ercolor, footerd, getprefix, get_prefix, prefix, footera

regionals = {
    'a': '\N{REGIONAL INDICATOR SYMBOL LETTER A}', 'b': '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
    'c': '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
    'd': '\N{REGIONAL INDICATOR SYMBOL LETTER D}', 'e': '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
    'f': '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
    'g': '\N{REGIONAL INDICATOR SYMBOL LETTER G}', 'h': '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
    'i': '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
    'j': '\N{REGIONAL INDICATOR SYMBOL LETTER J}', 'k': '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
    'l': '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
    'm': '\N{REGIONAL INDICATOR SYMBOL LETTER M}', 'n': '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
    'o': '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
    'p': '\N{REGIONAL INDICATOR SYMBOL LETTER P}', 'q': '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
    'r': '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
    's': '\N{REGIONAL INDICATOR SYMBOL LETTER S}', 't': '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
    'u': '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
    'v': '\N{REGIONAL INDICATOR SYMBOL LETTER V}', 'w': '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
    'x': '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
    'y': '\N{REGIONAL INDICATOR SYMBOL LETTER Y}', 'z': '\N{REGIONAL INDICATOR SYMBOL LETTER Z}',
    '0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣',
    '4': '4⃣', '5': '5⃣', '6': '6⃣', '7': '7⃣', '8': '8⃣', '9': '9⃣', '!': '\u2757',
    '?': '\u2753'
}

emoji_reg = re.compile(r'<:.+?:([0-9]{15,21})>')

text_flip = {}
char_list = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}"
alt_char_list = "{|}zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ,‾^[\\]Z⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀@¿<=>;:68ㄥ9ϛㄣƐᄅƖ0/˙-'+*(),⅋%$#¡"[::-1]
for idx, char in enumerate(char_list):
    text_flip[char] = alt_char_list[idx]
    text_flip[alt_char_list[idx]] = char

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gayrate'])
    @commands.guild_only()
    async def howgay(self, ctx, *, args : discord.Member = None):
        if args == None:
            args = ctx.author
        await ctx.send(f"**{args.name}** is {random.randint(1,100)}% gay.")

    @commands.command(aliases=['simprate'])
    @commands.guild_only()
    async def howsimp(self, ctx, *, args : discord.Member = None):
        if args == None:
            args = ctx.author
        await ctx.send(f"**{args.name}** is {random.randint(1,100)}% a simp.")

    @commands.command()
    @commands.guild_only()
    async def choice(self, ctx, *, args):
        a = args.split('|')
        b = ', '.join(a)
        embed=discord.Embed(
            title='Random Choice',
            description=f'\n**Choices:**\n{b}\n\n**Picked:**\n{random.choice(a)}',
            color=emcolor)
        footerd(embed)
        await ctx.send(embed=embed)

    @commands.command(aliases=['8ball'])
    @commands.guild_only()
    async def eight_ball_answr(self, ctx, *, question):
        answers = [
            'Possibly.',
            'Ask Again Later...',
            'Try Again.',
            'It\'s Certain.',
            'Most Likely No',
            'Most Likely Yes',
            'No.',
            'Yes.',
            'Definetly a Yes.',
            'Definetly a No.',
            'What did you expected?',
            'Cannot answer now, try again.',
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes, definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]
        embed = discord.Embed(
            title='8ball',
            description=f"\n\n**Question Asked:**\n{question}\n\n**Answer:**\n*{random.choice(answers)}*",
            colour=emcolor)
        footerd(embed)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def gifsearch(self, ctx, query=None):
        if query is None:
            r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
            res = r.json()
            await ctx.send(res['data']['url'])
        else:
            r = requests.get(
                f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
            res = r.json()
            await ctx.send(res['data'][0]["url"])

    @commands.command(aliases=["searchimg", "searchimage", "imagesearch", "imgsearch"])
    @commands.guild_only()
    async def image(self, ctx, *, args):
        url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
        page = requests.get(url)
        soup = bs4(page.text, 'html.parser')
        image_tags = soup.findAll('img')
        if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
            link = image_tags[2]['src']
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(link) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"{ctx.message.id}.png"))
            except:
                await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
        else:
            await ctx.send("Nothing found for **" + args + "**")

    @commands.command()
    @commands.guild_only()
    async def encode(self, ctx, *, args):
        i = args.encode('ascii')
        b = base64.b64encode(i)
        b64 = b.decode('ascii')
        await ctx.send(b64)

    @commands.command()
    @commands.guild_only()
    async def decode(self, ctx, *, args):
        i = args.encode('ascii')
        b = base64.b64decode(i)
        b64 = b.decode('ascii')
        await ctx.send(b64)

    @commands.command()
    @commands.guild_only()
    async def textflip(self, ctx, *, msg):
        result = ""
        for char in msg:
            if char in text_flip:
                result += text_flip[char]
            else:
                result += char
        await ctx.send(result[::-1])

    @commands.command()
    @commands.guild_only()
    async def spacetext(self, ctx, *, msg):
        if msg.split(' ', 1)[0].isdigit():
            spaces = int(msg.split(' ', 1)[0]) * ' '
            msg = msg.split(' ', 1)[1].strip()
        else:
            spaces = '  '
        spaced_message = spaces.join(list(msg))
        await ctx.send(spaced_message)

    @commands.command()
    @commands.guild_only()
    async def ascii(self, ctx, *, args):
        ascii_ = pyfiglet.figlet_format(args)
        await ctx.send(f"```{ascii_}```")

    @commands.command(pass_context=True, aliases=['regional'])
    @commands.guild_only()
    async def bigtext(self, ctx, *, msg):
        msg = list(msg)
        regional_list = [regionals[x.lower()] if x.isalnum() or x in ["!", "?"] else x for x in msg]
        regional_output = ' '.join(regional_list) #\u200b alternative for space
        await ctx.send(regional_output)

    @commands.command(aliases=['findiq'])
    @commands.guild_only()
    async def iq(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        iq = random.randint(12, 200)
        if iq < 45:
            message='Wow he\'s a fucking retard. Go learn preschool you dumbfuck.'
        elif iq < 120:
            message='Average IQ anyways.'
        elif iq > 160:
            message='Wow. He could be the next Albert Einstein'
        else:
            message=''
        await ctx.send(f"**{member.name}** has {iq} IQ.")

    @commands.command()
    @commands.guild_only()
    async def hack(self, ctx, user: discord.Member):
        msg = await ctx.send(f'⌛ Hacking started for user {user.name}.')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Getting user\'s email...')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Fetching login (token found)...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Fetching user\'s DMs...')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Tracing user\'s IP from messages...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Last DM: `stop pinging`')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Finding most used feature in discord...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Most used feature: `Selfbots`')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Injecting threats `Trojan:Win32/Ymacco.AA53`, `Trojan:Win32/Wacatac.D5!ml` and `HackTool:Win32/Keygen`...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Injected `Trojan:Win32/Wacatac.D5!ml`... (Status: `High`)')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Injected `Trojan:Win32/Ymacco.AA53`... (Status: `Severe`)')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Injected `HackTool:Win32/KeyGen`... (Status: `Very High`)')
        await asyncio.sleep(2)
        await msg.edit(content='⌛ Found AppData information... Nitro Stolen...')
        await asyncio.sleep(2)
        await msg.edit(content='⏳ Selling data to goverment')
        await asyncio.sleep(2)
        await msg.edit(content=f'⌛ Getting house info with discriminator of #{user.discriminator}')
        await asyncio.sleep(2)
        await msg.edit(content=f'⌛ Email: **{user.name}h@gmail.com**\nPassword: **\\*\\*\\*\\*\\*\\*\\***')
        await asyncio.sleep(1)
        await msg.edit(content=f'✅ User has been hacked! Login info saved in DMs.')

    @commands.command(aliases=['claptalk'])
    @commands.guild_only()
    async def clap(self, ctx, *, message):
        await ctx.send(' 👏 '.join(message.split(' ')))

    @commands.command(name='1337', aliases=['leetspeak','1337speak'])
    @commands.guild_only()
    async def _1337_speak(self, ctx, *, text):
        text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
            .replace('E', '3').replace('i', '!').replace('I', '!') \
            .replace('o', '0').replace('O', '0')
        await ctx.send(f'{text}')

    @commands.command()
    @commands.guild_only()
    async def embed(self, ctx, *, args):
        argsplit = args.split("|")
        if "|" in ctx.message.content:
            title = argsplit[0]
            desc = argsplit[1]
            embed = discord.Embed(
                title=title,  description=desc, colour=emcolor)
        else:
            title=args
            embed = discord.Embed(title=title, colour=emcolor)
        footera(embed)
        await ctx.send(embed=embed)

    @commands.command()
    async def findip(self, ctx, member: discord.Member):
        nums = '1234567890'
        await ctx.send(f'{member.mention}\'s IP is `18'+random.choice(nums)+f'.{random.randint(2, 7)}'+''.join(random.choice(nums) for i in range(random.randint(1, 2)))+'.'+''.join(random.choice(nums) for i in range(random.randint(2, 3)))+'.'+''.join(random.choice(nums) for i in range(3))+'`')

    @commands.command(aliases=['coinflip','flipcoin'])
    @commands.guild_only()
    async def coin(self, ctx):
        var_2 = ['Heads', 'Tails', 'Coin was lost. Try again.']
        var_3 = await ctx.channel.send("Flipping the **coin**... <a:coin:772658216580153355>")
        await asyncio.sleep(2)
        await var_3.edit(content=random.choice(var_2))

    @commands.command(aliases=['rolldice'])
    @commands.guild_only()
    async def dice(self, ctx):
        var_4 = ['<:1_:772644723076366377>', '<:2_:772644722959187969>', '<:3_:772644723173097522>', '<:4_:772644723269697586>', '<:5_:772644723121979443>', '<:6_:772644723080953907>']
        var_5 = await ctx.channel.send("Rolling **dice**... <a:dicegif:772644723474169899>")
        await asyncio.sleep(4)
        await var_5.edit(content=random.choice(var_4))

def setup(bot):
    bot.add_cog(FunCommands(bot))