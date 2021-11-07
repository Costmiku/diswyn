import discord
from discord.ext import commands
from main import bot, ENV
import json

# add owner command
@commands.command()
async def addowner(ctx, user: discord.Member):
    if (ctx.message.author.id == bot.inf.owner.id) or (ctx.message.author.id in ENV['ADDITIONAL_OWN_PERMS']):
        if user.id not in ENV['ADDITIONAL_OWN_PERMS']:
            ENV['ADDITIONAL_OWN_PERMS'].append(user.id)
            json.dump(ENV, open('env.json', 'w'), indent=4)
            await ctx.send(f'Added {user.name}#{user.discriminator} (ID {user.id}) to the owner list!')
        else:
            await ctx.send('User is already in the owner list!')
    else:
        await ctx.send('You are not my owner!')

def setup(bot):
    bot.add_command(addowner)
