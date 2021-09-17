import discord
from discord.ext import commands
import random
import time

color = 0xafcbff

end=False
auto = False
run = False
p1 = 'Player 1' # Player 1 
p2 = 'Player 2' # Player 2
hpmax = 9
hp1 = 9 # Health 1
hp2 = 9 # Health 2
c1 = 0 # Charge 1
c2 = 0 # Charge 2
l1 = 1 # Level 1
l2 = 1 # Level 2
dismax = 2
dis1 = 2
dis2 = 2

turn = 0

async def update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2):
    global turn,end
    next_turn = turn + 1
    if next_turn == 2:
        next_turn = 0
    play_next_turn = turnconvert(next_turn)
    print(f'Turn after update_game {turn}')
    embed=discord.Embed(title=f"Discharged : {play_next_turn[:-5]}'s turn.", color=color)
    embed.add_field(name=f'P1 Lv.{l1} : {p1[:-5]} ', value=f'DisChr : {dis1}/{dismax}', inline=True)
    embed.add_field(name="HP", value=f'{hp1}/{hpmax}', inline=True)
    embed.add_field(name="Chr", value=f'{c1}/3', inline=True)
    embed.add_field(name=f'P2 Lv.{l2} : {p2[:-5]} ', value=f'DisChr : {dis2}/{dismax}', inline=True)
    embed.add_field(name="HP", value=f'{hp2}/{hpmax}', inline=True)
    embed.add_field(name="Chr", value=f'{c2}/3', inline=True)
    turn +=1
    if turn == 2 :
        turn = 0
    
    if hp1 <= 0 or hp2 <= 0:
        end = True
        await ctx.send('Discharged Ended!')
        winner = 'none of you because everyone died :P' if hp1 <= 0 and hp2 <= 0 else None
        winner = p1 if hp2 <= 0 else p2
        embed=discord.Embed(title="We have a winner!!", description=f'The winner is {winner}', color=0xbffcc6)
        await restart()

    await ctx.send(embed=embed)
    time.sleep(1)
    if not end:
        if turn == 1 and auto:
            await bot_turn(ctx)
async def action_upgrade(ctx):
    global l1,l2,c1,c2,now_turn
    now_turn = turnconvert(turn)
    print(f'Turn:{turn}')
    print(f'Upgraded initiated for {now_turn}')
    print(f'{l1} {l2} {c1} {c2}')
    if turn == 0 and str(ctx.author) == p1:
        if l1 == 1:
            if c1 >= 1:
                l1 += 1
                c1 -= 1
                print(f'{l1} {c1}')
                await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            else:
                await ctx.send('Not enough charge.')
            
        elif l1 == 2:
            if c1 >= 2:
                l1 += 1
                c1 -= 2
                await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            else:
                await ctx.send('Not enough charge.')
                
        else:
            await ctx.send('Cannot Upgrade.')
    elif (turn == 1 and str(ctx.author) == p2) or auto:
        if l2 == 1:
            if c2 >= 1:
                l2 += 1
                c2 -= 1
                await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            else:
                await ctx.send('Not enough charge.')
            
        elif l2 == 2:
            if c2 >= 2:
                l2 += 1
                c2 -= 2
                await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            else:
                await ctx.send('Not enough charge.')
                
        else:
            await ctx.send('Cannot Upgrade.')
        
        
    else:
        await ctx.send('Unable.')
        
async def action_charge(ctx):
    global c1,c2,now_turn
    now_turn = turnconvert(turn)
    print(f'Turn:{turn}')
    print(f'Charge initiated for {now_turn}')
    if turn == 0 and str(ctx.author) == p1:
        if c1 <= 2:
            c1 += 1
            print(f'Charge initiated success for {now_turn} as {turn}')
            await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
        else:
            await ctx.send('Max Charge reached!')
    elif (turn == 1 and str(ctx.author) == p2) or auto:
        if c2 <= 2:
            c2 += 1
            print(f'Charge initiated success for {now_turn} as {turn}')
            await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
        else:
            await ctx.send('Max Charge reached!')
    else:
        await ctx.send('Unable.')

