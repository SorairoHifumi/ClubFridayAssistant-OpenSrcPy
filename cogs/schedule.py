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

urls = {
'1' : {
'Animation' : 'http://classroom.google.com/',
'Workshop' : 'https://teams.microsoft.com/l/channel/19%3a5lQajKHkAZGSFP1hcvQr6OZijaC-pWN-AmMtqEsWoM81%40thread.tacv2/General?groupId=452d822f-f0cb-4331-b7f1-4ce888995a92&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'ArtProject' : 'https://teams.microsoft.com/l/channel/19%3aYU8yBNB-16j_ETUlGD1xXu9OJ39m0gWuRFK1YJWjdYs1%40thread.tacv2/General?groupId=7f916f02-856c-42fa-9a7a-4f3b4b1bd73d&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Art' : 'https://teams.microsoft.com/l/channel/19%3aj9-JHQytpqDu4ItXKY1Xq_KYpelvakaTQrk78iu3ljA1%40thread.tacv2/General?groupId=09b8e3e4-d910-4ac6-98c7-3d5389cea470&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Listening' : 'https://teams.microsoft.com/l/channel/19%3aKMuT5b33Z9D8CSucmO6rMLI_YWBJ48dR-jHCD5CqPC81%40thread.tacv2/General?groupId=578e485e-b9fa-4dc8-80a3-c3efafeea986&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'PhysicalEducation' : 'https://teams.microsoft.com/l/channel/19%3a4bQkFjB4bYW2hI28eJvtOMKOIQHovfAanBz0ks3Wp8E1%40thread.tacv2/General?groupId=449a1b9f-ff81-48d3-becc-f7487c540dcd&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'CurrentEvent' : "https://teams.microsoft.com/l/channel/19%3a72ac4c6ed1b64017b87ce943179c8085%40thread.tacv2/General?groupId=c08c013d-27c3-4da8-8c0d-0f76b394c2d9&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d",
'Mathematics' : 'https://teams.microsoft.com/l/channel/19%3af2YJuG8sd41yDOkDiuU1Ov9gvU8KqBdbh7Qaofeu_j81%40thread.tacv2/General?groupId=c5d1025e-a519-4e80-a989-9d02b9b0a71e&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Thai' : 'https://teams.microsoft.com/l/channel/19%3aUhomJZvojdaYgYL01MINwR4pkjv9_8Du4-IeB994Fvg1%40thread.tacv2/General?groupId=4bbe386e-12a4-4fcf-b50e-f7c2424ee9cc&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Grammar' : 'https://teams.microsoft.com/l/channel/19%3af49fac7362684ea59865e42aebb793a7%40thread.tacv2/General?groupId=74157026-e2d7-407a-838e-573cf2614bed&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Literature' : 'https://teams.microsoft.com/l/channel/19%3ad7HMK0LiaRypnAf1WstkSooGTjYwGCeEEmTZC2zOdh01%40thread.tacv2/General?groupId=007371f3-daf6-499d-a193-c65a807ca29f&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Economics' : 'https://teams.microsoft.com/l/channel/19%3aUAJZcoKwCojfBDHr_2b2CNEUKVGWdhuaiNUMTah2b3U1%40thread.tacv2/General?groupId=b967fcd0-27fa-421e-a49a-9cbe5349a9d0&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Science' : 'https://teams.microsoft.com/l/channel/19%3aB-nShcjx006dKM6mRMM8ZAw5h0pRVEg1q2hBDPSxf641%40thread.tacv2/General?groupId=5ed04663-29fb-46bd-8ab8-916111af8e79&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Social' : 'https://teams.microsoft.com/l/channel/19%3aWFAAfcoHb-QHPhhZy5Pc7uE1XK5FMnNrRmfLWC-WWpM1%40thread.tacv2/General?groupId=15a3140c-ac08-4a25-b4c3-a60b74f1cec2&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Web Design' : 'http://classroom.google.com/',
'Guidance' : 'https://teams.microsoft.com/l/channel/19%3aeS6tt3sPS2q2lP83JPBkwWDDl70vsNIassi4ZV82A_E1%40thread.tacv2/General?groupId=e7bab30f-a6fc-4a57-a9c4-8255df9177c0&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Elective' : 'https://www.youtube.com/watch?v=y6120QOlsfU',
'Writing' : 'https://teams.microsoft.com/l/channel/19%3andAC2qP0gp17w98phNFQeAKvWEWkaFCfrQiyV45Rehs1%40thread.tacv2/General?groupId=9ec42380-eb32-472b-870f-351c22ae8cec&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'WorkEducation' : 'https://teams.microsoft.com/l/channel/19%3aLbFCsq6x2UFS9tH03LLFQf9_JM0ENAXanoVxS_xsOeM1%40thread.tacv2/General?groupId=09900c21-7fab-4966-9224-69a730919f75&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'GraphicDesign' : 'https://teams.microsoft.com/l/channel/19%3a_LO7W35RDGEi1fpqSc0cGVmn8BoQfUjgbir1mVDnrSY1%40thread.tacv2/General?groupId=1768f5e5-8952-480f-af1b-d89e74def11d&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Club' : 'https://tetr.io',
'None' : 'None',
'Homeroom' : 'https://teams.microsoft.com/l/channel/19%3axzwCO-EdJP2d3BvA7BX-FgBePz19a56hNvxJgbAGqec1%40thread.tacv2/General?groupId=51c37b30-bd90-4ce6-bad6-9133b7915743&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d'
},

'3' : {
'Homeroom' : 'https://teams.microsoft.com/l/team/19%3a11Cyygyt7CArYDMpd6H1vuDESl37TvG4qWX0kK-9L_01%40thread.tacv2/conversations?groupId=ca14ebd6-2495-4478-9810-cbb7f118ea4f&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Physics' : 'https://teams.microsoft.com/l/team/19%3awiRyWxv-a2ufOGA1K9eulIvOvHwK-RWUNX0fcc13zZQ1%40thread.tacv2/conversations?groupId=c4862ed4-ef78-427e-89be-af6050a340d3&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Biology' : 'https://classroom.google.com',
'EarthScience' : 'https://teams.microsoft.com/l/team/19%3ab3IfEr1z-62aKpWpEwsHFB2QOA--FSQyVCi7oyqL46k1%40thread.tacv2/conversations?groupId=11fe7652-a13b-435d-a7bb-778769116400&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Meteorology' : 'https://teams.microsoft.com/l/team/19%3aU0d_CgNsCQOdF47GSbhnwY2VJWW3kzXcj239qQNqBXQ1%40thread.tacv2/conversations?groupId=b8f8b8e6-873b-4f85-af11-11a918df14e8&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Thai' : 'https://teams.microsoft.com/l/team/19%3aCmcc60pZF1yfQa7o4cGC4XR6o9OlRgjKh-EOEdqvhq81%40thread.tacv2/conversations?groupId=45eb15da-9003-4af8-b9ee-014e483971b5&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'GrammarTuesday' : 'https://teams.microsoft.com/l/team/19%3a7dd03270c207459c88a18a19e9098da3%40thread.tacv2/conversations?groupId=e63e1193-319e-4aa4-ba89-234ab130d3e0&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d' ,
'GrammarWednesday' : 'https://teams.microsoft.com/l/team/19%3aa36ed0923b19478384d57ddfaf7469fd%40thread.tacv2/conversations?groupId=c63baa94-2b57-4b90-aa68-c72ef90508d7&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'AppliedScience' : 'https://teams.microsoft.com/l/team/19%3a21d35345de9349f8abc9d27a2ea99aad%40thread.tacv2/conversations?groupId=141f44f7-1fe6-4ed4-bdf1-1a11b69ff73f&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Mathematics' : 'https://teams.microsoft.com/l/team/19%3aIgymq5NY3W00sljDTPLR7fF3CrJZaYRbXP3hUrOxQ3w1%40thread.tacv2/conversations?groupId=fa1209cf-db59-4f85-bc08-7bda6c95a677&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'MathematicsONET' : 'https://teams.microsoft.com/l/team/19%3ag7HLaYPMCBBDcD-kO3lt9ZgpY8EzHira5WcEZMT9c5g1%40thread.tacv2/conversations?groupId=1a4211d1-16fb-4ec2-9c29-dce18e12754e&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Chemistry' : 'https://teams.microsoft.com/l/team/19%3aCsHy_jRXNJelEjwsHg4h2GEsOIXJUjUtqxDLmQtXtn81%40thread.tacv2/conversations?groupId=b5e924f3-ddb7-4a2b-9c99-0838b7ede423&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Social' : 'https://teams.microsoft.com/l/team/19%3abot5qj5PykPWN-fHUpyW9_OJoqJNPEMvZY9eXP2aFlI1%40thread.tacv2/conversations?groupId=7eb5370b-a635-43c8-ac6e-f64746017054&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Animation' : 'https://classroom.google.com',
'WorkEducation' : 'https://teams.microsoft.com/l/team/19%3a0BAWx0rDhcOIx8YT8OOKqFfTZeVhDftFcO87fWwblE01%40thread.tacv2/conversations?groupId=1e17b7d3-238b-45a1-88a6-91842dd40ce4&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Art' : 'https://teams.microsoft.com/l/team/19%3a27f4Iiu4DafLtuUCygNIPbTGyPjA3kwz8tYrrnpbF_I1%40thread.tacv2/conversations?groupId=12b24a4a-df09-4ac8-a6f6-709d557f4523&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'EnglishOnline' : "https://teams.microsoft.com/l/team/19%3ab_sA-B9928ifxIO7ZTVZ_gcqMyiA_BRWxtDLrEBkzaU1%40thread.tacv2/conversations?groupId=54084e6b-e52a-47dd-b850-191394f45a5c&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d",
'Vocabulary' : 'https://teams.microsoft.com/l/team/19%3aE_gYMPZDhcxQFviozeUr0NoFrQYPjTzgt-tYow_tiH01%40thread.tacv2/conversations?groupId=8b6feaeb-15d4-4c5c-8c50-a7ac67f1dbfc&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Guidance' : 'https://teams.microsoft.com/l/team/19%3az9fQL5MOPKBZxMYFkTKU4bXAj2lXE0RyK-9NRbC7Atw1%40thread.tacv2/conversations?groupId=dbe4f198-53db-421f-adfd-4a3005c17c79&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'HealthEducation' : 'https://teams.microsoft.com/l/team/19%3a_EpdOGtQ1krG3rl6e-prLPkB_-Bq9ncjgwhb4iTohLA1%40thread.tacv2/conversations?groupId=cc655c61-d65b-4f82-b3b0-93bfcfa986ac&tenantId=80bd855e-1509-448a-92ec-505024f9ff2d',
'Club' : 'https://tetr.io',
'None' : 'None'

}
}

