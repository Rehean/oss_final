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

    if message.content.startswith('/안녕'):
        await message.channel.send("안녕하세요")
    
client.run(TOKEN)
