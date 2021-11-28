#discord specific imports
import discord
from discord.ext import commands
from discord.utils import get
from discord import Webhook, RequestsWebhookAdapter

#other imports
import time as t
import random as ran
import json

#file specific imports
from reqconcept1 import getreddit
from owoify.owoify import owoify
from emojifier import Emojifier
from splitconcept1 import split
from keepalive import dorevive

#discord objects/variables
client = commands.Bot(command_prefix='.')

#discord IDs
poleskiID=416327111922679810
crimsonID=479663186144919556
shushbotid=888118494695153694
benID=806853826123530240
andreiID=894264180583067700



#other vars
global emojikeyword, trustedemojilimit,emojilimit
token=('OTExNjAwMjM3MDUzODcwMDgw.YZjv4Q.YDhN7FBi03j40SKt5qPV1GFo7xg')
emojikeyword=('emoji')




#functions
def emojify(textinput):
    with open('emoji.json','r',encoding="utf8") as f:
        mapping=json.load(f)
    emojiobj = Emojifier.of_custom_mappings(mapping)
    return emojiobj.generate_emojipasta(text=textinput)

def send(message,channel):
    client.loop.create_task(channel.send(message))





#events

@client.event
async def on_ready():
    print('Hello World')

@client.event
async def on_message(message):

    #vars to not depend on message.
    messageuse=str(message.content)
    author=message.author
    authorid=message.author.id
    channelobj=message.channel
    serverobj=message.guild
    messagearray= await channelobj.history(limit=2).flatten()
    previousmessage=str(messagearray[1].content)



    if message.content.startswith(emojikeyword) and authorid != 911600237053870080:
        trustedemojilimit=200
        emojilimit=10
        for roles in author.roles:
          if roles.id==847202104171167820:
            emojilimit=trustedemojilimit
          #print(roles)
        if messageuse == (emojikeyword):  # if message is to only be emoji'd once
            await channelobj.send((emojify(previousmessage)))
            # send('hello',channelobj)
        else:  # if more than once
            messageuse = list(messageuse)
            for i in range(len(emojikeyword) + 1):
                messageuse.pop(0)
            messageuse = ''.join(messageuse)
            #try:
            itr = int(messageuse)
            if itr <= emojilimit:
                emojifiedmessage = (previousmessage)
                await channelobj.send('0%')
                msg = await channelobj.history(limit=2).flatten()
                progressmessage = msg[0]

                for i in range(itr):
                    emojifiedmessage = emojify(emojifiedmessage)
                    percentage = (i / itr) * 100
                    if round(percentage)%10==0:
                        await progressmessage.edit(content=(str(round(percentage)) + ('%')))

              # if len(emojifiedmessage)>2000:
              #     await channelobj.send('over send limit')
              # else:
            else:
              send('fuck off im not doing that', channelobj)
            
            try:
                
              await progressmessage.edit(content=(str(100) + ('%')))
              sendable = split(emojifiedmessage, 2000)
              for i in range(len(sendable)):
                send(sendable[i], channelobj)
              await progressmessage.delete()
            except:
              pass    

            #except:
              #send('bad format, use:\nemoji *1-100*', channelobj)
        try:
            print(str(author), '(' + (str(author.display_name)) + ")", 'used emoji', itr, 'command in',
                  str(serverobj.name))
        except:
            print(str(author), '(' + (str(author.display_name)) + ")", 'failed using emoji command in',
                  str(serverobj.name))

dorevive()
client.run(token)