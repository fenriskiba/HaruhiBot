from modules.settings import register


@register
async def hello(client, message):
    await client.send_message(message.channel, 'Hello World')


@register
async def echo(client, message):
    msg = message.content.split(' ', 1)[1]
    await client.send_message(message.channel, msg)
    await client.delete_message(message)


# TODO: Create Pray/Fortune Functionality
