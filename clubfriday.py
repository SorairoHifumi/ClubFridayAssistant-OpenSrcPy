import discord
import os
from discord.ext import commands
import datetime
import asyncio

colorlib = {
'yellow' : 0xffff8a,
'red' :0xff9999,
'green' : 0xadff2f,
'orange' : 0xFFC8A2,
'blue' :  0xABDEE6
}
helpIntro = discord.Embed(title = 'Help Page',color = 0xffffff)
helpIntro.add_field(name='Introduction:',value="""The commands that are listed here is the command that is available to the highest rank
If the server owner decided to unload some script, then you wouldn't be able to use some
of the commands, specifically the ones that are in the script that got unloaded. The bot is loaded with 
every script by default.""")#Hello are you here?

helpEmbed = [helpIntro,

discord.Embed(title='General Commands',color=colorlib['red'],description="""
`<reload`
Reload all scripts.

`<load`
Load specific script.

`<unload`
Unload specific script.

`<version`
Get the version that the bot is run on.

`<ping`
Get the latency between Discord server and the bot server.

""")
,
discord.Embed(title='Schedule Commands',color=colorlib['orange'],description="""
`<c [Class] [period]`
Get the specified class today

`<ctmr [Class] [period]`
Get the specified class tomorrow

`<db`
Look at the database that the bot is using.

`<hr`
Get the link to be redirected to homeroom.

`<call [Class] [Day of the week]`
List all the class in the day specified

`<cindiv [Dayof the week] [Class] [Period]`
Get a specific class in a specific day.

`<cinfo [Class] [Subject Name]`aaaaaaaaaaaa
Get Info about the Subject.


"""),
discord.Embed(title='Fortune Cookie! Command',color=colorlib['yellow'],description="""
`<cookie`
Eat a fortune cookie.
`<cookiedelay [seconds]`
Set `<cookie` delay between message.
""")
]

client = commands.Bot(command_prefix='<',help_command=None)
@client.event
async def on_ready():
  print('Main Loaded!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def help(ctx):
  emoji = ["⏪","⏩"]
  page = 0
  message =await ctx.send(embed=helpEmbed[page])

  for emojis in emoji:
    await message.add_reaction(emojis)

  def check(reaction,user):
    return user == ctx.author and str(reaction.emoji) in emoji

  while True:
    reaction, user = await client.wait_for('reaction_add',timeout=200,check=check)
    try:
        if str(reaction.emoji) == '⏩':
            page += 1
            await message.edit(embed=helpEmbed[page])
            for emojis in emoji:
                await message.remove_reaction(reaction,user)
        elif str(reaction.emoji) == '⏪':
            page -= 1
            await message.edit(embed=helpEmbed[page])
            for emojis in emoji:
                    await message.remove_reaction(reaction,user)
        else:
                await message.remove_reaction(reaction, user)
    except asyncio.TimeoutError:
      await message.delete
      break

@client.command()
async def load(ctx,ext):
    try:
        client.load_extension(f'cogs.{ext}')
        await ctx.send(f'Loaded {ext}.py')
    except:
        await ctx.send('There is no such script.')
@client.command()
async def unload(ctx,ext):
    try:
        client.unload_extension(f'cogs.{ext}')
        await ctx.send(f'Loaded {ext}.py')
    except:
        await ctx.send('Failed!')
        
@client.command()
async def reload(ctx):
    i = 0
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
            client.load_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Reloaded {filename}')
            i += 1
    await ctx.send(f'{i} script(s) has been reloaded in total.')
    
@client.command()
async def ping(ctx):
	await ctx.send(f'Latency : {round(client.latency * 1000)} ms')

@client.command()
async def getservertime(ctx):
    thisDay = datetime.date.today()
    dotw = thisDay.isoweekday()
    await ctx.send(datetime.datetime.now())
    await ctx.send(dotw)


@client.command()
async def version(ctx):
	await ctx.send('Running Version : v1.2.5 Server 2')

@client.command()
async def nuay(ctx):
	await ctx.send('nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay',tts=True)

client.run('no')
