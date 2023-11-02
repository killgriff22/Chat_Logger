import discord
import os
import datetime
client = discord.Client()
TOKEN = ""


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


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    print(f"ID: {client.user.id}")
    print("------")
