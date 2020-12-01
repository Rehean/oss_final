from discord.ext import commands
import random

TOKEN = ""

client = commands.Bot(command_prefix='/')

@client.command(name='주사위')
async def roll(ctx, number):
    await ctx.send("주사위 굴리는 중")
    await ctx.send("...")
    await ctx.send("...")
    await ctx.send("...")
    await ctx.send("...")
    await ctx.send(f'주사위를 굴려 {random.randint(1,int(number))}이(가) 나왔습니다. (1-{number})')

@roll.error
async def roll_error(ctx, error):
    await ctx.send("명령어 오류. \" /주사위 숫자(1이상) \"")
    
client.run(TOKEN)
