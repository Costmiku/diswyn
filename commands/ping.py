import discord
from discord.ext import commands

# ping command
@commands.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(commands.latency*1000)}ms')

def setup(bot):
    bot.add_command(ping)