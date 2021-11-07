import discord
from discord.ext import commands

# echo command
@commands.command()
async def echo(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

def setup(bot):
    bot.add_command(echo)