import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
import datetime
TOKEN = ""


client = discord.Client()
@client.event
async def on_message(message):

    if message.content.startswith("/한판더"):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send(message.channel, embed=discord.Embed(title="한판더!", color=discord.Color.blue()))
        else:
            await message.channel.send(message.channel, embed=discord.Embed(title="오늘은 그만", color=discord.Color.red()))        
client.run(TOKEN)
