import discord
from discord.ext import commands
import datetime
import json

# Initiate JSON
with open('scheduledatabase.json', 'r') as data:
    json_data = json.load(data)
    urls = json_data['urls']
    teachername = json_data['teachername']
    schedule = json_data['schedule']
    information = json_data["information"]
dbclasslist = information['dbclasslist']
dbvaluelist = information['dbvaluelist']
version = information['version']


sourceDict = {"cmdList": ['+c [Class] [Period] \n+nuay \n+ping \n+db \n+cindiv [day of the week (Monday, Tuesday,...)] [class] [period]'], 'dotweek': [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}


dotwColor = {
    'Monday': 0xffff8a,
    'Tuesday': 0xf3b0c3,
    'Wednesday': 0xadff2f,
    'Thursday': 0xFFC8A2,
    'Friday':  0xABDEE6,
    'Weekend': 0xff3333


}
# Database
#When update, also update at #####################################


async def checkClassBefore(grade, class_number, iperiod, dotw):
    dayoftoday = sourceDict['dotweek'][dotw - 1]
    return not (schedule[grade][class_number][dayoftoday][iperiod - 1] == schedule[grade][class_number][dayoftoday][iperiod - 2])


async def getClassInfo(ctx, grade, class_number, period, dotw):
    if dotw == 8:
        dotw = 1
    if dotw > 5:
        dayoftoday = 'Weekend'
    else:
        dayoftoday = sourceDict['dotweek'][dotw - 1]

    icnum = int(class_number)
    iperiod = int(period)
    subject = schedule[grade][class_number][dayoftoday][iperiod - 1]
    color = dotwColor[dayoftoday]

    try:
        print(f'0:{icnum} {iperiod} {dotw} {type(icnum)} {type(iperiod)}')
        print(f'1:{dayoftoday}')
        tunk = False  # Declare Teacher Unknown
        rec = 0  # declare rec and extend
        extend = 0
        try:
            teacher_name = teachername[grade][class_number][subject]
        except:
            teacher_name = 'Unknown'
        try:
            the_subject = subject
            url = urls[grade][class_number][the_subject]
        except:
            url = 'http://127.0.0.1'
        try:
            next_url = urls[grade][class_number][schedule[grade]
                                                 [class_number][dayoftoday][iperiod]]
        except:
            url = 'http://127.0.0.1'

        print('end hyperlink init')
        # double class init.
        try:
            if schedule[grade][class_number][dayoftoday][iperiod - 1] == schedule[grade][class_number][dayoftoday][iperiod]:
                extend = 1
            if schedule[grade][class_number][dayoftoday][iperiod - 1] == schedule[grade][class_number][dayoftoday][iperiod - 2]:
                rec = 1
        except:
            pass
        print('end double class init')
        print(f'{extend}{rec}')

        if iperiod >= 5:
            startTime = iperiod + 8  # in case after lunch
        else:
            startTime = iperiod + 7  # get hour of start time
        print(f'test start:{startTime}')
        endTime = startTime + 1 + extend  # extend end time or reduce start time
        startTime = startTime - rec
        print(f'erse:{extend}{rec}{startTime}{endTime}')
        print('end time init')
        print(f'0::{startTime} {endTime}')
        if iperiod == 1 or iperiod == 2:
            timenum = ':20'
        elif iperiod >= 3 and iperiod <= 5:
            timenum = ':30'
        elif iperiod >= 6:
            timenum = ':40'
        print(f'2:{iperiod} {timenum} {dotw}')

        endtimenum = timenum

        if extend == 1 or rec == 1:
            if iperiod >= 5:
                timenum = ':30'
                endtimenum = ':40'

        day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

        the_subject = schedule[grade][class_number][dayoftoday][iperiod - 1]

        projection = []

        try:
            for days in schedule[grade][class_number]:
                index = 0
                for subject in schedule[grade][class_number][days]:

                    if subject == the_subject:
                        if iperiod < 7:
                            if the_subject == schedule[grade][class_number][days][index + 1] and the_subject == schedule[grade][class_number][days][index - 1]:
                                projection.append('=X=')
                            elif the_subject == schedule[grade][class_number][days][index + 1]:
                                projection.append('[X=')
                            elif the_subject == schedule[grade][class_number][days][index - 1]:
                                projection.append('=X]')
                            else:
                                projection.append('[X]')
                    else:
                        projection.append('___')
                    index += 1
        except:
            pass
            print(subject)

        try:
            projection[(7 * (dotw - 1)) + iperiod - 1] = '<X>'
        except:
            pass
        print(f'3:{len(projection)}')
        table = f'''```
Days --- 1 - 2 - 3 - 4 --- 5 - 6 - 7
{day[0]} --- {projection[0]} {projection[1]} {projection[2]} {projection[3]} - {projection[4]} {projection[5]} {projection[6]}
{day[1]} --- {projection[7]} {projection[8]} {projection[9]} {projection[10]} - {projection[11]} {projection[12]} {projection[13]}
{day[2]} --- {projection[14]} {projection[15]} {projection[16]} {projection[17]} - {projection[18]} {projection[19]} {projection[20]}
{day[3]} --- {projection[21]} {projection[22]} {projection[23]} {projection[24]} - {projection[25]} {projection[26]} {projection[27]}
{day[4]} --- {projection[28]} {projection[29]} {projection[30]} {projection[31]} - {projection[32]} {projection[33]} {projection[34]}
```'''
    # value init done
        print('value init done')
        if (dotw > 5):
            embed = discord.Embed(
                title='Weekend!', description="If you think I'm wrong, try using +cindiv. More info at +clistcmd", color=dotwColor['Weekend'])
            await ctx.send(embed=embed)
        elif (iperiod >= 8 or iperiod < 1):
            await ctx.send('What?')
        try:
            the_subject = schedule[grade][class_number][dayoftoday][iperiod - 1]
            url = urls[grade][class_number][the_subject]
        except:
            url = 'None'

        if (iperiod == 7):
            next_class = 'Unknown'
        else:
            next_class = schedule[grade][class_number][dayoftoday][iperiod]

        print(url)
        # For troubleshooting
        print(f'finalize {class_number} {type(class_number)} {dayoftoday}')
        if not url == "None":
            embed = discord.Embed(title=f'{schedule[grade][class_number][dayoftoday][iperiod - 1]}',
                                  url=url, description='(Click the title to be redirected to class.)', color=color)
        else:
            embed = discord.Embed(
                title=f'{schedule[grade][class_number][dayoftoday][iperiod - 1]}', color=color)

        embed.add_field(name=f'Teacher :', value=teacher_name)
        embed.add_field(name='Start time:', value=f'{startTime}{timenum}')
        embed.add_field(name='End time:', value=f'{endTime}{endtimenum}')
        embed.add_field(name=f'Class Presented on :', value=table, inline=True)
        embed.add_field(name='Next Class :', value=next_class, inline=True)
        embed.set_footer(text=f'{dayoftoday} {grade}/{class_number} #{period}')
        await ctx.send(embed=embed)

    except:
        if (dotw > 5):
            embed = discord.Embed(
                title='Weekend!', description="If you think I'm wrong, try using <cindiv. More info at <help", color=dotwColor['Weekend'])
            embed.set_footer(
                text=f'{dayoftoday} {grade}/{class_number} #{period}')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Unavailable', description="It's either you spell something wrong, I don't have it in my database.\n Or it could be that I have error in my database", color=dotwColor['Weekend'])
            embed.set_footer(
                text=f'{dayoftoday} {grade}/{class_number} #{period}')
            await ctx.send(embed=embed)


class Schedule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Schedule Loaded!')

    @commands.command()
    async def c(self, ctx, grade, class_number, period):
        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday()
        await getClassInfo(ctx, grade, class_number, period, dotw)

    @commands.command()
    async def ctmr(self, ctx, grade, class_number, period):
        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday()
        dotw += 1
        await getClassInfo(ctx, grade, class_number, period, dotw)

    @commands.command()
    async def db(self, ctx):
        embed = discord.Embed(title='My Database', color=dotwColor['Friday'])
        for index, classroom in enumerate(dbclasslist):
            embed.add_field(name=classroom, value=dbvaluelist[index])
        embed.set_footer(text=f'Version : {version}')
        await ctx.send(embed=embed)

    @commands.command()
    async def call(self, ctx, dayofrequest, grade, class_number):

        try:
            for subject in schedule[grade][class_number][dayofrequest]:
                try:
                    teacher_name = teachername[grade][class_number][subject]
                except:
                    teacher_name = 'Unknown'
                try:
                    the_subject = subject
                    url = urls[grade][class_number][the_subject]
                except:
                    url = 'http://127.0.0.1'

                embed = discord.Embed(
                    title=the_subject, color=dotwColor[dayofrequest], url=url)
                embed.add_field(
                    name="Teacher", value=teacher_name, inline=False)
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="Cannot Fetch more...",
                                  description="There was an error while looking up the database", color=0xff3333)
            await ctx.send(embed=embed)

    @commands.command()
    async def cinfo(self, ctx, grade, class_number, req):
        count = 0
        icnum = int(class_number)
        try:

            teacher_name = teachername[grade][class_number][req]
            the_subject = req
            try:
                url = urls[grade][class_number][the_subject]
            except:
                url = 'None'

            projection = []

            for days in schedule[grade][class_number]:
                index = 0
                for subject in schedule[grade][class_number][days]:

                    if subject == the_subject:
                        if the_subject == schedule[grade][class_number][days][index + 1] and the_subject == schedule[grade][class_number][days][index - 1]:
                            projection.append('=X=')
                        elif the_subject == schedule[grade][class_number][days][index + 1]:
                            projection.append('[X=')
                        elif the_subject == schedule[grade][class_number][days][index - 1]:
                            projection.append('=X]')
                        else:

                            projection.append('[X]')
                    else:
                        projection.append('___')
                    index += 1
            table = f'''```
Days --- 1 - 2 - 3 - 4 --- 5 - 6 - 7
Mon --- {projection[0]} {projection[1]} {projection[2]} {projection[3]} - {projection[4]} {projection[5]} {projection[6]}
Tue --- {projection[7]} {projection[8]} {projection[9]} {projection[10]} - {projection[11]} {projection[12]} {projection[13]}
Wed --- {projection[14]} {projection[15]} {projection[16]} {projection[17]} - {projection[18]} {projection[19]} {projection[20]}
Thu --- {projection[21]} {projection[22]} {projection[23]} {projection[24]} - {projection[25]} {projection[26]} {projection[27]}
Fri --- {projection[28]} {projection[29]} {projection[30]} {projection[31]} - {projection[32]} {projection[33]} {projection[34]}
```'''
            print(table)

            # embed = discord.Embed(title = f'{req}', description = f'Teacher : {teacher_name}',url=url,color=dotwColor['Wednesday'])
            if not url == "None":
                embed = discord.Embed(
                    title=f'{req}', url=url, description='(Click the title to be redirected to class.)', color=dotwColor['Wednesday'])
            else:
                embed = discord.Embed(
                    title=f'{req}', color=dotwColor["Wednesday"])
            embed.add_field(name=f'Class Presented on :', value=table)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Cannot Fetch', description=f"Are you sure that your spelling is correct?\nI cannot fetch the information for you if you have mistake in your spelling\n\nMaybe get rid of spaces and place a capital latter between words\nEx. Applied sicence -> AppliedScience", color=0xff2222)
            await ctx.send(embed=embed)

    @commands.command()
    async def cindiv(self, ctx, dayofreq, grade, class_number, period):
        try:
            convert = {
                'Monday': 1,
                'Tuesday': 2,
                'Wednesday': 3,
                'Thursday': 4,
                'Friday': 5
            }

            dotw = convert[dayofreq]

            await getClassInfo(ctx, grade, class_number, period, dotw)
        except:
            embed = discord.Embed(
                title=f'Cannot Fetch', description=f"Are you sure that your spelling is correct?\nI cannot search the link for you if you have mistake in your spelling", color=0xff2222)
            embed.set_footer(
                text=f'Unaccepted Input :{dayofreq} 6/{class_number} {period}')
            await ctx.send(embed=embed)

    @commands.command()
    async def hr(self, ctx, grade, class_number):
        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday()
        if dotw == 8:
            dotw = 1
        if dotw > 5:
            dayoftoday = 'Weekend'
        else:
            dayoftoday = sourceDict['dotweek'][dotw - 1]
        try:
            embed = discord.Embed(title=f'Homeroom', description=f'Click the link to be redirected to Homeroom',
                                  url=urls[grade][class_number]['Homeroom'], color=dotwColor[dayoftoday])
        except:
            embed = discord.Embed(
                title=f'Homeroom', description=f'Not available', color=0xff0000)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Schedule(client))
