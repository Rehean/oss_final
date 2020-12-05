import discord
import asyncio
from discord import Member
from discord.ext import commands
TOKEN = ""


client = discord.Client()
@client.event
async def on_message(message):
        Text = ""
    """ adding codes to string here"""

        print(Text.strip())
        embed = discord.Embed(
            title="",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)        
client.run(TOKEN)
