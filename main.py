# # # # # # # # # # # # # # #
#                           #
#   Creator: $upreme#1337   #
#   https://dsc.gg/pungas   #
#                           #
# # # # # # # # # # # # # # #

import discord 
from discord.ext import commands

Prefix = "!"                            # Bot Prefix

bot = commands.Bot(command_prefix=Prefix, help_command=None)

# Obavestava vas kad je Bot online #
@bot.event
async def on_ready():
    print('Bot status: Online')
    print(f'Ime: {bot.user.name}')
    print(f'ID:  {bot.user.id}')
    print(f'Servers: {len(bot.guilds)}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$upreme#1337")) # Status Bota


# Komanda

@bot.command()                          # kreirate komandu           
async def test(ctx):                    # Ime komande (test)
    await ctx.reply("Test")             # Bot salje poruku 

bot.run("ODQ3NzkyOTE4ODAyNTk1ODYw.GHFe4Z.Ur16ycQK8edQpQbvpKqVoBT2ayyGM03fA6jNiw")  # Bot token