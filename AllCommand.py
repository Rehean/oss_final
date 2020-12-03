import discord
import asyncio
from discord import Member
from discord.ext import commands

TOKEN = "Nzc4MTY1NTM5MjU2MTM5ODI2.X7OBIg.GuOBhfeZTZfy-2sbxUomgL7mOSM"

client = discord.Client()
@client.event
async def on_message(message):

    if message.content.startswith("/명령어"):
        channel = message.channel
        embed = discord.Embed(
            title = '모든 명령어에요',
            description = '오타에 주의하세요',
            colour = discord.Colour.blue()
        )
        
        embed.add_field(name = '/명령', value = '상황',inline = False)
        
        await message.channel.send(channel,embed=embed)       
client.run(TOKEN)
