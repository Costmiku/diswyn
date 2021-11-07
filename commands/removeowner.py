import discord
from discord.ext import commands
from main import bot, ENV
import json

# remove owner command
@bot.command()
async def removeowner(ctx, user: discord.Member):
    if (ctx.message.author.id == bot.inf.owner.id) or (ctx.message.author.id in ENV['ADDITIONAL_OWN_PERMS']):
        if user.id in ENV['ADDITIONAL_OWN_PERMS']:
            ENV['ADDITIONAL_OWN_PERMS'].remove(user.id)
            json.dump(ENV, open('env.json', 'w'), indent=4)
            await ctx.send(f'Removed {user.name}#{user.discriminator} (ID {user.id}) from the owner list!')
        else:
            await ctx.send('User is not in the owner list!')
    else:
        await ctx.send('You are not my owner!')

def setup(bot):
    bot.add_command(removeowner)
