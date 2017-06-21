import discord
import asyncio
import datetime
import subprocess
import random

client = discord.Client()

@client.event
async def on_ready():
    print('I\'m here')

@client.event
async def on_message(message):
    if message.content.lower().startswith('!hello'):
        await client.delete_message('Hello World')

#TODO: set this up
#client.run('MzI2NDE5NTY2ODkwODQ0MTYy.DCmifA.VDn19q6vu9mTzkL6bv34JUjfbeg')