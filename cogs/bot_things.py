import json, discord, os, datetime
from discord.ext import commands

getprefix = ['z!', 'Z!']
actualprefix = 'z!'
motd = os.environ.get("MOTD")
footer = 'Zeptagon'
emcolor = discord.Color.blue() #0x777777
ercolor = 0xff0000

def get_prefix(client, message):
    with open("./configs/serverconfs.json", "r") as f:
        prefixes = json.load(f)
    try:
        prefixes[str(message.guild.id)]
    except KeyError:
        with open("./configs/serverconfs.json", "w") as f:
            prefixes[f"{message.guild.id}"] = {
                "prefix": "z!",
                "muterole": None,
                "events": {
                    "autorole": None,
                    "joinMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "Welcome {user}, to **{server}**!"
                    },
                    "leaveMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "**{user}** just left the server."
                    }
                }
            }
            json.dump(prefixes, f, indent=4)
        return ['z!', 'Z!']
    else:
        prefix = prefixes[str(message.guild.id)]["prefix"]
        return [prefix.lower(), prefix.upper(), prefix]

def prefix(message):
    with open("./configs/serverconfs.json", "r") as f:
        prefixes = json.load(f)
    try:
        prefixes[str(message.guild.id)]
    except KeyError:
        with open("./configs/serverconfs.json", "w") as f:
            prefixes[f"{message.guild.id}"] = {
                "prefix": "z!",
                "muterole": None,
                "events": {
                    "autorole": None,
                    "joinMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "Welcome {user}, to **{server}**!"
                    },
                    "leaveMsg": {
                        "enabled": False,
                        "channel": None,
                        "message": "**{user}** just left the server."
                    }
                }
            }
            json.dump(prefixes, f, indent=4)
        return 'z!'
    else:
        prefix = prefixes[str(message.guild.id)]["prefix"]
        return prefix

class timei():
    now = datetime.datetime.utcnow()

def footerd(emb):
    emb.add_field(
        name='_ _', 
        value="> Links: [Support Server](https://discord.gg/89eu5WD)・"
        "[Invite Me](https://discord.com/oauth2/authorize?client_id=785496485659148359&permissions=1036381431&scope=bot)\n** **",
        inline=False)
    emb.set_footer(
        text='Zeptagon', 
        icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')

def footera(e):
    e.set_footer(
        text='Zeptagon', 
        icon_url='https://cdn.discordapp.com/avatars/785496485659148359/0fc85eb060bb37c35726fabe791170fe.webp?size=1024')

theJsonDump = {
        "prefix": "z!",
        "muterole": None,
        "events": {
            "autorole": None,
            "joinMsg": {
                "enabled": False,
                "channel": None,
                "message": "Welcome {user}, to **{server}**!"
            },
            "leaveMsg": {
                "enabled": False,
                "channel": None,
                "message": "**{user}** just left the server."
            }
        }
    }