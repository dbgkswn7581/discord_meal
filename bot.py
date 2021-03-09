from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request
import discord
from discord.ext import commands
import os
import time

# Client Id : 816671240293974066
# Client Token : 

client = commands.Bot(command_prefix='#')



def get_time():
    global now, timon, tiday, tihour
    
    now = time.localtime() 
    timon = now.tm_mon
    tiday = now.tm_mday
    tihour = now.tm_hour
    tihour = tihour + 9

    if tihour >= 24:
        tihour = tihour - 24
        tiday += 1
        if timon == 3:
            if tiday >= 32:
                tiday = 1
                timon += 1
        elif timon ==  4 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  5 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  6 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  7 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  8 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  9 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  10 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  11 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  12 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  1 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  2 :
            if tiday >=  29 :
                tiday = 1
                timon += 1


#오늘 날짜 
def set_today():
    global today
    get_time()
#     today_year = str(datetime.today().year)
#     today_month = str(datetime.today().month)
#     today_day = str(datetime.today().day)
    today_year = str(int(now.tm_year))
    today_month = timon
    today_day = tiday


    if len(str(today_month)) == 1:
        today_month = '0' + str(today_month)
    else:
        today_month = str(today_month)

    if len(str(today_day)) == 1:
        today_day = '0' + str(today_day)
    else:
        today_day = str(today_day)

    today = today_year+today_month+today_day

    print("today is ", end='')
    print(today)
#내일 날짜
def set_tomorrow():
    global tomorrow

    set_today()

    tomorrow = str(int(today) + 1)

    # tom_month = int(tomorrow[4:6])
    # tom_day = int(tomorrow[6:])

    # if tom_month == 3:
    #     if tom_day >= 32:
    #         tomorrow = str("20210401")
    # elif tom_month ==  4 :
    #     if tom_day >=  31 :
    #         tomorrow = str("20210501")
    # elif tom_month ==  5 :
    #     if tom_day >=  32 :
    #         tomorrow = str("20210601")
    # elif tom_month ==  6 :
    #     if tom_day >=  31 :
    #         tomorrow = str("20210701")
    # elif tom_month ==  7 :
    #     if tom_day >=  32 :
    #         tomorrow = str("20210801")
    # elif tom_month ==  8 :
    #     if tom_day >=  32 :
    #         tomorrow = str("20210901")
    # elif tom_month ==  9 :
    #     if tom_day >=  31 :
    #         tomorrow = str("20211001")
    # elif tom_month ==  10 :
    #     if tom_day >=  32 :
    #         tomorrow = str("20211101")
    # elif tom_month ==  11 :
    #     if tom_day >=  31 :
    #         tomorrow = str("20211201")
    # elif tom_month ==  12 :
    #     if tom_day >=  32 :
    #         tomorrow = str("20220101")
    # elif tom_month ==  1 :
    #     if tom_day >=  32 :
    #         tomorrow = str("20220201")
    # elif tom_month ==  2 :
    #     if tom_day >=  29 :
    #         tomorrow = str('20220301')

    print("tomorrow is ", end='')
    print(tomorrow)
    
#알레르기 성분 번호 삭제    
def num_remove(food):
    food = str(food).replace("10.", "")
    food = str(food).replace("11.", "")
    food = str(food).replace("12.", "")
    food = str(food).replace("13.", "")
    food = str(food).replace("14.", "")
    food = str(food).replace("15.", "")
    food = str(food).replace("16.", "")
    food = str(food).replace("17.", "")
    food = str(food).replace("18.", "")
    food = str(food).replace("1.", "")
    food = str(food).replace("2.", "")
    food = str(food).replace("3.", "")
    food = str(food).replace("4.", "")
    food = str(food).replace("5.", "")
    food = str(food).replace("6.", "")
    food = str(food).replace("7.", "")
    food = str(food).replace("8.", "")
    food = str(food).replace("9.", "")

    return food
#알레르기 성분 번호 삭제    
def remove_num(meal):
    List = list(meal)
    Real = list()

    for i in List:
        a = num_remove(i)
        Real.append(a)
        
    return Real

#점심 급식 리스트로 받아오기
def get_meal_lunch(day):
    try:
        url = "https://school.jbedu.kr/jeolla-h/M01070403/list?ymd=" + day

        soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')

        meals = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li:nth-child(2) > dl > dd.tch-lnc > ul').get_text().split()
        meals = remove_num(meals)    

        return meals
    except:
        print("중식 정보가 없습니다.")

        return "Nope"


#저녁 급식 리스트로 받아오기
def get_meal_dinner(day):
    try:
        url = "https://school.jbedu.kr/jeolla-h/M01070403/list?ymd=" + day

        soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')

        meals = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li:nth-child(3) > dl > dd.tch-lnc > ul').get_text().split()
        meals = remove_num(meals)    

        return meals
    except:
        print("석식 정보가 없습니다.")

        return "Nope"

