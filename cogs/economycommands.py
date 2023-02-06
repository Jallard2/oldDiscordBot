from discord.ext import commands
import random
import json
import os
import discord

class Economycommands(commands.Cog, name='Economy Commands',description='Commands That Relate To the Economy'):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ecogive(self,ctx,userid:discord.Member,amount):
        logchannel = self.client.get_channel(int(923710173707644990))
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            jsondata[str(userid.id)][2] = jsondata[str(userid.id)][2] + int(amount)
            newamount = jsondata[str(userid.id)][2]
            #print(newamount)
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
            json.dump(jsondata,f)
        await ctx.message.delete()
        moneygive = discord.Embed(title = 'A Player Has Been Given Money',description = f'{ctx.message.author.mention} Has Given {userid.mention} ${int(amount):,}. They Now Have ${newamount:,}',color = discord.Color.purple())
        await logchannel.send(embed=moneygive)
        moneygiven = discord.Embed(title = 'You Have Been Given Money',description = f'You Have Been Given ${int(amount):,} Which Brings Your New Balance To ${int(newamount):,}')
        await userid.send(embed= moneygiven)
        
    @commands.command()
    @commands.cooldown(1,86400,commands.BucketType.user)
    async def dailyreward(self,ctx):
        amount = 100
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            jsondata[str(ctx.message.author.id)][2] = jsondata[str(ctx.message.author.id)][2] + amount
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
            json.dump(jsondata,f)
            await ctx.message.delete()
            reward = discord.Embed(title=f'You Have Gained ${amount:,} From Your Daily Reward',description = f'Your New Balance Is ${jsondata[str(ctx.message.author.id)][2]:,}',color=discord.Color.purple())
            await ctx.channel.send(embed=reward)

    @commands.command(aliases = ['bal','balance','b'])
    async def money(self,ctx):
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            currentmoney = jsondata[str(ctx.message.author.id)][2]
            money = discord.Embed(title=f'You Currently Have ${currentmoney:,}',color =discord.Color.purple())
            await ctx.message.delete()
            await ctx.channel.send(embed=money)
    
    @commands.command()
    @commands.cooldown(1,3600,commands.BucketType.user)
    async def work(self,ctx):
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            amount = random.randrange(50,250)
            jsondata[str(ctx.message.author.id)][2] = jsondata[str(ctx.message.author.id)][2] + amount
            await ctx.message.delete()
            reward = discord.Embed(title=f'You Have Gained ${amount:,} From Your Job',description = f'Your New Balance Is ${jsondata[str(ctx.message.author.id)][2]:,}',color=discord.Color.purple())
            await ctx.channel.send(embed=reward)
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
            json.dump(jsondata, f)
            

    @commands.command(aliases = ['moneyleaderboard','balanceleaderboard','balanceleaders','moneyleaders','balleader','balleaders','ecoleaders','ecoleader'])
    async def ecoleaderboard(self,ctx):
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
        guild = ctx.guild
        memberlist = guild.members
        balances = {}
        amount = 0
        moneyleaderboard = discord.Embed(title = 'Econonmy Leaderboard',color= discord.Color.purple())
        for member in guild.members:
            if str(member.id) in jsondata: 
                balances[jsondata[str(member.id)][2]] = str(member.id)
                balanceitems = balances.items()
                balancessorted = sorted(balanceitems,reverse=True)
                #print(balancessorted)
                moneyleaderboard.add_field(name=f'Number {(amount+1)}',value=f'{member.mention} Current Balance ${balancessorted[amount][0]:,}',inline = False)
                amount = amount + 1
                if amount == 4:
                    break
            else:
                #print(member)
                return
        
        await ctx.send(embed = moneyleaderboard)


def setup(client):
    client.add_cog(Economycommands(client))