async def action_discharge(ctx):
        global hp1,hp2,c1,c2,now_turn,dis1,dis2
        now_turn = turnconvert(turn)
        print(f'Turn:{turn}')
        print(f'Attack initiated for {now_turn} as {turn}')
        if turn == 0 and str(ctx.author) == p1:
            if dis1:
                damage = random.randint(0,2) if l1 == 1  else random.randint(0,3) if l1 == 2  else random.randint(1,4)
                possible = '0 - 2' if l1 == 1  else '0 - 3' if l1 == 2 else '1 - 4'
                extra_damage = random.randint(0,1) if c1 == 1  else random.randint(1,2) if c1 == 2  else random.randint(2,4)
                extra_possible = '+0 - +1' if c1 == 1  else '+1 - +2' if c1 == 2 else '+2 - +4'
                extra_heal = 0 if c1 == 1  else random.randint(-1,1) if c1 == 2  else random.randint(-2,2)
                await ctx.send(f'Attack as level {l1} Possible damage: {possible} hp')
                await ctx.send(f'Based Attack damage : {damage}')
                await ctx.send(f'Bonus from Discharge Attack possible : {extra_possible}')
                await ctx.send(f'You got +{extra_damage} from your Discharge Attack')
                if l1 >=3:
                    extra_damage +=1
                    await ctx.send('Your Lv.3+ character gave you a Discharge Boost, Damage + 1')
                damage += extra_damage
                await ctx.send(f'You dealt **{damage}** hp total')
                if extra_heal != 0:
                    await ctx.send(f'You got side effect from Discharge Attack. You got {str(extra_heal)} health')
                    hp1 += extra_heal
                hp2 -= damage
                c1 = 0
                dis1 -= 1
                if c2 > 1 :
                    c2 -= 1
                await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            else:
                await ctx.send('You already use your both discharges.')
            
        elif (turn == 1 and str(ctx.author) == p2) or auto:
            if dis2:
                damage = random.randint(0,2) if l2 == 1  else random.randint(0,3) if l2 == 2  else random.randint(1,4)
                possible = '0 - 2' if l2 == 1  else '0 - 3' if l2 == 2 else '1 - 4'
                extra_damage = random.randint(0,1) if c2 == 1  else random.randint(0,2) if c2 == 2  else random.randint(0,4)
                extra_possible = '+0 - +1' if c2 == 1  else '+0 - +2' if c2 == 2 else '+0 - +4'
                extra_heal = 0 if c2== 1  else random.randint(-1,1) if c2 == 2  else random.randint(-2,2)
                await ctx.send(f'Attack as level {l2} Possible damage: {possible} hp')
                await ctx.send(f'Based Attack damage : {damage}')
                await ctx.send(f'Bonus from Discharge Attack possible : {extra_possible}')
                await ctx.send(f'You got +{extra_damage} from your Discharge Attack')
                if l1 >=3:
                    extra_damage +=1
                    await ctx.send('Your Lv.3+ character gave you a Discharge Boost, Damage + 1')
                damage += extra_damage
                await ctx.send(f'You dealt **{damage}** hp total')
                if extra_heal != 0:
                    await ctx.send(f'You got side effect from Discharge Attack. You got {str(extra_heal)} health')
                    hp2 += extra_heal
                hp1 -= damage
                c2 = 0
                dis2 -= 1
                if c1 > 1 :
                    c2 -= 1
                await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            else:
                await ctx.send('You already use your both discharges.')
        else:
            await ctx.send('Unable.')
            
