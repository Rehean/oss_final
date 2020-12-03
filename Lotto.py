import discord
import asyncio
import random
from discord import Member
from discord.ext import commands

TOKEN = ""

client = discord.Client()
@client.event
async def on_message(message):

    if message.content.startswith("/복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7] 
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  
                        numberText = number[i]
                        print("이전 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("현재 : " + str(numberText))
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print("이전 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("현재 : " + str(numberText))
                            if number[i] == number[i2]: 
                                numberText = number[i]
                                print("이전 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("현재 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)        
client.run(TOKEN)