#에러 발생
class makeError(Exception):
    def __init__(self):
        super().__init__('급식 정보가 없습니다.')


def set_meal_today():
    global today_lunch, today_dinner

    today_lunch = get_meal_lunch(today)
    today_dinner = get_meal_dinner(today)

def set_meal_tomorrow():
    global tomorrow_lunch, tomorrow_dinner

    tomorrow_lunch = get_meal_lunch(tomorrow)
    tomorrow_dinner = get_meal_dinner(tomorrow)



#================================================================================================================================================

@client.event
async def on_ready():
    global today_lunch, today_dinner, tomorrow_lunch, tomorrow_dinner

    # print(client.user.id)
    print("ready")
    game = discord.Game("전라고 급식 서비스 제공")
    await client.change_presence(status = discord.Status.online, activity = game)



    



def list_to_str(list):
    k = str()
    for i in list:
        k += i + '\n'
    
    return k

@client.command(name="급식")
async def meal(ctx, *text):

    txt = ''
    for tmp in text:
        txt += tmp
        txt += ' '


    day = "2021" + txt
    day = day.replace(" ", "")

    if len(day) != 8:
        embed = discord.Embed(title = "Error",
        description = "잘못된 날짜 입니다.", color = discord.Color.dark_red()
        )
        await ctx.send(embed=embed)
        raise makeError
 
        
    


    day_lunch = get_meal_lunch(day)
    day_dinner = get_meal_dinner(day)

    if day_lunch == "Nope" and day_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif day_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif day_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(day[:4], day[5:6], day[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(day_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(day_dinner), inline=False)

    await ctx.send(embed=embed)

@client.command(name="ㄱㅅ")
async def meal(ctx, *text):

    txt = ''
    for tmp in text:
        txt += tmp
        txt += ' '


    day = "2021" + txt
    day = day.replace(" ", "")

    if len(day) != 8:
        embed = discord.Embed(title = "Error",
        description = "잘못된 날짜 입니다.", color = discord.Color.dark_red()
        )
        await ctx.send(embed=embed)
        raise makeError
 
        
    


    day_lunch = get_meal_lunch(day)
    day_dinner = get_meal_dinner(day)

    if day_lunch == "Nope" and day_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif day_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif day_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(day[:4], day[5:6], day[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(day_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(day_dinner), inline=False)

    await ctx.send(embed=embed)

@client.command(name="rt")
async def meal(ctx, *text):

    txt = ''
    for tmp in text:
        txt += tmp
        txt += ' '


    day = "2021" + txt
    day = day.replace(" ", "")

    if len(day) != 8:
        embed = discord.Embed(title = "Error",
        description = "잘못된 날짜 입니다.", color = discord.Color.dark_red()
        )
        await ctx.send(embed=embed)
        raise makeError
 
        
    


    day_lunch = get_meal_lunch(day)
    day_dinner = get_meal_dinner(day)

    if day_lunch == "Nope" and day_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif day_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif day_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(day[:4], day[5:6], day[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(day_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(day_dinner), inline=False)

    await ctx.send(embed=embed)

    
@client.command(name="오늘")
async def meal(ctx):
    set_today()
    set_meal_today()

    if today_lunch == "Nope" and today_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif today_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif today_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(today[:4], today[5:6], today[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(today_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(today_dinner), inline=False)

    await ctx.send(embed=embed)

@client.command(name="ㅇㄴ")
async def meal(ctx):
    set_today()
    set_meal_today()

    if today_lunch == "Nope" and today_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif today_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif today_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(today[:4], today[5:6], today[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(today_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(today_dinner), inline=False)

    await ctx.send(embed=embed)

@client.command(name="ds")
async def meal(ctx):
    set_today()
    set_meal_today()

    if today_lunch == "Nope" and today_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif today_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif today_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(today[:4], today[5:6], today[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(today_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(today_dinner), inline=False)

    await ctx.send(embed=embed)
    
@client.command(name="내일")
async def meal(ctx):
    set_tomorrow()
    set_meal_tomorrow()

    if tomorrow_lunch == "Nope" and tomorrow_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif tomorrow_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif tomorrow_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(tomorrow[:4], tomorrow[5:6], tomorrow[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(tomorrow_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(tomorrow_dinner), inline=False)

    await ctx.send(embed=embed)
    
@client.command(name="ㄴㅇ")
async def meal(ctx):
    set_tomorrow()
    set_meal_tomorrow()

    if tomorrow_lunch == "Nope" and tomorrow_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif tomorrow_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif tomorrow_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(tomorrow[:4], tomorrow[5:6], tomorrow[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(tomorrow_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(tomorrow_dinner), inline=False)

    await ctx.send(embed=embed)
    
@client.command(name="sd")
async def meal(ctx):
    set_tomorrow()
    set_meal_tomorrow()

    if tomorrow_lunch == "Nope" and tomorrow_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif tomorrow_dinner == "Nope":
        embed = discord.Embed(title = "Error",
        description = "저녁 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError
    elif tomorrow_lunch == "Nope":
        embed = discord.Embed(title = "Error",
        description = "점심 급식 정보가 없습니다.", color = discord.Color.red()
        )
        await ctx.send(embed=embed)
        raise makeError

    embed = discord.Embed(title = "전라고등학교 급식",
    description="날짜 : %s년 %s월 %s일" %(tomorrow[:4], tomorrow[5:6], tomorrow[6:]), color=discord.Color.blue())

    embed.add_field(name="중식", value=list_to_str(tomorrow_lunch), inline=False)
    embed.add_field(name="석식", value=list_to_str(tomorrow_dinner), inline=False)

    await ctx.send(embed=embed)

@client.command(name="check")
async def meal(ctx):
    set_today()
    set_tomorrow()
    
    
    embed = discord.Embed(title = "Check",
    description = "today 변수 값 : %s\ntomorrow 변수 값 : %s" %(today, tomorrow), color = discord.Color.green()
    )
    
    
    await ctx.send(embed=embed)

@client.command(name="time")
async def meal(ctx):
    now = time.localtime() 
    timon = now.tm_mon
    tiday = now.tm_mday
    tihour = now.tm_hour
    tihour = tihour + 9
    if tihour >= 24:
        tihour = tihour - 24
        tiday += 1
        if timon == 3:
            if tiday >= 32:
                tiday = 1
                timon += 1
        elif timon ==  4 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  5 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  6 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  7 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  8 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  9 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  10 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  11 :
            if tiday >=  31 :
                tiday = 1
                timon += 1
        elif timon ==  12 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  1 :
            if tiday >=  32 :
                tiday = 1
                timon += 1
        elif timon ==  2 :
            if tiday >=  29 :
                tiday = 1
                timon += 1

        
    embed = discord.Embed(title = "Time",
    description = "%04d/%02d/%02d %02d:%02d:%02d" %(now.tm_year, timon, tiday, tihour, now.tm_min, now.tm_sec), color = discord.Color.orange()
    )
    await ctx.send(embed=embed)

@client.command(name="도움말")
async def meal(ctx):
    embed = discord.Embed(title = "명령어",
    description = "전라고등학교 급식 서비스 봇 명령어" , color = discord.Color.purple()
    )

    embed.add_field(name="#오늘", value="오늘 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#내일", value="내일 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#급식 MMDD", value="MM월 DD일의 급식을 확인합니다.\nex) #급식 0305 → 3월 5일의 급식을 확인합니다.", inline=False)
    

    await ctx.send(embed=embed)

@client.command(name="명령어")
async def meal(ctx):
    embed = discord.Embed(title = "명령어",
    description = "전라고등학교 급식 서비스 봇 명령어" , color = discord.Color.purple()
    )

    embed.add_field(name="#오늘", value="오늘 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#내일", value="내일 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#급식 MMDD", value="MM월 DD일의 급식을 확인합니다.\nex) #급식 0305 → 3월 5일의 급식을 확인합니다.", inline=False)
    

    await ctx.send(embed=embed)

client.remove_command("help")
@client.command(name="help")
async def meal(ctx):
    embed = discord.Embed(title = "명령어",
    description = "전라고등학교 급식 서비스 봇 명령어" , color = discord.Color.purple()
    )

    embed.add_field(name="#오늘", value="오늘 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#내일", value="내일 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#급식 MMDD", value="MM월 DD일의 급식을 확인합니다.\nex) #급식 0305 → 3월 5일의 급식을 확인합니다.", inline=False)
    

    await ctx.send(embed=embed)

@client.command(name="?")
async def meal(ctx):
    embed = discord.Embed(title = "명령어",
    description = "전라고등학교 급식 서비스 봇 명령어" , color = discord.Color.purple()
    )

    embed.add_field(name="#오늘", value="오늘 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#내일", value="내일 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#급식 MMDD", value="MM월 DD일의 급식을 확인합니다.\nex) #급식 0305 → 3월 5일의 급식을 확인합니다.", inline=False)
    

    await ctx.send(embed=embed)
    
@client.command(name="command")
async def meal(ctx):
    embed = discord.Embed(title = "명령어",
    description = "전라고등학교 급식 서비스 봇 명령어" , color = discord.Color.purple()
    )

    embed.add_field(name="#오늘", value="오늘 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#내일", value="내일 날짜의 급식을 확인합니다.", inline=False)
    embed.add_field(name="#급식 MMDD", value="MM월 DD일의 급식을 확인합니다.\nex) #급식 0305 → 3월 5일의 급식을 확인합니다.", inline=False)
    

    await ctx.send(embed=embed)

client.run(os.environ['token'])
