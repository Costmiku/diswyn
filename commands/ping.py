import discord
from discord.ext import commands
from main import bot

# ping command
@commands.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency*1000)}ms')

def setup(bot):
    bot.add_command(ping)