import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
TOKEN = ""


client = discord.Client()
@client.event
async def on_message(message):

    if message.content.startswith("/메뉴"):
        Text = ""
        arr = ["한식", "중식", "양식", "일식", "치킨"]
        i = random.randint(1,5)
        Text = arr[i]

        print(Text.strip())
        embed = discord.Embed(
            title="메뉴!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)        
client.run(TOKEN)
