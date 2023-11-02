from config import *
Logging = True

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
async def on_message(message):
    # write_log(message.guild.id, message.channel.id, message)
    await check_command(message)

client.run(TOKEN)
