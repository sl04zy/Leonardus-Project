# fucking imports :)
import discord
import asyncio
import os
import random
from random import choice
from discord import channel
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

client = commands.Bot(command_prefix='leo ') # Bot command prefix. Example: leo [command] [args]
token = '' # No


# start event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Creating a better world.")) # Is used to set a custom status to the bot
    print(f"""
{Fore.YELLOW} __                          _         
|  |   ___ ___ ___ ___ ___ _| |_ _ ___ 
|  |__| -_| . |   | .'|  _| . | | |_ -|
|_____|___|___|_|_|__,|_| |___|___|___|
                                       
{Fore.BLUE}{Style.BRIGHT}Created by sl04zy{Fore.RESET}{Style.RESET_ALL}
{Fore.GREEN}{Style.BRIGHT}
* Main file ready
* Cogs online
* Handler online
* Chat-Filter online
{Fore.RESET}
{Fore.RED}Format: leo [command]{Fore.RESET}{Style.RESET_ALL}

""")
    Log = open("log.txt", "a")
    Log.write(f"\n\n[!] Leonardus Started [!]\n\n")
    Log.close()


@client.command(aliases=["shutdown"])
@has_permissions(administrator=True)
async def spegni(ctx):
    message = await ctx.send("*Spegnimento in corso...*")
    await asyncio.sleep(3)
    await message.edit(content="*Spegmimento compeltato!*")
    await ctx.bot.logout()



# Command for loading existing cogs without restarting the bot
@client.command()
@has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"*{extension} loaded!*")

# Command for reloading any cog
@client.command()
@has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"*{extension} reloaded!*")

# Command for unloading existing cogs without restarting the bot
@client.command()
@has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"*{extension} unloaded!*")

# Loop for loading/starting cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)







