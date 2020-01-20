import discord
import time
from key import secret
from pprint import pprint
from discord.ext import commands, tasks
import random
import asyncio
import datetime
import time

import giphy_client
from giphy_client.rest import ApiException

bot = commands.Bot(command_prefix='!')
#client = discord.Client()
giphy_token = 'tuoXTtCcBMfEvyGxjac1IiSRxTzSvLF3'

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'motivation')
async def motivationCommand(ctx):
    #Create an instance of the API class
        api_instance = giphy_client.DefaultApi()

        try:
            api_response = api_instance.gifs_search_get(giphy_token, "motivation", limit=50, rating='g')
            pprint(api_response)
            lst = list(api_response.data)
            gif = random.choices(lst)
            await ctx.send(gif[0].url)

        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)

@bot.command(name = 'cute')
async def cuteCommand(ctx):
    #Create an instance of the API class
        api_instance = giphy_client.DefaultApi()

        try:
            api_response = api_instance.gifs_search_get(giphy_token, "cute", limit=50, rating='g')
            pprint(api_response)
            lst = list(api_response.data)
            gif = random.choices(lst)
            await ctx.send(gif[0].url)

        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)

@bot.command(name = 'quote')
async def quoteCommand(ctx):
    
    file = "quotes.txt"
    try:
        q = open("quotes.txt", "r", encoding="utf-8")
        
        quotes = []
        for i in q:
            if i.strip():
                quotes.append(i.split(". ", 1).pop())

        print(*quotes)
        send = quotes[random.randint(1, len(quotes))]
        print(send)
        await ctx.send(send)
    except IOError:
        print("you suck")

@bot.command(name= 'studystrats')
async def studyStratsCommand(ctx):
    await ctx.send("Hi, which study strategy would you like to use today?")

if message.content.startswith("$procrastinate"):

        try:
            file = open("emoji.txt", "r", encoding="utf-8")
        except:
            print("you suck")

        e = []
        for i in file:
            if i.strip("\n"):
                e.append(i)


        send = e[random.randint(0, len(e))].strip("\n")
        print(random.choice(list))
        await message.add_reaction(random.choice(list))

        try:
            await message.add_reaction(unicode)
            #await message.add_reaction("\U0001F948")

        except:
            print(send, end="")
            
bot.run(secret['discordToken'])
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!hello'):
#         await message.channel.send('Hello!')

#     if message.content.startswith("!motivation"):

#         # Create an instance of the API class
#         api_instance = giphy_client.DefaultApi()

#         try:
#             api_response = api_instance.gifs_search_get(giphy_token, "motivation", limit=50, rating='g')
#             pprint(api_response)
#             lst = list(api_response.data)
#             gif = random.choices(lst)
#             await message.channel.send(gif[0].url)

#         except ApiException as e:
#             print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)

#     if message.content.startswith("!cute"):

#         # Create an instance of the API class
#         api_instance = giphy_client.DefaultApi()

#         try:
#             api_response = api_instance.gifs_search_get(giphy_token, "cute", limit=50, rating='g')
#             pprint(api_response)
#             lst = list(api_response.data)
#             gif = random.choices(lst)
#             await message.channel.send(gif[0].url)

#         except ApiException as e:
#             print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)

#     if message.content.startswith("!quote"):

#         file = "quotes.txt"

#         try:
#             q = open(file, "r", encoding="utf-8")
#         except IOError:
#             print("you suck")

#         quotes = []
#         for i in q:
#             if i.strip():
#                 quotes.append(i.split(". ", 1).pop())

#         print(*quotes)
#         send = quotes[random.randint(1, len(quotes))]
#         print(send)
#         await message.channel.send(send)
    
#     if message.content.startswith("!studystrats"):
#         await message.author.send("Hi, which study strategy would you like to use today?")
#     if str(message.channel).__contains__("Direct Message"):
#         print(message.channel)
#         if message.content.startswith("!pomodoro"):
#             period = 1
#             while not message.content.startswith("!taskdone"):
#                 if period%4 ==0:
#                     #workCounter = 25*60
#                     workCounter = 10
#                     while workCounter > 0:
#                         time.sleep(1)
#                         workCounter -= 1
#                     await message.author.send("Congrats! You finished your work period!\nTime for a longer 20 minute break")
#                     #breakCounter = 20*60
#                     breakCounter = 5
#                     while breakCounter > 0:
#                         time.sleep(1)
#                         breakCounter -= 1
#                     await message.author.send("Your break is complete, time to get back to work!")
#                     period +=1
#                 else:
#                     #workCounter = 25*60
#                     workCounter = 10
#                     while workCounter > 0:
#                         time.sleep(1)
#                         workCounter -= 1
#                     await message.author.send("Congrats! You finished your work period!\nTime for a quick 5 minute break")
#                     #breakCounter = 5*60
#                     breakCounter = 5
#                     while breakCounter > 0:
#                         time.sleep(1)
#                         breakCounter -= 1
#                     await message.author.send("Your break is complete, time to get back to work!")
#                     period +=1
#             await message.author.send("Good job! You have successfully used pomodoro to finish your task!")
#         #elif message.content.startswith("!flowtime"):
#         #elif message.content.startswith("!chain"):
            

#client.run(secret['discordToken'])
