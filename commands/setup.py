# setup command for moderation etc.
import discord
from discord.ext import commands
from main import bot, ENV, server_data # server_data is a dict, we'll use it to store server specific data
import json

@commands.command()
async def setup(ctx, *muted_role_name):
    # only run this command if the caller has manage server permissions
    if ctx.author.guild_permissions.manage_guild:
        server_data[ctx.guild.id] = {
            "mute_cmd": {
                "role": muted_role_name[0] if muted_role_name else "Muted",
                "mutes": {}
            },
            "warns": {},
            "bans": {}
        }
        with open('server_data.json', 'w') as f:
            json.dump(server_data, f, indent=4)
        # create the muted role
        muted_role = await ctx.guild.create_role(name=server_data[ctx.guild.id]["mute_cmd"]["role"])
        # add exceptions for all channels with the muted role
        try:
            for channel in ctx.guild.channels:
                if channel.permissions_for(muted_role).send_messages:
                    await channel.set_permissions(muted_role, send_messages=False)
        except Exception as e:
            print(e)
            await ctx.send(f'Failed to set permissions for muted role!\n```\n{e}\n```')
    else:
        await ctx.send("You don't have permission to run this command!")