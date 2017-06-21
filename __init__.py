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
    if message.content.lower().startswith('!hello'):
        await client.delete_message('Hello World')

client.run(config.get('DiscordConfig', 'UserToken'))