async def action_attack(ctx):
        global hp1,hp2,now_turn
        now_turn = turnconvert(turn)
        print(f'Turn:{turn}')
        print(f'Attack initiated for {now_turn} as {turn}')
        if turn == 0 and str(ctx.author) == p1:
            damage = random.randint(0,2) if l1 == 1  else random.randint(0,3) if l1 == 2  else random.randint(1,4)
            possible = '0 - 2' if l1 == 1  else '0 - 3' if l1 == 2 else '1 - 4'
            await ctx.send(f'Attack as level {l1} Possible damage: {possible} hp')
            await ctx.send(f'You dealt **{damage}** hp total')
            hp2 -= damage
            await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            
        elif (turn == 1 and str(ctx.author) == p2) or auto:
            damage = random.randint(0,2) if l2 == 1  else random.randint(0,3) if l2 == 2  else random.randint(1,4)
            possible = '0 - 2' if l2 == 1  else '0 - 3' if l2 == 2 else '1 - 4'
            await ctx.send(f'Attack as level {l2} Possible damage: {possible} hp')
            await ctx.send(f'You dealt **{damage}** hp total')
            hp1 -= damage
            await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            
        else:
            await ctx.send('Unable.')

def turnconvert(turn):
    nowturn = p1 if turn == 0 else p2 if turn == 1 else 'AutoPilot#AUTO' if auto else None
    return nowturn

async def restart():
    global run,p1,p2,hp1,hp2,c1,c2,l1,l2,hpmax,auto,end,turn,dis1,dis2,dismax
    end=False
    auto = False
    run = False
    hpmax = 9
    hp1 = 9 # Health 1
    hp2 = 9 # Health 2
    c1 = 0 # Charge 1
    c2 = 0 # Charge 2
    l1 = 1 # Level 1
    l2 = 1 # Level 2
    dismax = 2
    dis1 = 2
    dis2 = 2
    turn = 0

async def bot_turn(ctx):
    bot_choice = []
    bot_choice.append('attack')
    if not l2 == 3 and dis2 ==0: # change here when Lv4
        pass
    else:
        if not c2 == 3:
            bot_choice.append('charge')
        
    if c2 > 1 :
        bot_choice.append('discharge')
    
    if (l2 == 1 and c2 >= 1) or (l2 == 2 and c2 >= 2): # change here when Lv4
        bot_choice.append('upgrade')
        
    if hp1 < 4:
        bot_choice = ['attack']
    if c2 == 3 and dis2 >= 1:
        bot_choice = ['discharge']
    elif c2 ==3 and l2 <=3:
        bot_choice = ['upgrade']
    else:
        bot_choice = ['attack']
        
    if hp2 <= 3 and c1 == 3 and dis2 >= 1:
        bot_choice = ['discharge']
        
    action = random.choice(bot_choice)
    
    if action == 'attack':
        await ctx.send('I choose attack!')
        await action_attack(ctx)
        
    if action == 'charge':
        await ctx.send('I choose to charge!')
        await action_charge(ctx)
        
    if action == 'discharge':
        await ctx.send('I choose to discharge!')
        await action_discharge(ctx)
        
    if action == 'upgrade':
        await ctx.send('I chose to upgrade!')
        await action_upgrade(ctx)
        
