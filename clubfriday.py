import discord
import os
from discord.ext import commands
import datetime

sourceDict = {'dotweek':['Monday','Tuesday','Wednesday','Thursday','Friday']}
client = commands.Bot(command_prefix='<')
@client.event
async def on_ready():
  print('Main Loaded!')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

print('Cogs loading...')

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
    
    await ctx.send(datetime.datetime.now())

@client.command()
async def dayoftheweek(ctx):
    thisDay = datetime.date.today()
    dotw = thisDay.isoweekday()
    if dotw > 5:
        dayoftoday = 'Weekend'
    else:
        dayoftoday = sourceDict['dotweek'][dotw - 1]
    await ctx.send(f'{dayoftoday} #:{dotw}')

@client.command()
async def nuay(ctx):
	await ctx.send('nuay nuay nuay nuay nuay nuay nuay nuay nuay nuay' ,tts=True)
@client.command()
async def version(ctx):
	await ctx.send('Running Version : v1.2.2 VSC')

client.run(token_here)
