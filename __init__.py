import configparser
import discord

from settings import my_commands, register

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
            await func(message)


# TODO: Move to new file
@register
async def hello(message):
    await client.send_message(message.channel, 'Hello World')


@register
async def echo(message):
    msg = message.content.split(' ', 1)[1]
    await client.send_message(message.channel, msg)
    await client.delete_message(message)

# TODO: Create Pray/Fortune Functionality


client.run(config.get('DiscordConfig', 'UserToken'))
