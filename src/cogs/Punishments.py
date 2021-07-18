import discord
from discord import message
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import asyncio
from discord.ext.commands.errors import MemberNotFound

# Custom converter
# Needed for tempban command
class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]
        if amount.isdigit() and unit in ['s', 'm', 'h', 'd']: #seconds, minutes, hours and days
            return (int(amount), unit)
        raise commands.BadArgument(message="*Invalid duration.*")

# Converter documentation:
# https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=converters#converters

class Punishments(commands.Cog):

    def __init__(self, client):
        self.client = client


    # Tempban command
    @commands.command(aliases=["Tempban"])
    @has_permissions(ban_members=True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400} # Multiplier. This is needed for converting seconds to minutes, hours and days.
        amount, unit = duration
        await ctx.guild.ban(member)
        await ctx.send(f"{member.mention} has been temporaly banned from the server.")
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    # Ban command
    @commands.command(aliases=["Ban"])
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter):
        await ctx.guild.ban(member)
        await ctx.send(f"{member.mention} has been banned the server.")

    # Unban command
    @commands.command(aliases=["Unban", "UnBan"])
    @has_permissions(kick_members=True, ban_members=True)
    async def unban(self, ctx, *, member: commands.MemberConverter):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member.mention} has been unbanned.")
                print(f"User unbanned\n User: {member}")
                return


    # Kick command
    @commands.command(aliases=["Kick"])
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter):
        await ctx.guild.kick(member)
        await ctx.send(f"{member.mention} has been kicked from the server.")

    # Mute command
    @commands.command(aliases=['Mute'])
    @has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400} # Multiplier. This is needed for converting seconds to minutes, hours and days.
        amount, unit = duration
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await ctx.send(f"{member.mention} has been muted from the chat.")
        await asyncio.sleep(amount * multiplier[unit])
        await member.remove_roles(muted_role)

def setup(client):
    client.add_cog(Punishments(client))