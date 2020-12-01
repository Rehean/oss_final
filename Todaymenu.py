from discord.ext import commands
import random

TOKEN = ""

client = commands.Bot(command_prefix='/')

@client.command(name='메뉴')
async def menu(ctx):
    menulist = ["한식","중식","일식","양식","치킨","떡볶이"]
    i = random.randint(0,6)

    await ctx.send(menulist[i])
    
client.run(TOKEN)
