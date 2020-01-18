import discord
#hellloo

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NjY3NzYzNDA4NjQ4Nzk4MjU4.XiNskA.pen8SNAY4HVF7UM3aXXANUXzWEk')