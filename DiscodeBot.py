import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
import time
import datetime
TOKEN = ""

client = discord.Client()

#Papago API id/pw
n_id = "JLPMmTXOBkFMJ7rhAm1u"
n_secret = "WUECYHv2Wg"

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




@client.event
async def on_message(message):

    if message.content.startswith('/안녕'):
        await message.channel.send("안녕하세요")


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
        await message.channel.send(channel,embed=embed)


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

    if message.content.startswith("/이모티콘"):
        emoticon = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "]
        Text = ""
        Text = Text + emoticon[random.randint(0,len(emoticon))]
        print(Text.strip())
        embed = discord.Embed(
            title="이모티콘!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)

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

     if message.content.startswith("/한판더"):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send(message.channel, embed=discord.Embed(title="한판더!", color=discord.Color.blue()))
        else:
            await message.channel.send(message.channel, embed=discord.Embed(title="오늘은 그만", color=discord.Color.red())) 

     if message.content.startswith("/시간"):
        Text = ""
        timestamp=datetime.datetime.utcnow()
        Text = Text + str(datetime.datetime.utcnow())
        print(Text.strip())
        embed = discord.Embed(
            title="시간!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(message.channel, embed=embed)

    if message.content.startswith('/타이머'):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]
        secint = int(Text)
        sec = secint
        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)
        else:
            print("땡")
            await message.channel.send(message.channel, embed=discord.Embed(description='타이머 종료'))

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
