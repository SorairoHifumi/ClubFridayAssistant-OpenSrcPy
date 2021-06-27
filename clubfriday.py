import discord
import os
from discord.ext import commands
from discord.voice_client import VoiceClient
from dotenv import load_dotenv
import datetime
import calendar
import time
import random

load_dotenv()
token = 'not today boi...' #Don't hack my bot pls


thisDay = datetime.date.today()
dotw = thisDay.isoweekday()



sourceDict = {"cmdList":['+c [Class] [Period] \n+nuay \n+ping \n+db \n+cindiv [day of the week (Monday, Tuesday,...)] [class] [period]'],'dotweek':['Monday','Tuesday','Wednesday','Thursday','Friday']}
stupidWord = ["Are you sure that you have class today?","I'm pretty sure that today is weekend"]
if dotw > 5:
    dayoftoday = 'Weekend'
else:
    dayoftoday = sourceDict['dotweek'][dotw - 1]

#Database
#---------------------There is a lot of schedule things here but for privacy I removed it from Open Source file--------------------------
#It defines urls, teachername and schedule

client = commands.Bot(command_prefix='+')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Nuay's soul"))
    print('Bot is online')

@client.command()
async def db(ctx):
    await ctx.send('Database Available : 6/1(Subject)\n6/3(Subject , Teacher)')

@client.command()
async def c(ctx,cnum,period):
    icnum = int(cnum)
    iperiod = int(period)
    print(f'0:{icnum} {iperiod} {type(icnum)} {type(iperiod)}')
    print(f'1:{dayoftoday}')
    tunk = False # Declare Teacher Unknown
    rec = 0#declare rec and ext
    ext = 0
    if icnum == 3: #if class have link add here
        hyperlink = urls[cnum][schedule[cnum][dayoftoday][iperiod - 1]]
    else :
        hyperlink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    print('end hyperlink init')
    # for double class
    #start classes
    if (icnum == 3): #3rd class
        if dotw == 1: #Monday
            if iperiod == 1 or iperiod == 3 or iperiod == 5:
                ext = 1
        if dotw == 4:#Thursday
            if iperiod == 3:
                ext = 1
    if (icnum == 1):
        if dotw == 1:
            if iperiod == 1:
                ext = 1
        if dotw == 3:
            if iperiod == 1:
                ext = 1
        if dotw == 4:
            if iperiod == 5:
                ext = 1        

    #end classes
    if (icnum == 3):
        if dotw == 1:
            if iperiod == 2 or iperiod == 4 or iperiod == 6:
                rec = 1
        if dotw == 4:
            if iperiod == 4:
                rec = 1
    if (icnum == 1):
        if dotw == 1:
            if iperiod == 3:
                rec = 1
        if dotw == 3:
            if iperiod == 2:
                rec = 1
        if dotw == 4:
            if iperiod == 6:
                rec = 1    
    print('end double class init')
    if (icnum == 3): #I write it like this in case of same teachers
        tsrc = '3' #Teacher Source
    elif (icnum == 1):
        tsrc = '1' 
        
        #Add it here with elif
    else:
        tunk = True
    if iperiod >= 5:
        startTime = iperiod + 8#in case after lunch
    else:
        startTime = iperiod + 7# get hour of start time
    
    endTime = startTime + 1 + ext # extend end time or reduce start time
    startTime = startTime - rec
    print('end time init')
    if iperiod > 5 :#Determine minutes
        startTime += 1
    if iperiod == 1 or iperiod == 2:
        timenum = ':20'
    elif iperiod >=3 or iperiod <= 5:
        timenum = ':30'
    elif iperiod >= 6:
        timenum = ':40'
    print(f'2:{timenum} {dotw}') 

    if tunk == True:
        teacher_name = 'Unknown'
    if dotw > 5:
        teacher_name = 'Unknown'
    else:
        teacher_name = teachername[cnum][schedule[cnum][dayoftoday][iperiod - 1]]
#value init done
    if (dotw > 5):
        await ctx.send(random.choice(stupidWord) + "\nIf you think I'w wrong, try using +cindiv. More info at +listcmd")
    elif (iperiod >= 8 or iperiod < 1):
        await ctx.send('What?')
    else:
        print(f'finalize {cnum} {type(cnum)} {dayoftoday}') # For troubleshooting
        print(schedule['1']['Monday'])
        embed = discord.Embed(title = f'{schedule[cnum][dayoftoday][iperiod - 1]}', description = f'Teacher : {teacher_name}\nDuration : {startTime}{timenum} - {endTime}{timenum}',url=hyperlink,color=0x669900)
        embed.set_footer(text=f'6/{cnum} {dayoftoday} #{iperiod}')
        await ctx.send(embed=embed)
        #await ctx.send(f'{schedule[cnum][dayoftoday][iperiod - 1]} \nStarts at {startTime}{timenum}') - old one

    

@client.command()
async def clist(ctx,arg):
    for x in arg:
        await ctx.send(x)

@client.command()
async def dayoftheweek(ctx):
    await ctx.send(dotw)



@client.command()
async def easteregg(ctx):
    await ctx.send('yes.')

@client.command()
async def ping(ctx):
	await ctx.send(f'Latency : {round(client.latency * 1000)} ms')

@client.command()
async def getTimeNow(ctx):
    
    await ctx.send(datetime.datetime.now())

	
@client.command()
async def nuay(ctx):
	await ctx.send('nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay')

@client.command()
async def call(ctx,dayofrequest,cnum):
    icnum = int(cnum)
    i = 0
    for y in schedule[cnum][dayofrequest]:
        
        if (icnum == 3): #I write it like this in case of same teachers
            tsrc = '3' #Teacher Source
            teacher_name = teachername[cnum][schedule[cnum][dayofrequest][i]]
        elif (icnum == 1):
            tsrc = '1' 
            teacher_name = teachername[cnum][schedule[cnum][dayofrequest][i]]
        
        #Add it here with elif
        else:
            teacher_name = 'Unknown'
        if icnum == 3: #if class have link add here
            hyperlink = urls[cnum][schedule[cnum][dayofrequest][i]]
        else :
            hyperlink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

        
        embed = discord.Embed(title = f'{schedule[cnum][dayofrequest][i]}', description = f'Teacher : {teacher_name}',url=hyperlink,color=0x669900)
        embed.set_footer(text=f'6/{cnum} {dayofrequest} #{i + 1}')
        await ctx.send(embed=embed)
        i += 1

@client.command()
async def listcmd(ctx):
    for x in sourceDict['cmdList']:
        await ctx.send(x)

@client.command()
async def cindiv(ctx,arg2,arg1,arg3):
    arg4 = int(arg3)
    print(f'{arg1} {arg2} {type(arg2)} {arg3} {arg4}')
    await ctx.send(f'{schedule[arg1][arg2][arg4 - 1]}')
	
@client.command()
async def repeatafterme(ctx,arg):
  await ctx.send(arg)

@client.command()
async def version(ctx):
	await ctx.send('Running Version : v1.1.0 VSCode')
client.run(token)
