import discord
import asyncio
import os
import sys
import json
import urllib.request
from discord import Member
from discord.est import commands
TOKEN = ""

#Papago API id/pw
n_id = "JLPMmTXOBkFMJ7rhAm1u"
n_secret = "WUECYHv2Wg"

client = discord.Client()
@client.event

def pst_translation(from_lan, to_lan, target_text):
    encText = urllib.parse.quote(target_text)
    data = "source=" + from_lan + "&target=" + to_lan + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",n_id)
    request.add_header("X-Naver-Client-Secret",n_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read().decode('utf-8')
        jDict = json.loads(response_body)
        result = jDict['message']['result']['translatedText']
        print(result)
        return result
    else:
        print("Error Code:" + rescode)

embed = discord.Embed(title = "How to use?", color = 0x00ff56)
embed.set_author(name = "OpenSource")
embed.add_field(name = "#help" , value = "사용법 안내", inline = False)
embed.add_field(name = "#번역 [도착언어] [목표 문장(출발 언어는 자동 감지)]" , value = "Ko - 한국어\nen - 영어\nja - 일본어\nzh-CN - 중국어 간체\nzh-TW - 중국어 번체\nvi - 베트남어\nde - 독일어\nth - 태국어\nru - 러시아어\nfr - 프랑스어\nit - 이탈리아어", inline = False)


client.run(TOKEN)
