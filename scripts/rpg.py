import datetime
import json
import discord
import asyncio
import random
import PIL
import requests
import collections
import functools

from io import BytesIO

      
from functools import reduce
from PIL import ImageDraw, Image, ImageFont
from discord import utils
from discord.utils import find, get
from collections import defaultdict, OrderedDict

#ToDo: Stats Display,  JSON/TXT file for storing storyline for each class and user, Items creation, Missions creation, Ranks and Leaderboard, Player Market for Malware, Mission related Anims and gifs.


def generate_ip(self,router=None,network=None):        #static ip
   a = str(random.randint(10,127))
   b = str(random.randint(0,255))
   c = str(random.randint(0,255))
   d = str(random.randint(2,255))
   if router != None:
      d = 1
   if network != None:
      d = 0
   l = [a,b,c,d]
   s = '.'.join(l)
   return s   

async def assign_ip(self,message):                      #dynamic ip
   msg = await self.send_message(message.channel,"0.0.0.0")
   for i in range(random.randint(1,5)):
      a = str(random.randint(10,127))
      for j in range(random.randint(0,3)):
         b = str(random.randint(0,255))
         for k in range(random.randint(0,3)):
            c = str(random.randint(0,255))
            for m in range(random.randint(0,3)):
               d = str(random.randint(2,255))
               l = [a,b,c,d]
               st = '.'.join(l)
               await self.edit_message(msg,"```ml\n%s```" % st)
   await self.delete_message(msg)
   await self.send_message(message.channel,"Your new IP address is: ```ml\n%s```" % st)
			  
async def get_create_character(self,message):
   with open('images/hckr_bg3.png', 'rb') as fp:
      msg = await self.send_file(message.channel,fp,content="`Choose a Role:`")
   servc = self.get_server(id="261133451762204674")                                      #custom emojis saved in my server.
   await self.add_reaction(msg, get(servc.emojis, name = 'vir'))                         #using reactions as input
   await self.add_reaction(msg, get(servc.emojis, name = 'socialengineer'))
   await self.add_reaction(msg, get(servc.emojis, name = 'btc'))
   chosen = ""
   while True:
      rctn = await self.wait_for_reaction(user=message.author)
      if rctn[0].emoji == get(servc.emojis, name = 'vir'):
         chosen = "Masterminds of Malware" 
         break		 
      elif rctn[0].emoji == get(servc.emojis, name = 'socialengineer'):
         chosen = "Silvertongued Social Engineers"
         break
      elif rctn[0].emoji == get(servc.emojis, name = 'btc'):
         chosen = "Bitcoin Breakers"
         break
      else:
         await self.send_message(message.channel, "Please choose a valid Class.")   
         pass
         await asyncio.sleep(2)
   if chosen == "Masterminds of Malware":
      skill = 5
      btc = 0
      bkdr = 5
      risk = 7
      modif = 1.5
      color = "```Diff\n-%s```" % chosen 
   if chosen == "Silvertongued Social Engineers":
      skill = 3
      btc = 5000
      bkdr = 2
      risk = 2
      modif = 1
      color = "```md\n# %s```" % chosen
   if chosen == "Bitcoin Breakers":
      skill = 1
      btc = 50000
      bkdr = 0
      risk = 4
      modif = 0.75 	  
      color = "```ml\n%s```" % chosen 
   await self.send_message(message.channel, "Congrats %s! You're now a hacker of class:%s" % (message.author.mention, color))
   bootem = discord.Embed(Title="",Description="",Color=0x000000)
   bootem.set_image(url="http://orig00.deviantart.net/48a7/f/2014/292/0/e/0e1335790f13a0986ea1496000ff4686-d7mv1gp.gif")
   msg = await self.send_message(message.channel,content=None,embed=bootem)
   await asyncio.sleep(8)
   await self.delete_message(msg)
   while True:
      await self.send_message(message.channel, "Now %s, enter a username:" % message.author.mention)
      blinkem = discord.Embed(Title="",Description="",Color=0x000000)
      blinkem.set_image(url="http://wes.is/content/images/2015/02/ezgif-com-crop.gif")
      msg = await self.send_message(message.channel,content=None,embed=blinkem)
      username = await self.wait_for_message(author=message.author)
      username = username.content
      await self.delete_message(msg)
      await self.send_message(message.channel, "**Confirm `%s` as username?**\n```prolog\n1.Yes``````ml\n2.No```" % username)   
      rep   = await self.wait_for_message(author=message.author)
      if "1" in rep.content or "Y" in rep.content:
         break
      else:
         pass
   await self.send_message(message.channel,"Welcome to HyperRPG, `%s`!" % username)
   with open('bot_files/rpg/rpg.json','r') as f:
      rpg_dict = json.load(f)
   rpgl = [("Name:",str(message.author.display_name)),("Username:",username),("Role:",chosen),("Level:",1),("XP:",0),("Modifier:",modif),("Hacking Skill:",skill),("Bitcoins:",btc),("Backdoor Creation:",bkdr),("Risk:",risk),("Heat:",0),("Reputation:","__Script Kiddie__")]
   rpg_dict[str(message.author.id)] = OrderedDict(rpgl)
   dumpy = json.dumps(rpg_dict)
   with open('bot_files/rpg/rpg.json','w+') as f:
      f.write(dumpy)   
	  
   #async def get_stats(self, message):
  
     