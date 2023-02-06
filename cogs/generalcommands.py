from discord.ext import commands
import random
import json
import os
import discord

class Generalcommands(commands.Cog, name='General Commands',description='Commands That Everyone Can Run'):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('Pong')
    
    @commands.command(pass_context=True)
    async def rps(self,ctx,choice):
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            #print(jsondata)
            
        computeroptions = ['rock','paper','scissors']
        computerchoice = random.choice(computeroptions)
        await ctx.send(f'I chose {computerchoice.capitalize()}')
        choice = choice.strip().lower()
        
        if choice == computerchoice:
            await ctx.send('We Tied!')
            jsondata[str(ctx.message.author.id)][0][1] = jsondata[str(ctx.message.author.id)][0][1] + 1
        elif choice == 'paper' and computerchoice == 'scissors':
            await ctx.send('You Lost')
            jsondata[str(ctx.message.author.id)][0][2] = jsondata[str(ctx.message.author.id)][0][2] + 1
        elif choice == 'paper' and computerchoice == 'rock':
            await ctx.send('You Won')
            jsondata[str(ctx.message.author.id)][0][0] = jsondata[str(ctx.message.author.id)][0][0] + 1
        elif choice == 'scissors' and computerchoice == 'paper':
            await ctx.send('You Won')
            jsondata[str(ctx.message.author.id)][0][0] = jsondata[str(ctx.message.author.id)][0][0] + 1
        elif choice == 'scissors' and computerchoice == 'rock':
            await ctx.send('You Lost')
            jsondata[str(ctx.message.author.id)][0][2] = jsondata[str(ctx.message.author.id)][0][2] + 1
        elif choice == 'rock' and computerchoice == 'paper':
            await ctx.send('You Lost')
            jsondata[str(ctx.message.author.id)][0][2] = jsondata[str(ctx.message.author.id)][0][2] + 1
        elif choice == 'rock' and computerchoice == 'scissors':
            await ctx.send('You Won')
            jsondata[str(ctx.message.author.id)][0][0] = jsondata[str(ctx.message.author.id)][0][0] + 1

        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
            json.dump(jsondata,f)
        
    
    @commands.command()
    async def test(self,ctx,userid:discord.Member):
        await userid.send('Test')
    
       

def setup(client):
    client.add_cog(Generalcommands(client))