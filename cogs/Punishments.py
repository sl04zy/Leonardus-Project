import discord
from discord import message
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import asyncio

from discord.ext.commands.errors import MemberNotFound

class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]
        if amount.isdigit() and unit in ['s', 'm', 'h', 'd']: #seconds and minutes
            return (int(amount), unit)
        raise commands.BadArgument(message="*Invalid duration.*")



class Punishments(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(aliases=["Tempan"])
    @has_permissions(ban_members=True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = duration
        await ctx.guild.ban(member)
        await ctx.send(f"{member.mention} has been temporaly banned from the server.")
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)

    @commands.command(aliases=["Ban"])
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter):
        await ctx.guild.ban(member)
        await ctx.send(f"{member.mention} has been banned the server.")

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



    @commands.command(aliases=["Kick"])
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter):
        await ctx.guild.kick(member)
        await ctx.send(f"{member.mention} has been kicked from the server.")


def setup(client):
    client.add_cog(Punishments(client))