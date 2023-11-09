from config import *
guilds_lst = [int(guild) for guild in guilds.fetch_guilds()]
guilds_names = [open(f"guilds/{guild}/name", "r").read()
                for guild in guilds_lst]
for name in guilds_names:
    print(name, end=": ")
    print(guilds_lst[guilds_names.index(name)])
print()
input()
