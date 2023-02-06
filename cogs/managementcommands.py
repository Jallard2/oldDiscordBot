from discord.ext import commands
import random
import json
import os
import discord
import asyncio

class ManagementCommands(commands.Cog, name='Management Commands',description='Commands For Mods And Above'):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self,ctx,userid:discord.Member,*,reason=None):
        logchannel = self.client.get_channel(int(923710173707644990))
        if reason == None:
            user = ctx.message.author
            await user.send('Please Include a Reason For This Punishment')
        else:
            try: 
                await userid.send(f'You Have Been Kicked From {ctx.guild.name} For {reason}')
            except:
                pass
            kickembed = discord.Embed(title=f'A Player Has Been Kicked',description=f'{ctx.message.author.mention} has Kicked {userid.mention} For {reason}',color=discord.Color.purple())
            await ctx.message.delete()
            await logchannel.send(embed=kickembed)
            await userid.kick(reason=reason)
    
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self,ctx,amount,*,reason='No Reason Specified'): 
        logchannel = self.client.get_channel(int(923710173707644990))
        await ctx.channel.purge(limit=int(amount))
        #await ctx.message.author.send(f'You Have Cleared {int(amount):,} messages in {ctx.channel.mention}')
        clearembed = discord.Embed(title='Messages Have Been Cleared',description=f'{ctx.message.author.mention} has Cleared {int(amount):,} messages in the Chanel {ctx.channel.mention}',color = discord.Color.purple())
        await logchannel.send(embed=clearembed)
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx,userid:discord.Member,*,reason=None):
        logchannel = self.client.get_channel(int(923710173707644990))
        if reason == None:
            user = ctx.messsage.author
            await user.send('Please Include a Reason For This Punishment')
        else:
            try: 
                await userid.send(f'You Have Been Banned From {ctx.guild.name} For {reason}')
            except:
                pass
            banembed = discord.Embed(title='A Player Has Been Banned',description=f'{ctx.message.author.mention} has Banned {userid.mention} For {reason}',color = discord.Color.purple())
            await ctx.message.delete()
            await logchannel.send(embed=banembed)
            await userid.ban(reason=reason)
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def preban(self,ctx,userid,*,reason='Preventative Ban'):
        if '@' in userid:
            await ctx.message.author.send('Please Just Put The Id of The User Without Anything Else For This Punishment')
        else:
            logchannel = self.client.get_channel(int(923710173707644990))
            prebanembed = discord.Embed(title='A Player Has Been Prebanned',description=f'{ctx.message.author.mention} has Prebanned <@{userid}> For {reason}',color = discord.Color.purple())
            await logchannel.send(embed=prebanembed)
            user = await self.client.fetch_user(int(userid))
            await ctx.guild.ban(user,reason=reason)
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def warn(self,ctx,userid:discord.Member,*,reason=None):
        logchannel = self.client.get_channel(int(923710173707644990))
        if reason == None:
            await ctx.message.author.send('Please Include a Reason For This Punishment')
        else: 
            warnembed = discord.Embed(title='A Player Has Been Warned',description=f'{ctx.message.author.mention} has Warned {userid.mention} For {reason}.',color = discord.Color.purple())
            await logchannel.send(embed=warnembed)
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
                jsondata = json.load(f)
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                #print(jsondata[str(userid.id)][1])
                jsondata[str(userid.id)][1] = jsondata[str(userid.id)][1] + 1
                try: 
                    await userid.send(f'You Have Been Warned For {reason}. This is Warning Number {jsondata[str(userid.id)][1]}. Please Make Sure That You Read The Rules To Prevent Getting Any More Warnings')
                except:
                    pass
                json.dump(jsondata, f)
        
        if jsondata[str(userid.id)][1] == 5:
            await ctx.invoke(self.client.get_command('ban'), userid=userid,reason='Too Many Warnings')
        elif 3<= jsondata[str(userid.id)][1] <= 4:
            await ctx.invoke(self.client.get_command('kick'), userid=userid,reason='Too Many Warnings')
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def warns(self,ctx,userid:discord.Member):
        logchannel = self.client.get_channel(int(923710173707644990))
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
                jsondata = json.load(f)
        amountofwarns = jsondata[str(userid.id)][1]
        warnsamount = discord.Embed(title = 'Player Warnings',description = f'{userid.mention} Has Been Warned {amountofwarns} Times')
        await logchannel.send(embed = warnsamount)
        
        
                

def setup(client):
    client.add_cog(ManagementCommands(client))