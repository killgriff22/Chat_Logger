import threading
from config import *
import asyncio
Logging = True
animate_flag = threading.Event()


async def check_command(message):
    if message == None:
        return
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
            emojis = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", " 🇬 ", "🇭", "🇮",
                      "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", " 🇵 ", "🇶", "🇷",
                      "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿",]
            letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m", "n", "o", "p", "q", "r",
                       "s", "t", "u", "v", "w", "x", "y", "z"]
            target_message = await message.channel.fetch_message(int(message.content.split(" ")[2]))
            for letter in message.content.split(" ")[1].lower():
                await target_message.add_reaction(emojis[letters.index(letter)])
        case "#!state":
            await set_status(message)
        case "#!anim":
            animations = {
                "cars": [
                    "❤🩷🧡💛💚💙🩵",
                    "🩷🧡💛💚💙🩵❤",
                    "🧡💛💚💙🩵❤🩷",
                    "💛💚💙🩵❤🩷🧡",
                    "💚💙🩵❤🩷🧡💛",
                    "💙🩵❤🩷🧡💛💚",
                    "🩵❤🩷🧡💛💚💙"
                ]
            }
            if not animate_flag.is_set():
                animate_flag.set()
                asyncio.run(animate_status(
                    animations[message.content.split(" ")[1]]))
            else:
                animate_flag.clear()


async def set_status(message):
    if message == None:
        return
    if not message.content.startswith("#!"):
        return
    status = message.content.split(" ")[2:]
    _ = ""
    for item in status:
        _ += item+" "
    status = _
    match message.content.lower().split(" ")[1]:
        case "game":
            await client.change_presence(activity=discord.Game(name=status))
        case "listen":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
        case "watch":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        case "stream":
            await client.change_presence(activity=discord.Streaming(name=status, url="x-x.ftp.sh"))


async def animate_status(animation):
    while animate_flag.is_set():
        for status in animation:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
            await asyncio.sleep(10)


@client.event
async def on_message(message):
    # write_log(message.guild.id, message.channel.id, message)
    print(message.content)
    await check_command(message)

# asyncio.run(set_status(message_))
client.run(TOKEN)
