import discord
from discord.ext import commands
import datetime
import calendar
import time
import asyncio
import random

thisDay = datetime.date.today()
dotw = thisDay.isoweekday()

sourceDict = {"cmdList":['+c [Class] [Period] \n+nuay \n+ping \n+db \n+cindiv [day of the week (Monday, Tuesday,...)] [class] [period]'],'dotweek':['Monday','Tuesday','Wednesday','Thursday','Friday']}
stupidWord = ["Are you sure that you have class today?","I'm pretty sure that today is weekend"]
if dotw > 5:
    dayoftoday = 'Weekend'
else:
    dayoftoday = sourceDict['dotweek'][dotw - 1]

dotwColor = {
'Monday' : 0xffff8a,
'Tuesday' :0xf3b0c3,
'Wednesday' : 0xadff2f,
'Thursday' : 0xFFC8A2,
'Friday' :  0xABDEE6


}
#Database
#When update, also update at #####################################
#Dict here define urls,teachername,schedule

async def getCInfo(ctx,cnum,period):
        
        
        if dotw > 5:
            dayoftoday = 'Weekend'
        else:
            dayoftoday = sourceDict['dotweek'][dotw - 1]
        icnum = int(cnum)
        iperiod = int(period)
        color = dotwColor[dayoftoday]
        
        try:   
            print(f'0:{icnum} {iperiod} {type(icnum)} {type(iperiod)}')
            print(f'1:{dayoftoday}')
            tunk = False # Declare Teacher Unknown
            rec = 0#declare rec and ext
            ext = 0
            if icnum == 3 or icnum == 1: #if class have link add here#############################################################Add if link exist
                hyperlink = urls[cnum][schedule[cnum][dayoftoday][iperiod - 1]]
            else :
                hyperlink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            print('end hyperlink init')
            # for double class
            #start classes#############################################################################Add if schedule have double class
            if (icnum == 3): #3rd class
                if dotw == 1: #Monday
                    if iperiod == 1 or iperiod == 3 or iperiod == 5:
                        ext = 1
                if dotw == 4:#Thursday
                    if iperiod == 3:
                        ext = 1
            if (icnum == 1):
                if dotw == 1:
                    if iperiod == 3:
                        ext = 1
                if dotw == 3:
                    if iperiod == 1:
                        ext = 1
                if dotw == 4:
                    if iperiod == 5:
                        ext = 1        
            if (icnum == 5):
                if dotw == 2:
                    if iperiod == 1 or iperiod == 3 or iperiod == 5:
                        ext = 1
                if dotw == 5:
                    if iperiod == 1:
                        ext = 1
            if (icnum == 6):
                if dotw == 2:
                    if iperiod == 1 or iperiod == 3:
                        ext = 1
                if dotw == 3:
                    if iperiod == 1 or iperiod == 3:
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
                    if iperiod == 4:
                        rec = 1
                if dotw == 3:
                    if iperiod == 2:
                        rec = 1
                if dotw == 4:
                    if iperiod == 6:
                        rec = 1  
            if (icnum == 5):
                if dotw == 2:
                    if iperiod == 2 or iperiod == 4 or iperiod == 6:
                        rec = 1
                if dotw == 5:
                    if iperiod == 2:
                        rec = 1
            if (icnum == 6):
                if dotw == 2:
                    if iperiod == 2 or iperiod == 4:
                        rec = 1
                if dotw == 3:
                    if iperiod == 2 or iperiod == 4:
                        rec = 1
            #end classes
            print('end double class init')
            print(f'{ext}{rec}')
            if (icnum == 3 or icnum == 5 or icnum == 6): #I write it like this in case of same teachers#########################################Add if have T.name
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
            print(f'test start:{startTime}')
            endTime = startTime + 1 + ext # extend end time or reduce start time
            startTime = startTime - rec
            print('end time init')
            print(f'0::{startTime} {endTime}')
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
                teacher_name = teachername[tsrc][schedule[cnum][dayoftoday][iperiod - 1]]
        #value init done
            if (dotw > 5):
                await ctx.send(random.choice(stupidWord) + "\nIf you think I'm wrong, try using +cindiv. More info at +clistcmd")
            elif (iperiod >= 8 or iperiod < 1):
                await ctx.send('What?')
            else:
                print(f'finalize {cnum} {type(cnum)} {dayoftoday}') # For troubleshooting
                embed = discord.Embed(title = f'{schedule[cnum][dayoftoday][iperiod - 1]}', description = f'Teacher : {teacher_name}\nDuration : {startTime}{timenum} - {endTime}{timenum}',url=hyperlink,color=color)
                embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} {dayoftoday} #{iperiod}', icon_url = ctx.author.avatar_url)
                await ctx.send(embed=embed)
                #await ctx.send(f'{schedule[cnum][dayoftoday][iperiod - 1]} \nStarts at {startTime}{timenum}')
        
        except: 
            embed = discord.Embed(title = f'Unavailable', description = "I don't have your schedule in my Database \n type +db to check my database availability",color=0xff2222)
            embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} {dayoftoday} #ERROR', icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)


