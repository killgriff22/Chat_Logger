import discord
import os
import datetime
from config import *
client = discord.Client()
Logging = True


def fetch_guild(id):
    if str(id) in os.listdir("guilds"):
        return os.listdir(f"guilds/{str(id)}")
    else:
        os.mkdir(f"guilds/{str(id)}")
        return os.listdir(f"guilds/{str(id)}")


def fetch_channel(gid, id):
    if str(id) in fetch_guild(gid):
        return os.listdir(f"guilds/{gid}/{str(id)}")
    else:
        os.mkdir(f"guilds/{gid}/{str(id)}")
        return os.listdir(f"guilds/{gid}/{str(id)}")


def write_log(gid, cid, message):
    messages = [int(m.split(".")[0]) for m in fetch_channel(gid, cid)]
    if fetch_channel(gid, cid) == [] or max(messages)+1000 < int(datetime.datetime.now().strftime('%H%M%S')):
        with open(f"guilds/{gid}/{cid}/{datetime.datetime.now().strftime('%H%M%S')}.txt", "w") as f:
            try:
                f.write(
                    f"{message.id}:{message.author.id}:{message.author.name}:{message.content}:{datetime.datetime.now().strftime('%H%M%S')}")
            except:
                print(
                    f"Could Not Log {message.id}:{message.content}:{datetime.datetime.now().strftime('%H%M%S')}")
    else:
        with open(f"guilds/{gid}/{cid}/{max(messages)}.txt", "a") as f:
            try:
                f.write(
                    f"\n{message.id}:{message.author.id}:{message.author.name}:{message.content}:{datetime.datetime.now().strftime('%H%M%S')}")
            except:
                print(
                    f"Could Not Log {message.id}:{message.content}:{datetime.datetime.now().strftime('%H%M%S')}")


async def check_command(message):
    if not message.author == client.user:
        return
    if not message.content.startswith("#!"):
        return
    match message.content.split(" ")[0].lower():
        case "#!help":
            await message.channel.send(f"""``` help
1. Toggle Logging with #!Log
2. Toggle Logging for a specific channel with #!LogChannel (id)
3. Toggle Logging for a specific guild with #!LogGuild (id)
4. Toggle Logging for a specific user with #!LogUser (id)
5. AutoReact with #!react (message) (messageid)```""")
        case "#!log":
            if Logging:
                Logging = False
                await message.channel.send("Logging Disabled")
            else:
                Logging = True
                await message.channel.send("Logging Enabled")
        case "#!react":
            emojis = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮",
                      "🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷",
                      "🇸","🇹","🇺","🇻","🇼","🇽","🇾","🇿",]
            letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m", "n", "o", "p", "q", "r",
                       "s", "t", "u", "v", "w", "x", "y", "z"]
            target_message = await message.channel.fetch_message(int(message.content.split(" ")[2]))
            for letter in message.content.split(" ")[1].lower():
                await target_message.add_reaction(emojis[letters.index(letter)])


@client.event
async def on_ready():
    print(client.user.name)


@client.event
async def on_message(message):
    # write_log(message.guild.id, message.channel.id, message)
    await check_command(message)
client.run(TOKEN)
