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

    if message.content.startswith("/시간"):
        Text = ""
        timestamp=datetime.datetime.utcnow()
        Text = Text + str(datetime.datetime.utcnow())
        print(Text.strip())
        embed = discord.Embed(
            title="시간!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)        
client.run(TOKEN)
