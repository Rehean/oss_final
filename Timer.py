import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
import time
import datetime
TOKEN = ""


client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith('/타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)

        else:
            print("땡")
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 종료'))

client.run(TOKEN)
