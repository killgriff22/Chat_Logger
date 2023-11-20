from config import *
from pokes import pokemon as names
import datetime
import time
lastpoke = ""
approved_channels = [
    1174005255189569587
]
pokemon_have = {}


@client.event
async def on_message(ctx):
    global lastmessage, lastpoke, pokemon_have
    if not ctx.channel.id in approved_channels:
        return
    print(ctx.content)
    if True:  # not ctx.author == client.user:
        if not ctx.author.id in [716390085896962058, 976512674806501397]:
            return
        if ctx.embeds:
            if "your pokémon" in ctx.embeds[0].title.lower():
                # determine pokemon on page
                description = (ctx.embeds[0].description.split("\n"))
                for item in description:
                    split = item.split("`")[2].split(" ")[1].split("**")[0]
                    if split in pokemon_have.keys():
                        pokemon_have.update({split: pokemon_have[split] + 1})
                    else:
                        pokemon_have.update({split: 1})
                # determine page number, and number of pages
                print(ctx.embeds[0].footer.text)
                page_count = int(ctx.embeds[0].footer.text.split(
                    " ")[5][:-1])/20
                page = int(ctx.embeds[0].footer.text.split(
                    " ")[2].split("–")[1])//20
                if int(str(page_count).split(".")[1]) > 0:
                    page_count = int(str(page_count).split(".")[0])+1
                print(page)
                print(pokemon_have)
                sleep = 5
                print(f"sleeping for {sleep} seconds")
                time.sleep(sleep)
                await ctx.channel.send(f"<@716390085896962058> p {page+1}")
                return
            if not "wild" in ctx.embeds[0].title.lower():
                return
            await ctx.channel.send(f"<@716390085896962058> h")
        if "Congratulations" in ctx.content:
            await ctx.channel.send(":3")
            split = ctx.content.split(" ")[7][:-1]
            if split in pokemon_have.keys():
                pokemon_have.update({split: pokemon_have[split] + 1})
            else:
                pokemon_have.update({split: 1})
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
