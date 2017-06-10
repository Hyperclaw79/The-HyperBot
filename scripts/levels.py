import datetime
import json
import discord
import asyncio
import random
import PIL
import requests
from io import BytesIO
from scripts import profiles,currency
import collections
import functools

from functools import reduce
from PIL import ImageDraw, Image, ImageFont
from discord import utils
from discord.utils import find
from collections import defaultdict, OrderedDict

#ToDo: Ranks and Leaderboard - Global and Server

async def get_levels(self, message, user_id):
   msg_len = len(message.content.strip())
   modif = 1
   flag = False
   with open('bot_files/user_profiles.json', 'r+') as f:
          prof = json.load(f)
   with open('bot_files/users.json', 'r+') as f:
          datac = json.load(f)
   try:
      lvlu = int(prof[str(user_id)]['Level:'])
      xpu = int(prof[str(user_id)]['XP:'])
   except Exception as e:
      await profiles.make_profile(self,message.author)
      await asyncio.sleep(2)
      lvlu = 1
      xpu = 0
   mod = round(msg_len * 0.35)
   bias = 0
   targ_xp = lvlu * 700
   if mod > targ_xp:                       #For spammers
      d = defaultdict(int)
      for c in message.content.strip(''):
         d[c]+=1
      for i in d:
         if d[i] > 10:
            bias+=1			
      mod = mod * int(1/bias)
   xpu = xpu + mod
   try:
      prof[str(user_id)]['XP:'] = xpu
   except:
      await profiles.make_profile(self,message.author)
      prof[str(user_id)]['XP:'] = xpu
      #for some strange reason, i again get key error for the dict.	  
   if (xpu >= lvlu * 700):              #yay level up!
      lvlu += 1
      if lvlu != 1:                     #cause the bot will spam this message for level one XD
         try:
            await self.send_message(message.channel, "Congrats %s! You levelled up! You're now level %s" % (message.author.mention, lvlu))
         except:
            pass
      if lvlu % 5 == 0:
         flag = True
   if lvlu % 5 == 0 and flag == True:     #Milestone at levels of 5.
      flag = False
      try:
         roboty = prof[str(user_id)].get('Robotcoins',"0 :robot:")
      except:
         await profiles.make_profile(self,message.author)
         roboty = prof[str(user_id)].get('Robotcoins',"0 :robot:")
      roboty_getter = roboty.split(' ')[0]
      roboty_int = int(roboty_getter)
      roboty_int = roboty_int + 1
      roboty = str(roboty_int) + " :robot:"	  
      try:
         prof[str(user_id)]['robotcoin'] = roboty
         datac[str(user_id)]['robotcoin'] = roboty
      except:
         await profiles.make_profile(self,message.author)
         await currency.get_daily(self, message, author=message.author)
         prof[str(user_id)]['robotcoin'] = roboty
         datac[str(user_id)]['robotcoin'] = roboty
      await self.send_message(message.channel, "Congrats %s! You levelled up 5 times! Enjoy this Robotcoin. :robot: " % message.author.mention)
   targ_xp = lvlu * 700
   prof[str(user_id)]['Target:'] = targ_xp
   prof[str(user_id)]['Level:'] = lvlu
   dumpy = json.dumps(prof)
   with open('bot_files/user_profiles.json', 'w+') as f:
      f.write(dumpy) 
   dumpy = json.dumps(datac)
   with open('bot_files/users.json', 'w+') as f:
      f.write(dumpy)