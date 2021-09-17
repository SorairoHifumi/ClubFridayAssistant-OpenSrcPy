import discord
from discord.ext import commands
import math

round_to = 2

class Calculator(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Calculator Loaded!')
        
    @commands.command()
    async def sqrt(self,ctx,arg):
        ans = math.sqrt(arg)
        ctx.send(ans)
        
    @commands.command()
    async def calc(self,ctx,a,op,b):
        try:
            a = float(a)
            b = float(b)
            print(op)
            print(type(op))
            if op == '+':
                ans = a + b
            elif op == '-':
                ans = a - b
            elif op == '*':
                ans = a * b
            elif op == '/':
                ans = a / b
            elif op == '^':
                ans = a ** b
            else:
                ans = 'ERROR'
            await ctx.send(ans)
        except ZeroDivisionError :
            await ctx.send('Cannot divide by 0')
            
    @commands.command()
    async def circle(self,ctx,r):
        radius = float(r)
        
        area = (radius * radius) * math.pi
        area = round(area , round_to)
        circumference = math.pi * radius * 2
        circumference = round(circumference , round_to)
        embed = discord.Embed(title = 'Circle Information')
        embed.add_field(name = 'Area',value = area,inline=True)
        embed.add_field(name = 'Circumference',value = circumference,inline=True)
        await ctx.send(embed = embed)
        

    @commands.command()
    async def trig(self,ctx,trig,deg):
        
            deg = float(deg)
            rad = (math.pi / 180.0) * deg
            if trig == 'sin':
                ans = math.sin(rad)
            elif trig == 'cos':
                ans = math.cos(rad)
            elif trig == 'tan':
                ans = math.tan(rad)
            else:
                ans = 'ERROR'     
                
            await ctx.send(round(ans,round_to))   
    @commands.command()
    async def setrounding(self,ctx,arg):    
        global round_to
        arg = int(arg)
        if arg > 10:
            await ctx.send("I'd recommend to sue decimal rounding less that 10")
            round_to = 10
            await ctx.send(f'Set decimal rounding to {arg}')
        else:
            
            round_to = int(arg)
            await ctx.send(f'Set decimal rounding to {arg}')
            
def setup(client):
    client.add_cog(Calculator(client))