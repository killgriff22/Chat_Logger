import discord
import os
import datetime
client = discord.Client()
TOKEN = "OTc2NTEyNjc0ODA2NTAxMzk3.GacmJv.AHgHT3BjmimpY3yZpxSLRtCJFoiowKV7gNqHkE"


class guilds:
    def fetch_guild(id, name):
        if str(id) in os.listdir("guilds"):
            return os.listdir(f"guilds/{str(id)}")
        else:
            os.mkdir(f"guilds/{str(id)}")
            with open(f"guilds/{str(id)}/name", "w") as f:
                f.write(name)
            return os.listdir(f"guilds/{str(id)}")

    def fetch_guilds():
        return os.listdir("guilds")


class channels:
    def fetch_channel(gid, id, name):
        if str(id) in guilds.fetch_guild(gid):
            return os.listdir(f"guilds/{gid}/{str(id)}")
        else:
            os.mkdir(f"guilds/{gid}/{str(id)}")
            with open(f"guilds/{gid}/{str(id)}/name", "w") as f:
                f.write(name)
            return os.listdir(f"guilds/{gid}/{str(id)}")

    def fetch_channels(gid):
        return os.listdir(f"guilds/{gid}")


def write_log(gid, cid, message):
    messages = [int(m.split(".")[0])
                for m in channels.fetch_channel(gid, cid)].remove("name")
    if messages == [] or max(messages)+1000 < int(datetime.datetime.now().strftime('%H%M%S')):
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
