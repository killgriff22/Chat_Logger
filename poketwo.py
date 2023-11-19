from config import *
from pokes import pokemon as names
import datetime
lastpoke = ""
shards = int(input("How many shards do you have?"))
pc = int(input("What is your how many pokecoins do you have?"))


@client.event
async def on_message(ctx):
    global lastmessage, lastpoke
    if not ctx.channel.id == 1174005255189569587:
        return
    print(ctx.content)
    if True:  # not ctx.author == client.user:
        if not ctx.author.id in [716390085896962058, 976512674806501397]:
            return
        if ctx.embeds:
            if not "wild" in ctx.embeds[0].title.lower():
                return
            await ctx.channel.send(f"<@716390085896962058> h")
        if "Congratulations" in ctx.content:
            await ctx.channel.send(":3")
        elif "That is the wrong pokémon!" in ctx.content:
            await ctx.channel.send(f"<@716390085896962058> h")
        elif 'The pokémon is' in ctx.content:
            poke = ctx.content.split(' ')[3:]
            if len(poke) > 1:
                poke = f"{poke[0]} {poke[1][:-1]}".replace("\\", "")
            else:
                poke = poke[0].replace("\\", "")[:-1]
            lastpoke = poke
            poses = []
            bestcandidate = ""
            print(poke)
            for i, char in enumerate(poke):
                if not char in [r"\\", "_"]:
                    poses.append({str(i): char})
            print(poses)
            for pokemon in names:
                if len(pokemon) == len(poke):
                    matches = 0
                    for pos in poses:
                        for key in pos:
                            if pokemon[int(key)] == pos[key]:
                                matches += 1
                    if matches >= len(poses):
                        bestcandidate = pokemon
            print(bestcandidate)
            await ctx.channel.send(f"<@716390085896962058> c {bestcandidate}")

client.run(TOKEN)
