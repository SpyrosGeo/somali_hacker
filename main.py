#!/home/thatguy/Myrepos/somali_hacker/bin/python3
import discord
import os
from dotenv import load_dotenv
from random import choice,randint
load_dotenv()

TOKEN = os.getenv('TOKEN')
client = discord.Client(intents=discord.Intents.default())
insults = ['skase','boulwne','ti les re clown', 'eisai megalos laiclown','ontws twra??','pame space engineers?','mono wow','...']
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def spam_koulis():
    await client.wait_until_ready()
    channel = client.get_channel(int(412366307015524359))
    await channel.send("Hello fellow hackers!")

@client.event
async def on_message(message):
    print('message',message.author.id)
    if message.author.id == 206177953120256000:
        chance = randint(1,100)
        print('chance',chance)
        if chance> 60:
            print(choice(insults))


client.run(TOKEN)
