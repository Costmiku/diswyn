import discord
import json
from discord.ext import commands

ENV = json.load(open('env.json'))

bot = commands.Bot(command_prefix='!!')

@bot.listen('on_ready')
async def on_ready():
    print('Logged in as')
    print('| Username:', bot.user)
    print('| ID:', bot.user.id)
    print('| Prefix:', f'"{bot.command_prefix}"')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency*1000)}ms')

bot.run(ENV['DISCORD_TOKEN'])