# -*- coding:utf-8 -*-

import discord, asyncio #디스코드 모듈과 보조 모듈인 asynico 모듈을 불러옵니다.

token = "NjgxOTg5ODkwODc1MDY0MzQx.XlW4Hw.l-ueJo2CeJFxPbkwY4f1Jtev8A4"
client = discord.Client()  #discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언 입니다.

@client.event
async def on_ready(): #봇이 준비가 되면 1회 실행하는 부분 입니다.
    #봇이 "반갑습니다" 를 플레이 하게 됩니다.
    #discord.Status.online에서 online 을 dnd로 바꾸면  "다른 용무 중", idle로 바꾸면 "자리비움"으로 바뀝니다.
    await client.change_presence(status=discord.Status.online, activity=discord.Game("제 이름을 불러주세요!!!"))
    print("I'm Ready!!!!!!!!!!!!!!") #"I'm Ready!!!!!!!!!!!!"를 출력합니다.
    print(client.user.name) #봇의 이름을 출력합니다.
    

@client.event
async def on_message(message): #메시지가 들어올 때 마다 가동되는 구문입니다.
    if message.author.bot: #채팅을 친 사람이 봇일 경우
        return None # 반응을 하지 않고 구문을 종료합니다.

    if message.content == "보미야": # ! 명령어 라는 채팅을 치면 
        await message.channel.send("'짖어'라고하면 짖어줘요.\n'산책 가자'라고 하면 제가 좋아 죽어요\n'가을아'라고 하면 제가 꼭 올게요!!\n무신사가 들어가고 싶으시면 '무신사' 라고 입력해주세요! \n절 그만 보고 싶으시면 '꺼져'라고 입력해주시면 이만 돌아갈게요") #메시지가 보내진 채널에 "--" 이라고 보냅니다.
        #await message.author.send("응답") #이렇게 하면 dm으로도 보낼 수 있습니다.
    elif message.content == "짖어":
        await message.channel.send("https://youtu.be/vnzxzewE230 ")
    elif message.content == "산책 가자":
        await message.channel.send("왈왈! 살랑살랑 컹컹 ")
    elif message.content == "봄이":
        await message.channel.send("'보미야' 를 입력하시면 사용 설명서가 나와요!")
    elif message.content == "가을아":
        await message.channel.send("https://cdn.discordapp.com/attachments/539064171103518733/682018388385464395/KakaoTalk_20200226_091702093.jpg")
    elif message.content == "무신사":
        await message.channel.send("https://www.musinsa.com/")
    elif message.content == ";; stop":
        await message.channel.send("저 주크박스 같은 새끼 그만 써")
    elif message.content == "꺼져":
        await message.channel.send("알겠노,, 미호")

client.run(token) # 아까넣은 토큰을 가져다가 봇을 실행하라는 부분입니다. 이 코드가 없으면 구문이 아무리 완벽해도 실행되지 않습니다.



