import discord
import json
from discord.ext import commands
import os
from sys import argv
import time

debug_mode = False

# if env file doesn't exist or argv[1] == "setup", create it
if not os.path.isfile("env.json") or (len(argv) > 1 and argv[1] == "setup"):
    print("Creating config file...")
    with open("env.json", "w") as f:
        f.write(json.dumps({"DISCORD_TOKEN": "bot token here" if argv[2] == None else argv[2], "ADDITIONAL_OWN_PERMS": []}, indent=4))
    print("Creating server data file...")
    with open("server_data.json", "w") as f:
        f.write(json.dumps({}, indent=4))
    print("Done!")
    exit()
elif len(argv) > 1 and argv[1] == "debug":
    print("Debug mode enabled!")
    debug_mode = True

ENV = json.load(open('env.json'))
data = json.load(open('data.json'))
server_data = json.load(open('server_data.json'))

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
    # set bot start time
    bot.start_time = time.time()

# log command usage
@bot.listen('on_command')
async def on_command(ctx):
    print(f'{ctx.message.author} (ID {ctx.message.author.id}) used command "{ctx.message.content}"')

# if debug mode is enabled, print error to discord, in addition to printing to console
@bot.listen('on_command_error')
async def on_command_error(ctx, error):
    if debug_mode:
        await ctx.send(f'Error!\n```\n{error}```')
    print(f'Error!\n{error}')

# import commands
for filename in os.listdir('./commands'):
    if filename.endswith('.py') and not filename.startswith('_'):
        bot.load_extension(f'commands.{filename[:-3]}')

bot.run(ENV['DISCORD_TOKEN'])