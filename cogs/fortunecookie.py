import asyncio
import discord
from discord.ext import commands
import random
import time
delay = 2
stageOne = [
'That cookie was yummy.',
'That cookie was disgusting',
"What is this abomination. Oh, It's quite good.",
'Wow, oishii!!!',
'What is this thing. Yuck...',
'This one taste like vomit.',
'Is this cookie a poison or something?'
]

stageTwo = [
"Why is there a piece of paper inside? Let's read it.",
"Is this a cookie sandwich with a piece of paper in the middle?",
"I accidently ate a tiny piece of paper. Oh there is more. Let's read this thing",


]
stageThree = [
'Paper Unrolling...',
'Paper Unfolding...',
'He lost that paper. Wait... he found it.',
'...',
"He ate the paper. Wait... He's spitting it out?"
]

wordList = [
'You learn from your mistakes... You will learn a lot today.',
'Land is always on the mind of a flying bird.',
'Some of us learn from the mistakes of others; the rest are others.',
'You are unique, just like everybody else.',
'A clean bedroom is the sign of a broken computer.',
"If you don't want someone to ask you to do something again, do it terribly the first time! Or just make a bot to do it for you.",
'The next sentence is a lie. The previous sentence is the truth.',
'If you push hard enough you can get through any obstacle. Except a door marked "pull"!',
"Nothing ruins a Friday more then realising it's actually a Tuesday.",
"You started out with nothing, and you still have most of it.",
"If Mom says no, ask Dad!",
"The universe contains protons, neutrons, electrons and morons.",
"When life gives you lemons, make lemonade. When life gives you limes, throw the limes out the window and buy some damn lemonade!",
"If you're not supposed to eat after dark, why is there a light in the refrigerator?",
"If you forget what you look like, just look into a mirror. If the mirror doesn't look back, it's a window!",
"Bob has no hands. Knock Knock... who is it? It isn't Bob.",
"If you're not supposed to eat after dark, why is there a light in the refrigerator?",
'The greatest risk is not taking one.',
'This bot is a joke'
]

class FortuneCookie(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fortune Cookine Loaded!')

    @commands.command()
    async def cookie(self,ctx):
        await ctx.send(random.choice(stageOne))
        time.sleep(delay)
        await ctx.send(random.choice(stageTwo))
        time.sleep(delay)
        await ctx.send(f'`{random.choice(stageThree)}`')
        time.sleep(delay)
        embed = discord.Embed(title=random.choice(wordList),description=f'- The Cookie.')
        await ctx.send(embed=embed)

    @commands.command()
    async def cookiedelay(self,ctx,arg):
        global delay
        delay = int(arg)

def setup(client):
    client.add_cog(FortuneCookie(client))