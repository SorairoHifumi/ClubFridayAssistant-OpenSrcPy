import assignment_api
import datetime
import discord
from cogs.schedule import getClassInfo


async def notify(ctx, mention, grade, classnum, limit, force, gmt, homework):
    print(f'Initiate with {grade}/{classnum} {mention}')
    now = datetime.datetime.now()
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    next2days = datetime.datetime.now() + datetime.timedelta(days=2)

    today_day = str(int(now.strftime('%d')))
    today_month = str(int(now.strftime('%m')))
    tomorrow_day = str(int(tomorrow.strftime('%d')))
    tomorrow_month = str(int(tomorrow.strftime('%m')))
    next2days_day = str(int(next2days.strftime('%d')))
    next2days_month = str(int(next2days.strftime('%m')))
    filtered_list = []
    assignment_list = assignment_api.getCurrentItem()

# Auto index
    timenow = datetime.datetime.now()
    hour = int(timenow.strftime('%H')) + gmt

    if hour >= 13:
        index = hour - 8
    else:
        index = hour - 7

    # index = 0 if force or hour >= 18 else index

    if force or hour >= 18:
        index = 0

    if index == 0 and homework:
        print(str(grade), str(classnum))

        for item in assignment_list:
            print(f'PROCESSING {item}')
            if item == []:
                continue
            elif item[2] == str(grade) and item[3] == str(classnum):
                filtered_list.append(item)
                print("Added: ", item)
        print(filtered_list)

        noti_today = []
        noti_tomorrow = []
        noti_next2days = []
        extra = []
        print("Start for loop 2")
        print(today_day, today_month)
        for item in filtered_list:
            if item[4] == today_day and item[5] == today_month:
                noti_today.append(item)
                print('Added Today:', item)
            elif item[4] == tomorrow_day and item[5] == tomorrow_month:
                noti_tomorrow.append(item)
                print('Tomorrow:', noti_tomorrow)
            elif item[4] == next2days_day and item[5] == next2days_month:
                noti_next2days.append(item)
                print('2d:', noti_next2days)

        count = len(noti_tomorrow)
        for itterate in noti_next2days:
            if int(count) < int(limit):
                extra.append(itterate)
                count += 1
        # Probably try to randomize the word...
        before_embed = discord.Embed(title="Make sure you submit these...")
        for itterate in noti_today:
            before_embed.add_field(
                name=itterate[7], value=f'Subject : {itterate[1]} / Submit Via:{itterate[6]}')

        if noti_today != []:
            await ctx.send(embed=before_embed)

        if len(noti_tomorrow) == 0:
            embed = discord.Embed(title="NO HOMEWORK!!",
                                  description="I guess it's just another uncommon days", color=0xff0000)
            pass
        elif len(noti_tomorrow) != 0:
            embed = discord.Embed(title="Homework Today!!!",
                                  description="Well, it's time for homework... I guess", color=0xff0000)
            for itterate in noti_tomorrow:
                embed.add_field(
                    name=itterate[7], value=f'Subject : {itterate[1]} / Submit Via:{itterate[6]}')

        await ctx.send(embed=embed)

        if noti_tomorrow != []:
            after_embed = discord.Embed(
                title="If you have free time...", description="If you want to minimize the work for tomorrow, you might want to consider some of these:")

            for itterate in noti_next2days:
                after_embed.add_field(
                    name=itterate[7], value=f'Subject : {itterate[1]} / Submit Via:{itterate[6]}')
            try:
                await ctx.send(embed=after_embed)
            except:
                pass
    else:
        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday()
        await getClassInfo(ctx, grade, classnum, index, dotw)


# payload = {'today': noti_today, 'tomorrow': noti_tomorrow,
#            'extra': extra}  # Incase I need to export ่the values
