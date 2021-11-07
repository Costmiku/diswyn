import discord
from discord.ext import commands
from main import bot, data, ENV

# bot reload command
@commands.command(aliases=['reload'])
async def botreload(ctx):
    # TODO: fix this command so it actually reloads the bot instead of erroring
    if (ctx.message.author.id == bot.inf.owner.id) or (ctx.message.author.id in ENV['ADDITIONAL_OWN_PERMS']):
        try:
            await ctx.send('Reloading...')
            bot.reload_extension('cogs.main')
            await ctx.send('Reloaded!')
        except Exception as e:
            print(str(type(e)), e)
            await ctx.send(f'Failed to reload!\n```\n{e}\n```')
    else:
        await ctx.send('You are not my owner!')

def setup(bot):
    bot.add_command(botreload)
