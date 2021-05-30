import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class Handler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(":x: **Error:** missing required argment.")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(":x: **Error:** unknown command.")
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(":x: **Error:** member not found.")

def setup(client):
    client.add_cog(Handler(client))