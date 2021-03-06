import discord
import asyncio
from discord import Member
from discord.ext import commands

TOKEN = ""

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
        
        embed.add_field(name = '/안녕', value = '봇과 인사',inline = False)
        embed.add_field(name = '/주사위', value = '6면체 주사위 굴리기',inline = False)
        embed.add_field(name = '/이모티콘', value = '추천 이모티콘',inline = False)
        embed.add_field(name = '/복권', value = '복권번호 7개 추천',inline = False)
        embed.add_field(name = '/한판더', value = '게임 한판더 할까',inline = False)
        embed.add_field(name = '/시간', value = '현재시간',inline = False)
        embed.add_field(name = '/타이머 n', value = 'n만큼 타이머',inline = False)
        embed.add_field(name = '/메뉴', value = '메뉴추천',inline = False)
        embed.add_field(name = '/게임을 시작하자!', value = '봇과 가위바위보',inline = False)
        embed.add_field(name = "#help" , value = "사용법 안내", inline = False)
        embed.add_field(name = "#번역 [도착언어] [목표 문장(출발 언어는 자동 감지)]" , value = "Ko - 한국어\nen - 영어\nja - 일본어\nzh-CN - 중국어 간체\nzh-TW - 중국어 번체\nvi - 베트남어\nde - 독일어\nth - 태국어\nru - 러시아어\nfr - 프랑스어\nit - 이탈리아어", inline = False)

        
        await message.channel.send(channel,embed=embed)       
client.run(TOKEN)
