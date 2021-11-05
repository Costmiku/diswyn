import discord
import json
from discord.ext import commands

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

# log command usage
@bot.listen('on_command')
async def on_command(ctx, *error):
    print(f'{ctx.message.author} (ID {ctx.message.author.id}) used command "{ctx.message.content}"')
    if error: print(f'Error: {error}')

# show the bot's ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency*1000)}ms')

# echo command
@bot.command()
async def echo(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

# stats command
@bot.command()
async def stats(ctx):
    # neat embed
    embed = discord.Embed(title='Statistics', description='', color=0x00ff00)
    embed.add_field(name='Prefix', value=f'"{bot.command_prefix}"')
    embed.add_field(name='Owner', value=f'{bot.owner}')
    embed.add_field(name='Guilds', value=f'{len(bot.guilds)}')
    embed.add_field(name='Users', value=f'{len(bot.users)}')
    embed.add_field(name='Latency', value=f'{round(bot.latency*1000)}ms')
    await ctx.send(embed=embed)

# command to change the bot's global prefix
@bot.command()
async def globalprefix(ctx, prefix, permanent = ''):
    if (ctx.message.author.id == bot.inf.owner.id) or (ctx.message.author.id in ENV['ADDITIONAL_OWN_PERMS']):
        if permanent == 'perm' or permanent == 'permanent':
            data['prefix'] = prefix
            json.dump(data, open('data.json', 'w'), indent=4)
        bot.command_prefix = prefix
        await ctx.send(f'Prefix changed to "{prefix}"')
    else:
        await ctx.send('You are not my owner!')

# eval command
@bot.command(aliases=['eval'])
async def boteval(ctx, *, code):
    if (ctx.message.author.id == bot.inf.owner.id) or (ctx.message.author.id in ENV['ADDITIONAL_OWN_PERMS']):
        try:
            result = eval(code)
            if result:
                await ctx.send(f'```py\n{result}\n```')
        except Exception as e:
            await ctx.send(f'```py\n{e}\n```')
    else:
        await ctx.send('You are not my owner!')

bot.run(ENV['DISCORD_TOKEN'])