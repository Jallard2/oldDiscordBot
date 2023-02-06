from discord.ext import commands
import random
import json
import os
import discord

class LevelCommands(commands.Cog, name='Level Commands',description='Commands That Relate To The Leveling System'):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def xp(self,ctx,userid:discord.Member=None):
        if userid == None:
            userid = ctx.message.author
            url = userid.avatar_url
            
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            xplevel = discord.Embed(color=discord.Color.purple())
            xplevel.set_thumbnail(url = url)
            xplevel.add_field(name=f'Current Level of {userid.name}',value = jsondata[str(userid.id)][3][0],inline=False)
            xplevel.add_field(name='Current XP',value = jsondata[str(userid.id)][3][1],inline=True)
            xplevel.add_field(name='XP Until Next Level',value = ((jsondata[str(userid.id)][3][0]) * 30) + 15,inline=True)
            await ctx.channel.send(embed = xplevel)
    
    @commands.command(aliases = ['xpleaders','xpleader','xpleaderboards'])
    async def xpleaderboard(self,ctx):
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
        guild = ctx.guild
        memberlist = guild.members
        levels = {}
        amount = 0
        xpleaderboard = discord.Embed(title = 'Chat Experience Leaderboard',color= discord.Color.purple())
        for member in guild.members:
            if str(member.id) in jsondata: 
                levels[jsondata[str(member.id)][3][0]] = str(member.id)
                levelsitems = levels.items()
                levelssorted = sorted(levelsitems,reverse=True)
                #print(levelssorted)
                xpleaderboard.add_field(name=f'Number {(amount+1)}',value=f'{member.mention} Experience Level {levelssorted[amount][0]}',inline = False)
                amount = amount + 1
                if amount == 4:
                    break
            else:
                #print(member)
                return
        
        await ctx.send(embed = xpleaderboard)
                
            
            



def setup(client):
    client.add_cog(LevelCommands(client))