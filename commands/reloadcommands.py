import discord
from discord.ext import commands
from main import bot, data, ENV

# Reloads all commands
@commands.command()
async def reloadcommands(ctx):
    # is supposed to reload all commands
    # TODO: fix this command so it actually reloads the commands instead of erroring
    await ctx.send('Reloading commands...')
    if (ctx.message.author.id == bot.inf.owner.id) or (ctx.message.author.id in ENV['ADDITIONAL_OWN_PERMS']):
        try:
            for command in bot.commands:
                bot.unload_extension(f'commands.{command.name}')
                bot.load_extension(f'commands.{command.name}')
            await ctx.send(f'Reloaded all commands!')
        except Exception as e:
            print(str(type(e)), e)
            await ctx.send(f'Failed to reload!\n```\n{e}\n```')
    else:
        await ctx.send('You are not my owner!')

def setup(bot):
    bot.add_command(reloadcommands)
