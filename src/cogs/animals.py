import discord
import asyncio
import os
import random
from random import choice
from discord import channel
from discord import client
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=False)

# definizione classe
class woman(commands.Cog):
    

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener(self) x eventi
    # commands.command(self)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('napolestoria'):
            await message.channel.send("Le rose sono rosse, il cielo è blu, guardati il polso l'orologio non cé più")
        gatti = ['https://cataas.com/cat/cute/says/coccolami', 'https://cataas.com/cat/cute/says/troia', 'https://cataas.com/cat/cute/says/venerami', 'https://cataas.com/cat/cute/says/bastardo']
        if message.content.startswith('catto'):
            await message.channel.send(choice(gatti))
        ducks = [ 'https://random-d.uk/api/randomimg?t=1626020422988', 'https://random-d.uk/api/randomimg?t=1626020422988', 'https://random-d.uk/api/randomimg?t=1626020422988' ]
        if message.content.startswith('papera'):
            await message.channel.send(choice(ducks))
# avvio
def setup(client):
    client.add_cog(woman(client))
