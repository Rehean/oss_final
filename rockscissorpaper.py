import discord
import asyncio
import os
import sys
from discord import Member
from discord.est import commands
TOKEN = ""


client = discord.Client()
@client.event

async def game(message):
        if message.content.startswith('/게임을 시작하자!'):
                rsp = ["가위","바위","보"]
                embed = discord.Embed(title="가위바위보",description="5초내로 (가위/바위/보)를 써주세요!", color=0x00aaaa)
                channel = message.channel
                msg1 = await message.channel.send(embed=embed)
                def check(m):
                        return m.author == message.author and m.channel == channel
                try:
                        msg2 = await client.wait_for('message', timeout=5.0, check=check)
                except asyncio.TimeoutError:
                        await msg1.delete()
                        embed = discord.Embed(title="가위바위보",description="왜 안내세요? 갈래요!", color=0x00aaaa)
                        await message.channel.send(embed=embed)
                        return
                else:
                        await msg1.delete()
                        bot_rsp = str(random.choice(rsp))
                        user_rsp  = str(msg2.content)
                        answer = ""
                        if bot_rsp == user_rsp:
                                answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 냈어요!\n" + "비겼습니다!"
                        elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (bot_rsp == "바위" and user_rsp == "보"):
                                answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 내셨내요.\n" + "당신의 승리입니다!"
                        elif (bot_rsp == "바위" and user_rsp == "가위") or (bot_rsp == "가위" and user_rsp == "보") or (bot_rsp == "보" and user_rsp == "바위"):
                                answer = "저는 " + bot_rsp + "를 냈고, 당신은 " + user_rsp + "를 내셨내요.\n" + "흣흠 제가 이겼어요!"
                        else:
                                answer == "정확하게 다시 입력해주세요!"
                                await message.channel.send(embed=embed)
                                return
                        embed = discord.Embed(title="가위바위보",description=answer, color=0x00aaaa)
                        await message.channel.send(embed=embed)
client.run(TOKEN)
