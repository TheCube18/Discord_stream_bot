import discord
from discord.ext import commands
import json


with open('setting.json','r',encoding ='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = '')

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_message(msg):

    

    if msg.content in jdata['KEYWORD']:
        await msg.delete()




        embed=discord.Embed()
        embed.set_author(name= msg.author.name, icon_url=  msg.author.avatar_url)
        embed.add_field(name="Now playing", value = "   ", inline=True)
        await msg.channel.send(embed=embed)
     





      

bot.run(jdata['TOKEN'])

