from discord.ext import commands
import json
import discord

class StatsCommands(commands.Cog, name='Stats Commands',description='Commands Relating To Stats'):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clearrps(self,ctx,userid=None):
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            guild = ctx.guild
            memberlist = guild.members
            for member in guild.members:
                author = member.id
                #print(jsondata)
                if str(author) in jsondata:
                    jsondata[str(author)][0][0] = 0
                    jsondata[str(author)][0][1] = 0
                    jsondata[str(author)][0][2] = 0
                    with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                        json.dump(jsondata,f)
                        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clearwarns(self,ctx,userid:discord.Member=None):
        logchannel = self.client.get_channel(int(923710173707644990))
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            guild = ctx.guild
            if userid == None:
                memberlist = guild.members
                for member in guild.members:
                    author = member.id
                    if str(author) in jsondata:
                        jsondata[str(author)][1] = 0
                        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                            json.dump(jsondata,f)
                        unwarnembed = discord.Embed(title='All Players Have Had Their Warns Cleared',description=f'{ctx.message.author.mention} Has Cleared The Warnings of All Players',color = discord.Color.purple())
                        await logchannel.send(embed = unwarnembed)
            else:
                jsondata[str(userid.id)][1] = 0
                unwarnembed = discord.Embed(title='A Player Has Had Their Warns Cleared',description=f'{ctx.message.author.mention} Has Cleared The Warnings of {userid.mention}',color = discord.Color.purple())
                await logchannel.send(embed = unwarnembed)
                with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                    json.dump(jsondata,f)
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def cleareco(self,ctx,userid:discord.Member=None):
        logchannel = self.client.get_channel(int(923710173707644990))
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            guild = ctx.guild
            memberlist = guild.members
            if userid == None:
                for member in guild.members:
                    if str(member.id) in jsondata:
                        jsondata[str(member.id)][2] = 0
                        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                            json.dump(jsondata,f)
                        cleareco = discord.Embed(title='All Players Have Had Their Economy Set To 0',description=f'{ctx.message.author.mention} Has Reset The Economy of All Players',color = discord.Color.purple())
                        await logchannel.send(embed = cleareco)
            else:
                jsondata[str(userid.id)][2] = 0
                cleareco = discord.Embed(title='A Player Has Had Their Economy Set To 0',description=f'{ctx.message.author.mention} Has Rest The Economy of {userid.mention}',color = discord.Color.purple())
                await logchannel.send(embed = cleareco)
                with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                    json.dump(jsondata,f)
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clearlevels(self,ctx,userid:discord.Member=None):
        logchannel = self.client.get_channel(int(923710173707644990))
        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
            jsondata = json.load(f)
            guild = ctx.guild
            memberlist = guild.members
            if userid == None:
                for member in guild.members:
                    if str(member.id) in jsondata:
                        jsondata[str(member.id)][3][0] = 1
                        jsondata[str(member.id)][3][1] = 0
                        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                            json.dump(jsondata,f)
                        clearlevels = discord.Embed(title='All Players Have Had Their Chat Experience Set To 0',description=f'{ctx.message.author.mention} Has Reset The Chat Experience of All Players',color = discord.Color.purple())
                        await logchannel.send(embed = clearlevels)
            else:
                jsondata[str(userid.id)][3][0] = 1
                jsondata[str(userid.id)][3][1] = 0
                clearlevels = discord.Embed(title='A Player Has Had Their Chat Experience Set To 0',description=f'{ctx.message.author.mention} Has Rest The Chat Experience of {userid.mention}',color = discord.Color.purple())
                await logchannel.send(embed = clearlevels)
                with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                    json.dump(jsondata,f)
    
    @commands.command()
    @commands.is_owner()
    async def clearall(self,ctx,userid:discord.Member=None):
        await ctx.message.delete()
        await ctx.invoke(self.client.get_command('cleareco'), userid=userid)
        await ctx.invoke(self.client.get_command('clearrps'), userid=userid)
        await ctx.invoke(self.client.get_command('clearlevels'), userid=userid)
        await ctx.invoke(self.client.get_command('clearwarns'), userid=userid)
        
        
        
        

def setup(client):
    client.add_cog(StatsCommands(client))