import os
import random
import asyncio
import discord
import aiohttp
import requests
from discord.ext import commands
from discord import Embed, Color
from bot_things import  motd, emcolor, ercolor, footerd, footera, getprefix, get_prefix, prefix, footer, timei

class ImageCommands(commands.Cog):
    def __init__(self, bot):
        self.colors = (Color.red(), Color.gold(), Color.green(), Color.magenta(), Color.teal(), Color.dark_blue())
        self.bot = bot
        self.session = aiohttp.ClientSession(
            headers={'User-agent': 'RedditCrawler'})

    @commands.command()
    @commands.guild_only()
    async def gay(self, ctx, *, args: discord.Member = 'None'):
        await ctx.trigger_typing()
        if args == 'None':
            args = ctx.author
        avatar = args.avatar_url_as(format='jpg', size=256)
        embed=discord.Embed(
            color=emcolor,
            timestamp=timei.now)
        embed.set_image(url=f"https://some-random-api.ml/canvas/gay?avatar={avatar}")
        footera(embed)
        await ctx.send(embed=embed)

    @commands.command(aliases=['twitter'])
    @commands.guild_only()
    async def tweet(self, ctx, *, message: str):
        await ctx.trigger_typing()
        a = message.split(' ')
        msg = '+'.join(a)
        e = ctx.author.name.split(' ')
        username = '+'.join(e)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={msg}") as r:
                res = await r.json()
                em = discord.Embed(title=f'{ctx.author.name} Tweeted!', color=emcolor, timestamp=timei.now)
                em.set_image(url=res["message"])
                footera(em)
                await ctx.send(embed=em)

    # @commands.command()
    # @commands.guild_only()
    # async def wanted(self, ctx, user: discord.Member = None):
    #     if user == None:
    #         user = ctx.author
    #     wanted = Image.open("images/wanted.png")
    #     asset = user.avatar_url_as(size = 256)
    #     data = BytesIO(await asset.read())
    #     pfp = Image.open(data)
    #     pfp = pfp.resize((335, 335))
    #     wanted.paste(pfp, (57, 207))
    #     wanted.save(f"{ctx.message.id}.png")
    #     await ctx.send(file = discord.File(f"{ctx.message.id}.png"))
    #     await asyncio.sleep(2)
    #     os.system(f"del {ctx.message.id}.png")

    @commands.command(aliases=['ytcomment'])
    @commands.guild_only()
    async def youtubecomment(self, ctx, *, args):
        await ctx.trigger_typing()
        a = args.split(' ')
        b = '+'.join(a)
        c = ctx.author.avatar_url_as(format='jpg')
        e = ctx.author.name.split(' ')
        d = '+'.join(e)
        #Image.open(BytesIO(await f'https://some-random-api.ml/canvas/youtube-comment?username={d}&avatar={c}&comment={b}'.read())).save(f'{ctx.message.id}.png')
        embed=discord.Embed(
            title=f'{ctx.author.name} Commented!',
            color=emcolor)
        footera(embed)
        embed.set_image(url=f'https://some-random-api.ml/canvas/youtube-comment?username={d}&avatar={c}&comment={b}')
        await ctx.send(embed=embed)
        #await ctx.channel.send(file = discord.File(f"{ctx.message.id}.png"))
        #await asyncio.sleep(2)
        #os.system(f"del {ctx.message.id}.png")

    @commands.command()
    @commands.guild_only()
    async def triggered(self, ctx, *, args : discord.Member = None):
        if args == None:
            args = ctx.author
        e = discord.Embed(
            color=emcolor
        )
        footera(e)
        e.set_image(url=f"https://some-random-api.ml/canvas/triggered?avatar={args.avatar_url_as(format='jpg', size=256)}")
        await ctx.send(embed=e)
        # with open(f'./{ctx.message.id}.gif', 'wb') as i:
        #     i.write(requests.get(f"https://some-random-api.ml/canvas/triggered?avatar={args.avatar_url_as(format='jpg')}").content)
        # await ctx.send(file = discord.File(f"{ctx.message.id}.gif"))
        # await asyncio.sleep(2)
        # os.system(f"del {ctx.message.id}.gif")

    @commands.command(aliases=['redditmeme', 'memes'])
    @commands.guild_only()
    async def meme(self, ctx):
        await ctx.trigger_typing()
        data = await self.get_res_data(f"r/memes/random", {'limit': 10})
        await self.send_post(ctx, data[0]['data']['children'][0])
    async def random_from_post_list(self, ctx, url_part: str, params: dict):
        await ctx.trigger_typing()
        res = await self.get_res_data(url_part, params)
        error = res.get('error')
        if error:
            return await ctx.send(f"Error: {error} {res.get('message')}")
        posts = res['data']['children']
        posts = list(filter(self.post_safe_filter, posts))
        if not posts:
            return await ctx.send("No posts found.")
        if int(res['data']['ups']) < 7000:
            post = random.choice(posts)
        await self.send_post(ctx, post)
    async def get_res_data(self, url_part, params):
        async with self.session.get(f"https://reddit.com/{url_part}.json", params=params) as response:
            return await response.json()
    async def send_post(self, ctx, post):
        post = post['data']
        img_url = post.get('url')
        title = post.get('title')
        ups = post.get('ups')
        num_comments = post.get('num_comments')
        embed = Embed(title=title, color=emcolor, timestamp=timei.now)
        embed.set_image(url=img_url)
        # TODO: Use unicode instead of emojis directly
        embed.set_footer(text=f"👍 {ups} | 💬 {num_comments}")
        await ctx.send(embed=embed)
    def post_safe_filter(self, post):
        return(
            post['data']['is_reddit_media_domain'] and
            not post['data']['over_18'] and
            int(post['data']['ups']) > 7000)
    async def close_session(self):
        await self.session.close()

    @commands.command()
    @commands.guild_only()
    async def cat(self, ctx):
        await ctx.trigger_typing()
        r = requests.get('https://some-random-api.ml/img/cat')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Cat Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(
            text=f'Powered by some-random-api.ml | {footer}', 
            icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def dog(self, ctx):
        await ctx.trigger_typing()
        r = requests.get('https://some-random-api.ml/img/dog')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Dog Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(
            text=f'Powered by some-random-api.ml | {footer}', 
            icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def koala(self, ctx):
        await ctx.trigger_typing()
        r = requests.get('https://some-random-api.ml/img/koala')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Koala Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(
            text=f'Powered by some-random-api.ml | {footer}', 
            icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def bird(self, ctx):
        await ctx.trigger_typing()
        r = requests.get('https://some-random-api.ml/img/birb')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Bird Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(
            text=f'Powered by some-random-api.ml | {footer}', 
            icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def panda(self, ctx):
        await ctx.trigger_typing()
        r = requests.get('https://some-random-api.ml/img/panda')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Panda Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(
            text=f'Powered by some-random-api.ml | {footer}', 
            icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def fox(self, ctx):
        await ctx.trigger_typing()
        r = requests.get('https://some-random-api.ml/img/fox')
        data = r.json()
        img = data.get('link')
        embed = discord.Embed(color=emcolor, title='Random Fox Image')
        embed.set_image(url=f"{img}")
        embed.set_footer(
            text=f'Powered by some-random-api.ml | {footer}', 
            icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ImageCommands(bot))