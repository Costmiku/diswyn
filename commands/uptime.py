import discord
from discord.ext import commands
from main import bot
import datetime, time

# uptime command
@commands.command()
async def uptime(ctx):
    # Displays the bot's uptime.
    await ctx.send(f"I've been up for {str(datetime.timedelta(seconds=int(round(time.time()-bot.start_time))))}.")

def setup(bot):
    bot.add_command(uptime)