import discord
from discord.ext import commands

from dotenv import load_dotenv
import os 

import random

# 봇의 접두사를 설정합니다. 여기서는 '!'을 접두사로 사용합니다.
intents = discord.Intents.default()  # 기본 인텐트 설정
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
token = os.environ.get('TOKEN')

# 봇이 준비되었을 때 호출되는 이벤트
@bot.event
async def on_ready():
    print(f'봇이 로그인되었습니다! ({bot.user})')

# '!hello' 커맨드를 처리하는 명령어
@bot.command()
async def 안녕(ctx):
    user_name = ctx.author.display_name
    await ctx.send(f'{user_name}님 안녕하세요!')

# '!add' 커맨드 (숫자 두 개를 더하는 예시)
@bot.command()
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f'결과: {result}')

@bot.command()
async def 가위바위보(ctx, choice: str):
    rps_choices = ["가위", "바위", "보"]
    if choice not in rps_choices:
        await ctx.send("올바른 선택이 아닙니다ㅠㅠ '가위', '바위', '보' 중 하나를 선택해 주세요!")
        return

    bot_choice = random.choice(rps_choices)
    result = None
    if choice == bot_choice:
        result = "비겼습니다! 다시 해요"
    elif (choice == "가위" and bot_choice == "보") or (choice == "바위" and bot_choice == "가위") or (choice == "보" and bot_choice == "바위"):
        result = f"{ctx.author.display_name}님이 이겼습니다!ㅠ"
    else:
        result = "제가 이겼습니다! 😎 쉽네요요"

    
    embed = discord.Embed(title="🎮 가위바위보 게임 🎮", color=discord.Color.pink())
    
    
    embed.add_field(name=f"{ctx.author.display_name}님의 선택", value=choice, inline=True)
    embed.add_field(name="저의 선택", value=bot_choice, inline=True)
    embed.add_field(name="결과", value=result, inline=False)

    

    await ctx.send(embed=embed)

# 봇 토큰을 사용하여 봇을 실행합니다.
bot.run(token)
