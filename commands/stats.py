import discord
from discord.ext import commands
from main import bot, data

# stats command
@commands.command()
async def stats(ctx):
    # neat embed
    embed = discord.Embed(title='Statistics', description='', color=0x00ff00)
    embed.add_field(name='Prefix', value=f'`{bot.command_prefix}`')
    embed.add_field(name='Owner', value=f'{bot.owner}')
    embed.add_field(name='Guilds', value=f'{len(bot.guilds)}')
    embed.add_field(name='Users', value=f'{len(bot.users)}')
    embed.add_field(name='Latency', value=f'{round(bot.latency*1000)}ms')
    embed.add_field(name='Version', value=data['version'])
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(stats)