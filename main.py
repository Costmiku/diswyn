import discord
import json
from discord.ext import commands
import os

ENV = json.load(open('env.json'))
data = json.load(open('data.json'))

bot = commands.Bot(command_prefix=data['prefix'])

@bot.listen('on_ready')
async def on_ready():
    print('Logged in as')
    print('| Username:', bot.user)
    print('| ID:', bot.user.id)
    print('| Prefix:', f'"{bot.command_prefix}"')
    print('------')
    bot.inf = await bot.application_info()
    bot.owner = f'{bot.inf.owner.name}#{bot.inf.owner.discriminator}'
    # set bot status
    await bot.change_presence(activity=discord.Game(data['status'].format(prefix=bot.command_prefix)))

# log command usage
@bot.listen('on_command')
async def on_command(ctx, *error):
    print(f'{ctx.message.author} (ID {ctx.message.author.id}) used command "{ctx.message.content}"')
    if error: print(f'Error: {error}')

# import commands
for filename in os.listdir('./commands'):
    if filename.endswith('.py') and not filename.startswith('_'):
        bot.load_extension(f'commands.{filename[:-3]}')

bot.run(ENV['DISCORD_TOKEN'])