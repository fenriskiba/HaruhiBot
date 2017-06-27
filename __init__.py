import discord
import asyncio
import datetime
import subprocess
import random
import configparser

config = configparser.RawConfigParser()
config.read('Config.cfg')

client = discord.Client()

my_commands = {}


def register(cmd):
    my_commands[cmd.__name__] = cmd
    return cmd


@client.event
async def on_ready():
    print('I\'m here')


@client.event
async def on_message(message):
    if message.content.lower().startswith('!'):
        func_name = my_commands.get(message.content.lower()[1:].partition(' ')[0])
        if func_name:
            await func_name(message)


@register
async def hello(message):
    await client.send_message(message.channel, 'Hello World')


client.run(config.get('DiscordConfig', 'UserToken'))
