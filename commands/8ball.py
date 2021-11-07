import discord
from discord.ext import commands
import random

# 8ball command
@commands.command(aliases = ['8ball'])
async def eightball(ctx, *, question):
    responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.'
    ]
    # generate embed
    embed = discord.Embed(title='8ball', description=f'Question: {question}', color=0x00ff00)
    embed.add_field(name='Answer', value=f'{random.choice(responses)}')
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(eightball)