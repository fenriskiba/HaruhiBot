import discord
import asyncio
import datetime
import subprocess
import random
import configparser

config = configparser.RawConfigParser()
config.read('Config.cfg')

client = discord.Client()


@client.event
async def on_ready():
    print('I\'m here')


@client.event
async def on_message(message):
    call = 'await hello(message)'
    await exec(call)


async def hello(message):
    if message.content.lower().startswith('!hello'):
        await client.send_message(message.channel, 'Hello World')


client.run(config.get('DiscordConfig', 'UserToken'))
