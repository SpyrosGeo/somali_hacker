#!/home/thatguy/Myrepos/somali_hacker/bin/python3
import discord
import os
from dotenv import load_dotenv
import requests
from random import choice,randint
load_dotenv()
TOKEN = os.getenv('TOKEN')
AI_API_KEY = os.getenv('AITOKEN')
channelId = os.getenv('CHANNELID')
myId = os.getenv('MYID')
koulisId = os.getenv('KOULISID')
URL = 'https://api.openai.com/v1/completions'
HEADERS = {

    "Authorization":f"Bearer {AI_API_KEY}",
    "Content-type":"application/json"
}
client = discord.Client(intents=discord.Intents.default())

insults = ['skase','boulwne','ti les re clown', 'eisai megalos laiclown','ontws twra??','pame space engineers?','mono wow','...']
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def spam_koulis():
    await client.wait_until_ready()
    channel = client.get_channel(int(channelId))
    await channel.send("Hello fellow hackers!")

@client.event
async def on_message(message):
    await client.wait_until_ready()
    general = client.get_channel(int(channelId))
    print('message',message.author.id)
    if message.author.id == int(koulisId):
            await general.send(choice(insults))
    #data = {
     #   "model":"text-davinci-003",
      #  "prompt":message.content,
       # "max_tokens":256
    #}
    #response = requests.post(URL,json=data,headers=HEADERS)
    #print("response",response.json())


client.run(TOKEN)