class Schedule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Schedule Loaded!')  
    
    @commands.command()
    async def db(self,ctx):
        embed = discord.Embed(title = 'My active schedule database',description = 'This Database was last updated at 29/6/2021 10:44\n \n6/1 - 6/10 (14/40 355%)', color=0x7bd8f1)#####################################update database
        embed.add_field(name='6/1  (4/4 100%)', value = '- Schedule\n- Subject \n- Link \n- Teacher')
        embed.add_field(name='6/3  (4/4 100%)', value = '- Schedule\n- Subject \n- Link \n- Teacher', inline=True)
        embed.add_field(name='6/5  (3/4 75%)', value = '- Schedule()\n- Subject \nx Link \n- Teacher(same as 6/3)',inline=True)
        embed.add_field(name='6/6  (3/4 75%)', value = '- Schedule()\n- Subject \nx Link \n- Teacher(same as 6/3)',inline=True)
        embed.set_footer(text='Database Version : v9')
        await ctx.send(embed=embed)

    @commands.command()
    async def c(self,ctx,cnum,period):
        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday() + 1
        await getCInfo(ctx,cnum,period)
    @commands.command()
    async def c(self,ctx,cnum,period):
        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday()
        await getCInfo(ctx,cnum,period)
    @commands.command()
    async def hr(self,ctx,cnum):
        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday()	
        if dotw > 5:
            dayoftoday = 'Weekend'
        else:
            dayoftoday = sourceDict['dotweek'][dotw - 1]
        if cnum == '3' or cnum =='1':#####################################Add if have Homeroom

            embed = discord.Embed(title = f'Homeroom', description = f'Click to be redirected to Homeroom',url=urls[cnum]['Homeroom'],color=dotwColor[dayoftoday])
            embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} {dayoftoday} #0', icon_url = ctx.author.avatar_url)
            
        else: 
            embed = discord.Embed(title = f'Homeroom', description = f'Not available',color=0xff0000)
            embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} {dayoftoday} #ERROR', icon_url = ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def call(self,ctx,dayofrequest,cnum):
        icnum = int(cnum)
        i = 0
        try:
            for y in schedule[cnum][dayofrequest]:
                
                if (icnum == 3 or icnum == 5 or icnum == 6): #I write it like this in case of same teachers##############################################################Add Teacher here
                    tsrc = '3' #Teacher Source
                    teacher_name = teachername[tsrc][schedule[cnum][dayofrequest][i]]
                elif (icnum == 1):
                    tsrc = '1' 
                    teacher_name = teachername[tsrc][schedule[cnum][dayofrequest][i]]
                
                #Add it here with elif
                else:
                    teacher_name = 'Unknown'
                if icnum == 3 or icnum == 1: ########################################################################if class have link add here
                    hyperlink = urls[cnum][schedule[cnum][dayofrequest][i]]
                else :
                    hyperlink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

                
                embed = discord.Embed(title = f'{schedule[cnum][dayofrequest][i]}', description = f'Teacher : {teacher_name}',url=hyperlink,color=dotwColor[dayofrequest])
                embed.set_footer(text=f'6/{cnum} {dayofrequest} #{i + 1}')
                await ctx.send(embed=embed)
                i += 1
        except:
                embed = discord.Embed(title = f'Cannot Fetch', description = f'Please check that\n-You spell the day of the week correctly\n-I may not have your schedule info. Check my database at +db',color=0xff2222)
                embed.set_footer(text=f'6/{cnum} {dayofrequest} #ERROR')
                await ctx.send(embed=embed)
    
    @commands.command()
    async def cindiv(self,ctx,dayofrequest,cnum,i):
        icnum = int(cnum)
        iperiod = int(i)
        req = schedule[cnum][dayofrequest][iperiod - 1]
        try:
            if icnum == 3 or icnum == 1: ########################################################################if class have link add here
                    hyperlink = urls[cnum][req]
            else :
                    hyperlink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            if (icnum == 3 or icnum == 5 or icnum == 6): #I write it like this in case of same teachers##############################################################
                tsrc = '3' #Teacher Source
                teacher_name = teachername[cnum][req]
            elif (icnum == 1):
                tsrc = '1' 
                teacher_name = teachername[cnum][req]
            embed = discord.Embed(title = f'{req}', description = f'Teacher : {teacher_name}',url=hyperlink,color=dotwColor[dayofrequest])
            embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} #{i}(manual-input)', icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title = f'Cannot Fetch', description = f"Are you sure that your spelling is correct?\nI cannot search the link for you if you have mistake in your spelling",color=0xff2222)
            embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} #ERROR', icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
    @commands.command()
    async def cinfo(self,ctx,cnum,req):
        icnum = int(cnum)
        try:
            if icnum == 3 or icnum == 1: ########################################################################if class have link add here
                    hyperlink = urls[cnum][req]
            else :
                    hyperlink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            if (icnum == 3 or icnum == 5 or icnum == 6): #I write it like this in case of same teachers##############################################################
                tsrc = '3' #Teacher Source
                teacher_name = teachername[cnum][req]
            elif (icnum == 1):
                tsrc = '1' 
                teacher_name = teachername[cnum][req]
            embed = discord.Embed(title = f'{req}', description = f'Teacher : {teacher_name}',url=hyperlink,color=dotwColor['Wednesday'])
            embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} #manual-input', icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title = f'Cannot Fetch', description = f"Are you sure that your spelling is correct?\nI cannot search the link for you if you have mistake in your spelling",color=0xff2222)
            embed.set_footer(text=f'{ctx.author.name} : 6/{cnum} #ERROR', icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
            
def setup(client):
    client.add_cog(Schedule(client))
