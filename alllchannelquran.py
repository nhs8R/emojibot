import discord
from discord.ext import commands
from splitconcept1 import split
client=commands.Bot(command_prefix='s')
@client.event
async def on_ready():
    print('hello world')
@client.event
async def on_message(message):
    if ('zzzzzzzzzzz') in message.content:
        with open('quran.txt') as f:
            english=str(f.readlines())
        sendable=split(english,2000)
        allchannels=[]
        for channels in message.guild.channels:
            allchannels.append(channels)
        print(allchannels)
        for i in range(len(sendable)):                
            for index in range(len(allchannels)):
                await allchannels[index].send(sendable[i])
client.run('OTExNTgwMDQ4NTg5NDcxNzU0.YZjdEw.ltaaZuk7Hd7WEbk1XphSN9LTSsw')
