import discord
from discord.ext import commands
from main import bot, ENV

# bot shutdown command
@commands.command()
async def shutdown(ctx):
    if (ctx.message.author.id == bot.inf.owner.id) or (ctx.message.author.id in ENV['ADDITIONAL_OWN_PERMS']):
        await ctx.send('Shutting down...')
        await bot.close()
    else:
        await ctx.send('You are not my owner!')

def setup(bot):
    bot.add_command(shutdown)
