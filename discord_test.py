import discord
import time
from key import secret



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global start_time
    ## global rest_time
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!startstudy'):
        start_time = time.time()
        await message.channel.send("time started")

    if message.content.startswith('!stopstudy'):
        end_time = time.time()
        time_lapsed = end_time - start_time
        await message.channel.send(time_convert(time_lapsed))


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  '{:10}'.format('test')
  hours = mins // 60
  mins = mins % 60
  return ("You have studied for {0} hours, {1} minutes, and {2} seconds".format(int(hours),int(mins),int(sec)))



client.run(secret['discordToken'])
