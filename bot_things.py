import json, discord, os
from discord.ext import commands

getprefix = ['z!', 'Z!']
prefix = 'z!'
motd = os.environ.get("MOTD")
footer = 'Zeptagon'
emcolor = 0x777777
ercolor = 0xff0000

def get_prefix(client,message):
    if not message.guild:
        return commands.when_mentioned_or('z!' or 'Z!')(client, message)

    with open("./configs/prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or('z!' or 'Z!')(client, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(client, message)

def footerd(emb):
    emb.add_field(name='_ _', value='Links: [Support Server](https://discord.gg/89eu5WD)・[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=8&scope=bot)')
    emb.set_footer(text='Zeptagon', icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')