teachername = { # go update at the c command too, otherwise it'll not show up
'1' : {
'Animation' : 'Monaphat',
'Workshop' : 'Kittiphat',
'ArtProject' : 'Teeranan',
'Art' : 'Teeranan',
'Listening' : 'Panicha',
'PhysicalEducation' : 'Attaphorn',
'CurrentEvent' : "Pramote",
'Mathematics' : 'Potchanee',
'Thai' : 'Sasinut',
'Grammar' : 'Apinya',
'Literature' : 'Armad',
'Economics' : 'Athiporn',
'Science' : 'Phittaphorn',
'Social' : 'Chalong',
'WebDesign' : 'Siriyupin',
'Guidance' : 'Penphan',
'Elective' : 'Depends',
'Writing' : 'Natamon',
'WorkEducation' : 'Siriluk',
'GraphicDesign' : 'Nattawan',
'Club' : 'Depends.',
'None' : 'None'



},
'3' : {
'Physics' : 'Songkrod Kaewsirnual',
'Biology' : 'Pakamon Thipnet',
'EarthScience' : 'Boonsong Henngam',
'Meteorology' : 'Boonsong Henngam',
'Thai' : 'Sasinut Khumsubdee',
'GrammarTuesday' : 'Apinya Chaikul' ,
'GrammarWednesday' : 'Apinya Chaikul' ,
'GrammarThursday' : 'Apinya Chaikul' ,
'GrammarFriday' : 'Apinya Chaikul' ,
'AppliedScience' : 'Tanongsak Prasopkittikun',
'Mathematics' : 'Potchanee Thoengchang',
'MathematicsONET' : 'Atittaya Samae',
'Chemistry' : 'Phonchan Sangkarn',
'Social' : 'Athiporn Makpoon',
'Animation' : 'Monaphat Chockananruttana',
'WorkEducation' : 'Siriluk Chaibundit',
'Art' : 'Teeranan Choocherd',
'EnglishOnline' : "Apinya Chaikul",
'Vocabulary' : 'Natamon Keeratichotigool',
'Guidance' : 'Penphan Apiratiwanon',
'HealthEducation' : 'Attaphorn Prasittinava',
'Club' : 'Depends.',
'None' : 'None'
}
}
schedule = {
'1' : {
'Monday':['Animation' , 'Workshop' , 'ArtProject' , 'ArtProject' , 'Listening' , 'PhysicalEducation'],
'Tuesday':['CurrentEvent' , 'Mathematics' , 'Thai' , 'Grammar' , 'Literature' , 'Economics'],
'Wednesday': ['Science' ,'Science', 'Social' , 'Art' , 'CurrentEvent' , 'Thai'],
'Thursday': ['WebDesign' , 'Guidance' , 'Mathematics' , 'Social' , 'Elective' , 'Elective'],
'Friday': ['Writing' , 'WorkEducation' , 'Listening' , 'Literature' , 'GraphicDesign' , 'Club'],
'Weekend':['None','None','None','None','None','None','None','None']
}
,
'3' : {
'Monday': ['Physics','Physics','Biology','Biology','EarthScience','EarthScience'],
'Tuesday': ['Thai','GrammarTuesday','AppliedScience','Mathematics','MathematicsONET','Chemistry'],
'Wednesday': ['Physics','Mathematics','GrammarWednesday','Social','Thai','Animation'],
'Thursday': ['Meteorology','MathematicsONET','Chemistry','Chemistry','WorkEducation','Art','EnglishOnline'],
'Friday': ['Social','Vocabulary','Guidance','HealthEducation','Mathematics','Club'],
'Weekend':['None','None','None','None','None','None','None','None']



},
'5' : {
'Monday': ['MathematicsONET','Meteorology','Mathematics','Chemistry','Social','Thai'],
'Tuesday': ['Physics','Physics','Biology','Biology','EarthScience','EarthScience'],
'Wednesday': ['Social','Vocabulary','Art','Mathematics','Physics','MathematicsONET'],
'Thursday': ['AppliedScience','Thai','HealthEducation','Guidance','GrammarThursday','Animation','EnglishOnline'],
'Friday': ['Chemistry','Chemistry','Mathematics','GrammarFriday','WorkEducation','Club'],
'Weekend':['None','None','None','None','None','None','None','None']
},
'6' : {
'Monday': ['Thai','Chemistry','Meteorology','MathematicsONET','Art','Social'],
'Tuesday': ['Chemistry','Chemistry','Physics','Physics','Social','Thai'],
'Wednesday': ['Biology','Biology','EarthScience','EarthScience','Mathematics','Physics'],
'Thursday': ['WorkEducation','Animation','Vocabulary','HealthEducation','Mathematics','GrammarThursday','EnglishOnline'],
'Friday': ['MathematicsONET','Mathematics','GrammarFriday','Guidance','AppliedScience','Club'],
'Weekend':['None','None','None','None','None','None','None','None']
}
}
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