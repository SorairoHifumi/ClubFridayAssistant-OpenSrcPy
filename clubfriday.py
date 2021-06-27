from typing import AsyncGenerator
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
token = 'nope, not today' #Don't hack my bot pls


thisDay = datetime.date.today()
dotw = thisDay.isoweekday()


changelog1 = [" 1.0.1 The Beginning",'Add Schedule , Add +c',' 1.0.2 Changelog: Database Updated(6/1) , Teacher name added(6/3) , Added +nuay',' 1.0.3 Revamp Database from list to dict , Added +call , +changelog ','1.0.4 Improve +c ,Added +cindiv +repeatafterme']
sourceDict = {"cmdList":['+c [Class] [Period] \n+nuay \n+ping \n+db \n+cindiv [day of the week (Monday, Tuesday,...)] [class] [period]'],'dotweek':['Monday','Tuesday','Wednesday','Thursday','Friday']}
stupidWord = ["Are you sure that you have class today?","I'm pretty sure that today is weekend",""]
if dotw > 5:
    dayoftoday = 'Weekend'
else:
    dayoftoday = sourceDict['dotweek'][dotw - 1]

#Database
schedule = {
'1' : {
'Monday':['Animation' , 'Workshop' , 'Art Project' , 'Art Project' , 'Listening' , 'PE'],
'Tuesday':['Current Event' , 'Mathematics' , 'Thai' , 'Grammar' , 'Literature' , 'Economics'],
'Wednesday': ['Science' , 'Social' , 'Art' , 'Current Event' , 'Thai'],
'Thursday': ['Web Design' , 'Guidance' , 'Mathematics' , 'Social' , 'Elective' , 'Elective'],
'Friday': ['Writing' , 'WE' , 'Listening' , 'Literature' , 'Graphic Design' , 'Club']}
,
'3' : {
'Monday': ['Physic | Songkrod','Physic | Songkrod','Biology | Pakamon','Biology | Pakamon','Earth Science | Boonsong','Earth Science | Boonsong'],
'Tuesday': ['Thai | Sasinut','English Tuesday | Apinya','Applied Science | Tanongsak','Mathematics | Potchanee','Mathmatics for O-net | Atittaya','Chemistry | Phonchan'],
'Wednesday': ['Physic | Songkrod','Mathematics | Potchanee','English Wednesday | Apinya','Social | Athiporn','Thai | Sasinut','Animation | Monaphat'],
'Thursday': ['Meteorology | Boonsong','Mathematics for O-net | Atittaya','Chemistry | Phonchan','Chemistry | Phonchan','W.E. | Siriluk','Art | Teeranan','English Online | Apinya'],
'Friday': ['Social | Athiporn','English | Natamon','Guidance | Penphan','Health Education | Attaphorn','Mathematics | Potchanee','Club | ---']



}
}



client = commands.Bot(command_prefix='+')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Nuay's soul"))
    print('Bot is online')

@client.command()
async def db(ctx):
    await ctx.send('Database Available : 6/1 , 6/3')

@client.command()
async def c(ctx,cnum,period):
    icnum = int(cnum)
    iperiod = int(period)
    print(f'0:{icnum} {iperiod} {type(icnum)} {type(iperiod)}')
    print(f'1:{dayoftoday}')
    
    if iperiod >= 5:
        pernum = iperiod + 8
    else:
        pernum = iperiod + 7
    strpernum = str(pernum)
    if iperiod > 5 :
        pernum += 1
    if iperiod == 1 or iperiod == 2:
        timenum = ':20'
    elif iperiod >=3 or iperiod <= 5:
        timenum = ':30'
    elif iperiod >= 6:
        timenum = ':40'
    print(f'2:{timenum} {dotw}')
    if (dotw > 5):
        await ctx.send(random.choice(stupidWord) + "\nIf you think I'w wrong, try using +cindiv. More info at +listcmd")
    elif (iperiod >= 8 or iperiod < 1):
        await ctx.send('What?')
    else:
        print(f'finalize {cnum} {type(cnum)} {dayoftoday}')
        print(schedule['1']['Monday'])
        await ctx.send(f'{schedule[cnum][dayoftoday][iperiod - 1]} \nStarts at {strpernum}{timenum}')

    

@client.command()
async def clist(ctx,arg):
    for x in arg:
        await ctx.send(x)

@client.command()
async def dayoftheweek(ctx):
    await ctx.send(dotw)

#schedulecode used to be here now its at line 59

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
async def call(ctx,arg1,arg2):
    for x in schedule[arg1][arg2]:
        await ctx.send(x)   

@client.command()
async def changelog(ctx,arg):
    arg = int(arg)
    await ctx.send(changelog1[arg])

@client.command()
async def listcmd(ctx):
    for x in sourceDict['cmdList']:
        await ctx.send(x)

@client.command()
async def cindiv(ctx,arg2,arg1,arg3):
    arg4 = int(arg3)
    print(f'{arg1} {arg2} {type(arg2)} {arg3} {arg4}')
    await ctx.send(f'{schedule[arg1][arg2][arg4]}')
	
@client.command()
async def repeatafterme(ctx,arg):
  await ctx.send(arg)

@client.command()
async def version(ctx):
	await ctx.send('Running Version : v1.0.4 VSCode Self-Host')
client.run(token)