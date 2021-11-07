import discord
from discord.ext import commands
from main import bot, data, ENV

@commands.command(aliases=['eval'])
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

def setup(bot):
    bot.add_command(boteval)