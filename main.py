# # # # # # # # # # # # # # #
#                           #
#   Creator: $upreme#1337   #
#   https://dsc.gg/pungas   #
#                           #
# # # # # # # # # # # # # # #

import discord 
from discord.ext import commands
import colorama

Prefix = "!"                            # Bot Prefix

colorama.init()
bot = commands.Bot(command_prefix=Prefix, help_command=None)

# Obavestava vas kad je Bot online #
@bot.event
async def on_ready():
    print(f'\u001b[37mBot status: \u001b[32mOnline')
    print(f'\u001b[37mIme: \u001b[32m{bot.user.name}')
    print(f'\u001b[37mID: \u001b[32m{bot.user.id}')
    print(f'\u001b[37mServers: \u001b[32m{len(bot.guilds)}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$upreme#1337")) # Status Bota


# Komanda

@bot.command()                          # kreirate komandu           
async def test(ctx):                    # Ime komande (test)
    await ctx.reply("Test")             # Bot salje poruku 

bot.run("ODQ3NzkyOTE4ODAyNTk1ODYw.GHFe4Z.Ur16ycQK8edQpQbvpKqVoBT2ayyGM03fA6jNiw")  # Bot token