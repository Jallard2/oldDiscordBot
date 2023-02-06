import discord
from discord.ext import commands
import random
import json
import asyncio
from pretty_help import DefaultMenu, PrettyHelp
import datetime

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

command_prefix = '?'

menu = DefaultMenu('◀️', '▶️', '❌')
help_command = None
client = commands.Bot(command_prefix=command_prefix,description = 'Bot Created by <@462291477964259329> As A Testing Project',intents = intents,help_command = help_command)
client.help_command = PrettyHelp(navigation=menu, color=discord.Colour.purple(),active_time = 30, delete_after_timeout = True) 

initial_extensions = ['cogs.generalcommands','cogs.statscommands','cogs.managementcommands','cogs.economycommands','cogs.levelcommands']
if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)
    print('Finished Loading All Cogs')

url = 'http://google.com'

@client.event
async def on_ready():
    print('Bot is Online')
    await client.change_presence(activity=discord.Game(name='Day 3'))

@client.event    
async def on_member_join(member):
    Warns = 0
    RPSwin = 0
    RPStie = 0
    RPSloss = 0
    RPSStats = [RPSwin, RPStie, RPSloss]
    Money = 0
    Level = 1
    xp = 0
    nickname = "Placeholder"

    with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
        jsondata = json.load(f)
        if str(member.id) not in jsondata:
            print('A New Player Has Joined')
            author = member.id
            print(str(member.id))
            newdata = {author:[RPSStats, Warns, Money,[Level, xp]]}
            print(newdata)
            jsondata.update(newdata) 
        
    with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
        json.dump(jsondata,f)
        print(jsondata)
    
    
    with open(r'D:\Programs\NewDiscordBot\discordBotSamples\nicknames.json','r') as f:
        jsondata = json.load(f)
        print(jsondata)
        if str(member.id) not in jsondata:
            author = member.id
            newdata = {author:[nickname]}
            jsondata.update(newdata)
    
    with open(r'D:\Programs\NewDiscordBot\discordBotSamples\nicknames.json','w') as f:
        json.dump(jsondata,f)
        print(jsondata)


@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        cd = round(error.retry_after)
        timeleft = str(datetime.timedelta(seconds = cd))
        cdembed = discord.Embed(title =f'That Command is Still on Cooldown. You Can Use it Again In {timeleft}.',color = discord.Color.purple())
        await ctx.message.delete()
        await ctx.send(embed = cdembed)
    elif isinstance(error,commands.CommandError):
        print(error)
    else:
        print(error)


@client.event
async def on_message(message):
    if message.author !=client.user:
        if message.channel != message.author.dm_channel:
            #print(message.channel)
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
                jsondata = json.load(f)
                #print(jsondata[str(message.author.id)][3][1])
                jsondata[str(message.author.id)][3][1] = jsondata[str(message.author.id)][3][1] + 5 #Player Gains 5 Xp Per Message Sent
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                json.dump(jsondata,f)
            
            #Leveling Up System
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','r') as f:
                    jsondata = json.load(f)
                    currentlevel = jsondata[str(message.author.id)][3][0]
                    xpneededforlevel = (currentlevel * 30) + 15
                    currentxp = jsondata[str(message.author.id)][3][1]
                    if currentxp >= xpneededforlevel:
                        jsondata[str(message.author.id)][3][0] = jsondata[str(message.author.id)][3][0] + 1
                        jsondata[str(message.author.id)][3][1] = 0
                        await message.channel.send(f'Congrats {message.author.mention}! You Have Leveled Up To Level {jsondata[str(message.author.id)][3][0]}')
                        with open(r'D:\Programs\NewDiscordBot\discordBotSamples\Information.json','w') as f:
                            json.dump(jsondata,f)
            
    
    await client.process_commands(message)          

@client.event
async def on_voice_state_update(member, before, after):
    SeniorStaffWaitingRoomID = 933789149251657828
    if after.channel is not None:
        if after.channel.id == SeniorStaffWaitingRoomID:
            await member.send("What Realm/Topic Is Your Issue Relating To")
            lastmessage = await client.wait_for('message', check = lambda x: x.channel == member.dm_channel and x.author == member, timeout=30)
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\nicknames.json','r') as f:
                nicknamedata = json.load(f)
                nicknamedata[str(member.id)][0] = member.display_name
                print(nicknamedata[str(member.id)])
    
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\nicknames.json','w') as f:
                json.dump(nicknamedata,f)
                print(nicknamedata)
                nick = member.display_name + "-" + lastmessage.content
                await member.edit(nick=nick)

    if before.channel is not None:
        if before.channel.id == SeniorStaffWaitingRoomID:
            with open(r'D:\Programs\NewDiscordBot\discordBotSamples\nicknames.json','r') as f:
                    nicknamedata = json.load(f)
            nick = nicknamedata[str(member.id)][0]
            await member.edit(nick=nick)

                
    


client.run('TOKEN')
