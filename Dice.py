import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
TOKEN = ""


client = discord.Client()
@client.event
async def on_message(message):

    if message.content.startswith("/주사위"):
        Text = ""
        Text = Text + str(random.randint(1,6))

        print(Text.strip())
        embed = discord.Embed(
            title="주사위!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)        
client.run(TOKEN)
