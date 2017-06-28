import configparser
import discord

import modules.simple_commands

from modules.settings import my_commands

# Import Configurations
config = configparser.RawConfigParser()
config.read('Config.cfg')

client = discord.Client()


@client.event
async def on_ready():
    print('I\'m here')


@client.event
async def on_message(message):
    if message.content.lower().startswith('!'):
        func_name = message.content.lower()[1:].partition(' ')[0]
        func = my_commands.get(func_name)
        if func:
            await func(client, message)

client.run(config.get('DiscordConfig', 'UserToken'))
