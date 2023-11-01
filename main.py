import discord 
import os
import datetime
from config import *
client = discord.Client()
def fetch_guild(id):
    if str(id) in os.listdir("guilds"):
        return os.listdir(f"guilds/{str(id)}")
    else:
        os.mkdir(f"guilds/{str(id)}")
        return os.listdir(f"guilds/{str(id)}")
def fetch_channel(gid,id):
    if str(id) in fetch_guild(gid):
        return os.listdir(f"guilds/{gid}/{str(id)}")
    else:
        os.mkdir(f"guilds/{gid}/{str(id)}")
        return os.listdir(f"guilds/{gid}/{str(id)}")
def write_log(gid,cid,message):
    messages = [int(m.split(".")[0]) for m in fetch_channel(gid,cid)]
    if fetch_channel(gid,cid) == [] or max(messages)+1000 < int(datetime.datetime.now().strftime('%H%M%S')):
        with open(f"guilds/{gid}/{cid}/{datetime.datetime.now().strftime('%H%M%S')}.txt","w") as f:
            f.write(f"{message.id}:{message.author.id}:{message.author.name}:{message.content}:{datetime.datetime.now().strftime('%H%M%S')}")
    else:
        with open(f"guilds/{gid}/{cid}/{max(messages)}.txt","a") as f:
            f.write(f"\n{message.id}:{message.author.id}:{message.author.name}:{message.content}:{datetime.datetime.now().strftime('%H%M%S')}")
@client.event
async def on_ready():
    print(client.user.name)
@client.event
async def on_message(message):
    write_log(message.guild.id,message.channel.id,message)
client.run(TOKEN)