class Discharged(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command(name = "Upgrade", aliases=["up",'upgrade'])
    async def upgrade(self,ctx):
        await action_upgrade(ctx)

    @commands.command()
    async def p1(self,ctx):
        global p1
        if not run:
            p1 = str(ctx.author)
            await ctx.send(f'Set Player 1 to {p1}')
        else:
            await ctx.send('The game is running.')
        
    @commands.command()
    async def ap(self,ctx):
        global auto,p2
        if not run:
            if not auto:
                auto = True
                p2 = 'AutoPilot#AUTO'
                await ctx.send('AutoPilot Activated, The APBot will join as Player 2')
            else:
                auto = False
                p2 = 'Player 2'
                await ctx.send('AP Deactivated')
        else:
            await ctx.send('The game is running.')
            
    @commands.command()
    async def p2(self,ctx):
        global p2,auto
        if not run:         
            p2 = str(ctx.author)
            await ctx.send(f'Set Player 2 to {p2}')
            if auto:
                auto = False
                await ctx.send(f'APBot Detected at Player 2, AP Disengaged.')
        else:
            await ctx.send('The game is running.')
    
    
    @commands.command()
    async def pl(self,ctx):
        embed=discord.Embed(title="Player List", description="Here's the registered player.", color=color)
        embed.add_field(name="Player 1", value=p1, inline=False)
        embed.add_field(name="Player 2", value=p2, inline=False)
        await ctx.send(embed=embed)
    
        
    
    @commands.command()
    async def starthp(self,ctx,arg):
        global hp1,hp2,hpmax
        hp1 = int(arg)
        hp2 = int(arg)
        hpmax = int(arg)
        await ctx.send(f'Set starting health to {arg}')
        
    @commands.command()
    async def stop(self,ctx):
        global run,p1,p2,hp1,hp2,c1,c2,l1,l2,hpmax,auto,end,turn,dis1,dis2,dismax
        if run:# change here when Lv4
            end=False
            auto = False
            run = False
            p1 = 'Player 1' # Player 1 
            p2 = 'Player 2' # Player 2
            hpmax = 9
            hp1 = 9 # Health 1
            hp2 = 9 # Health 2
            c1 = 0 # Charge 1
            c2 = 0 # Charge 2
            l1 = 1 # Level 1
            l2 = 1 # Level 2
            dismax = 2
            dis1 = 2
            dis2 = 2
            turn = 0
            await ctx.send('Everything had been terminated and every value had been reset.')
        else:
            await ctx.send('No game were found.')
            
    @commands.command()
    async def reset(self,ctx):# change here when Lv4
        global dis1,dis2,run,p1,p2,hp1,hp2,c1,c2,l1,l2,hpmax,auto
        run = False
        auto = False
        end = False
        p1 = 'Player 1' # Player 1 
        p2 = 'Player 2' # Player 2
        hp1 = 9 # Health 1
        hp2 = 9 # Health 2
        hpmax = 9
        l1 = 1
        l2 = 1
        c1 = 0 # Charge 1
        c2 = 0 # Charge 2
        dis1 = 2
        dis2 = 2
        await ctx.send('The game data have been reset.')
        
    @commands.command()
    async def retry():
        global run,hp1,hp2,c1,c2,l1,l2,end,turn,dis1,dis2,dismax
        run = False
        end = False
        hp1 = hpmax # Health 1
        hp2 = hpmax # Health 2
        l1 = 1
        l2 = 1
        c1 = 0 # Charge 1
        c2 = 0 # Charge 2

    @commands.command()
    async def start(self,ctx):
        global run,turn
        turn = 0
        print(type(turn))
        print(turn)
        if not run:
            if p1 != 'Player 1' and p2 != 'Player 2':
                now_turn = p1 if turn == 0 else p2
                embed=discord.Embed(title=f"Discharged : {now_turn[:-5]}'s turn.", color=color)
                embed.add_field(name=f'Player 1 : {p1[:-5]}', value=f'Level : {l1}', inline=True)
                embed.add_field(name="HP", value=f'{hp1}', inline=True)
                embed.add_field(name="Chr", value=f'{c1}/3', inline=True)
                embed.add_field(name=f'Player 2 : {p2[:-5]}', value=f'Level : {l2}', inline=True)
                embed.add_field(name="HP", value=f'{hp2}', inline=True)
                embed.add_field(name="Chr", value=f'{c2}/3', inline=True)
                await ctx.send(embed = embed)
                run = True
            else:
                await ctx.send('Not enough player.')
        else:
            await ctx.send('There is already a game instance running.')
            
    @commands.command(name = "Charge", aliases=["chr",'charge'])
    async def charge(self,ctx):
        await action_charge(ctx)
        
    @commands.command(name = "Attack", aliases=["atk",'attack'])
    async def attack(self,ctx):
        await action_attack(ctx)
        
    
    @commands.command(name = "Discharge", aliases=["dischr",'discharge'])
    async def discharge(self,ctx):
        await action_discharge(ctx)
            
    @commands.command()
    async def resign(self,ctx):
        global hp1,hp2,now_turn
        if turn == 0 and str(ctx.author) == p1:
            hp1 = 0
            await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
            
        elif (turn == 1 and str(ctx.author) == p2) or auto:
            hp2 = 0
            await update_game(ctx,p1,p2,hp1,hp2,c1,c2,l1,l2)
        else:
            await ctx.send('Wait for your turn.')
    

def setup(client:commands.Bot):
    client.add_cog(Discharged(client))