import discord
from discord.ext import commands, tasks
import datetime

from discord.ext.commands.core import check
from cogs._assignment_noti_script import notify
import time
from cogs.schedule import checkClassBefore

gmt = 7  # GMT +7, Bangkok Thailand
hw_notihour = 19

# Variable for assignment_notification.py only
# ASSIGNMENT_NOTIFICATION CONFIG

runtime = [[8, 20], [9, 20], [10, 30], [
    12, 27], [11, 30], [14, 40], [15, 40]]
# These settings can be change in discord via commands


disableseventhclass = True
homework = True
hw_limitperday = 3
role_id = None
channel = None
gradenumber = None
classnumber = None
prior = 0
notification = True
cooldown = 0

colorlib = {
    'yellow': 0xffff8a,
    'red': 0xff9999,
    'green': 0xadff2f,
    'orange': 0xFFC8A2,
    'blue':  0xABDEE6
}


async def forcenoti(force, homework):
    if role_id and channel and gradenumber and classnumber:  # force starts from here
        await notify(channel, role_id, gradenumber,
                     classnumber, hw_limitperday, force, gmt, homework)
    # else:
    #     if role_id == None:
    #         try:
    #             channel.send(
    #                 "You haven't set a role for me to mention yet. Please make sure you do so and tell me by using `<setnotiroleid [role_id]`")
    #         except:
    #             pass
    #     if gradenumber == None and classnumber == None:
    #         try:
    #             channel.send(
    #                 "You haven't set your classroom yet. You can do so by using `<setclassroom [grade] [class]`")
    #         except:
    #             pass


class AssignmentNotification(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.background_task.start()
        print('Notifications Loaded!')

    @tasks.loop(seconds=10)
    async def background_task(self):
        global cooldown
        cooldown -= 1

        thisDay = datetime.date.today()
        dotw = thisDay.isoweekday()
        timenow = datetime.datetime.now()
        hour = int(timenow.strftime('%H')) + gmt
        if hour >= 13:
            index = hour - 8
        else:
            index = hour - 7
        await self.client.change_presence(activity=discord.Game(name=f"Studying Period {index}" if hour <= 16 and hour >= 8 else "Relaxing"))
        try:
            if not dotw >= 6 and not (disableseventhclass and hour >= 15) and await checkClassBefore(gradenumber, classnumber, index, dotw):
                timenow = datetime.datetime.now()
                hour = int(timenow.strftime('%H')) + gmt
                if hour >= 13:
                    index = hour - 8
                else:
                    index = hour - 7

                if notification:
                    timenow = datetime.datetime.now()
                    hour = int(timenow.strftime('%H')) + gmt
                    minute = int(timenow.strftime('%M')) + prior
                    if [hour, minute] in runtime:
                        if cooldown <= 0:
                            await channel.send(f'<@&{role_id}>')
                            # print('Trying to ping...')
                            await forcenoti(False, homework)
                            cooldown = 7
            if hour == hw_notihour and minute == 0 and homework and dotw != 6:
                if notification:
                    if cooldown <= 0:
                        await channel.send(f'<@&{role_id}>')
                        print('Trying to ping...')
                        await forcenoti(True, True)
                        cooldown += 8

        except:
            pass

    @commands.command()
    async def setnotiroleid(self, ctx, arg):
        global role_id
        role_id = arg
        await ctx.send(f"Successfully change the notification role to id:{role_id}")
        embed = discord.Embed(title='Notification Role Changed', color=colorlib['green'], description=f"""
    Be aware that all of this server notification that came from this bot will be redirected to <@&{role_id}> 
    """)
        await ctx.send(embed=embed)

    @commands.command()
    async def setclassroom(self, ctx, grade, classnum):
        global gradenumber, classnumber
        gradenumber = grade
        classnumber = classnum
        await ctx.send(f"Set the classroom to {gradenumber}/{classnumber}")

    @commands.command()
    async def setnotiprior(self, ctx, arg):
        global prior
        try:
            prior = int(arg)
            await ctx.send(f'Set the prior value to {prior}')
        except:
            await ctx.send("Please use whole number")

    @commands.command()
    async def togglenotification(self, ctx):
        global notification
        notification = False if notification else True
        embed = discord.Embed(title="Automatic Notification",
                              description=f"The Overall Notification has turned to {notification}", color=0xff0000)
        await channel.send(embed=embed)

    @commands.command()
    async def togglehomework(self, ctx):
        global homework
        homework = False if homework else True
        embed = discord.Embed(title="Automatic Homework Notification",
                              description=f"The Homowork Notification has turned to {homework}", color=0xff0000)
        await channel.send(embed=embed)

    @commands.command()
    async def forcenotification(self, ctx):
        await ctx.send("Force Execute Notification!")
        await forcenoti(True, True)

    @commands.command()
    async def setnotichannelid(self, ctx, arg):
        global channel_id, channel
        channel = self.client.get_channel(int(arg))

        await ctx.send(f"Successfully change the notification channel to channel_id:{arg}")
        embed = discord.Embed(title='Notification Channel Changed', color=colorlib['yellow'], description=f"""
    Be aware that all of this server notification that came from this bot will be redirected to the desired channel.
    
    """)
        embed.add_field(name=f'To test the new channel ID, the bot will send a test message to that channel',
                        value=f"If you don't see anything on that channel, make sure you follow the procedure correctly. If you think that the bot is misbehaving, feel free to report it at our website.", inline=False)
        await ctx.send(embed=embed)
        test = discord.Embed(title='This is a test message', color=colorlib['green'], description=f"""
    If you see this message pop up in the appropriate channel, you have successfully changed your notification chat channel.
    """)
        await channel.send(embed=test)


def setup(client):
    client.add_cog(AssignmentNotification(client))
