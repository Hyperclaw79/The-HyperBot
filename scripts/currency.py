import datetime
import json
import discord
import asyncio
import traceback
import random

from discord import utils
from discord.utils import find

from datetime import timedelta

#ToDo: Completely delete users.json and use only user_profiles.json

async def get_daily(self, message, author):                                #H!daily
       """
       Usage:
           {command_prefix}daily 
			
       Collect 100 Hypercoins everday.
       """
       datac={}
       with open('bot_files/users.json', 'r+') as f:
          datac = json.load(f)
       if not datac.get(str(author.id)):
          coiny = str(100) + " :moneybag:" 
          timey = datetime.datetime.now().strftime('%H:%M:%S')
          datac[str(author.id)] = {'name':author.name, 'coins' : coiny, 'robotcoin' : '0 :robot:', 'timecheck': timey}
          dumpy = json.dumps(datac)
          with open('bot_files/users.json', 'w+') as f:
             f.write(dumpy)  
          await self.send_message(message.channel, "Hey congrats %s! You just received your first 100 Hypercoins! Your current balance is: 100 :moneybag:." % author.mention)
       else:
          timey = datetime.datetime.now().strftime('%H:%M:%S')
          timey = datetime.datetime.strptime(timey,'%H:%M:%S')
          timey2 = datac[str(author.id)]['timecheck']
          timey2 = datetime.datetime.strptime(timey2,'%H:%M:%S')
          timediff = timey - timey2
          timediff = str(timediff)
          hours = timediff.split(':')[0]
          try:
             hours = int(hours)
          except:
             hours = hours.split(',')[1].strip()
             hours = int(hours)
          hour = str((24 - hours)-1)
          minutes = timediff.split(':')[1]
          minutes = int(minutes)
          minute = str(60 - minutes)
          seconds = timediff.split(':')[2]
          seconds = int(seconds)
          second = str(60 - seconds)
          if ((60 * hours + minutes) > 3600) or (message.author.id == self.config.owner_id):         #check for 24hrs completion
             coiny = datac[str(author.id)]['coins']
             roboty = datac[str(author.id)]['robotcoin']
             coiny_getter = coiny.split(' ')[0]
             coiny_int = int(coiny_getter)
             coiny_int = coiny_int + 100
             coiny = str(coiny_int) + " :moneybag:"
             datac[str(author.id)]['coins'] = coiny
             timey1 = timey + timedelta(hours=24)
             timey1 = timey1.strftime('%H:%M:%S') 
             datac[str(author.id)]['timecheck'] = timey1
             dumpy = json.dumps(datac)
             with open('bot_files/users.json', 'w+') as f:
                f.write(dumpy)
             await self.send_message(message.channel, "Hey %s, you successfully collected your 100 Hypercoins. Your current balance is: %s." % (author.mention, coiny))  
             await coin_exchange(self,message,message.author,coiny_int)
          else:
             await self.send_message(message.channel, "Hold on %s! You still have %s hours %s minutes and %s seconds before you can collect your daily Hypercoins." % (message.author.mention, hour, minute, second))
			   
async def get_checkbalance(self, message):
       """
       Usage:
           {command_prefix}checkbalance
			
       Check your account balance.
       """
       await self.send_message(message.channel, "Accessing your account %s:........... :credit_card: \n" % message.author.mention)
       datac={}
       with open('bot_files/users.json', 'r+') as f:
          datac = json.load(f)
       roboty = datac[str(message.author.id)].get('robotcoin')
       coiny = datac[str(message.author.id)].get('coins')
       coiny_getter = coiny.split(' ')[0]
       coiny_int = int(coiny_getter)	   
       loadem = discord.Embed(title='Authorizing', description='' , color=0)
       loadem.set_image(url='https://s-media-cache-ak0.pinimg.com/originals/9b/2b/2a/9b2b2a3a89e55d72d0bd6657cf7c6fd2.gif')
       lem = await self.send_message(message.channel, content=None, embed=loadem)
       await asyncio.sleep(5)
       await self.delete_message(lem)
       if coiny_int < 1:
          await self.send_message(message.channel, "Hey %s, you don't seem to have an account in HyperRealm. Type H!daily to get one now.\n" % message.author.mention)
       else:
          await self.send_message(message.channel, "Hey %s, your current balance is: %s and %s." % (message.author.mention, coiny, roboty))			   
			   
       await coin_exchange(self,message,message.author,coiny_int)	
		
async def get_transfer(self, message, amt, user_mentions):
       """
       Usage:
           {command_prefix}transfer[@user]
			
       Feeling generous? Transfer Hypercoins to another user.
       """
       datac={}
       with open('bot_files/users.json', 'r+') as f:
          datac = json.load(f)	
       coiny = datac[str(message.author.id)].get('coins')
       coiny_getter = coiny.split(' ')[0]
       coiny_int = int(coiny_getter)
       if coiny_int < 1:
          await self.send_message(message.channel, "Hey %s, you don't seem to have an account in HyperRealm. Type H!daily to get one now.\n" % message.author.mention)
       elif coiny_int < int(amt):
          await self.send_message(message.channel, "Hey %s, you have insufficient funds.\n" % message.author.mention)
       else:
          user = user_mentions[0]
          if user == message.author:
             await self.send_message(message.channel, "Hey %s, you can't transfer to yourself." % message.author.mention)
          if user.bot == True:
             await self.send_message(message.channel, "Hey %s, bots don't have bank accounts." % message.author.mention)
          r = random.randint(1000,9999)
          await self.send_message(message.channel, "Hey %s, are you sure you wanna transfer %s Hypercoins to %s?\n" % (message.author.mention, amt, user.mention))
          mrep = await self.wait_for_message(author=message.author)
          mrep = mrep.content.lower().strip()
          if ("yes" in mrep) or ("yea" in mrep):
             await self.send_message(message.channel, "%s, Please enter the following pin:\n%s" % (message.author.mention, r))
             mrep1 = await self.wait_for_message(author=message.author)
             mrep1 = mrep1.content.lower().strip()
             if int(mrep1) == r:                                               #Should I change this to a reaction based input?
                loadem = discord.Embed(title='Transferring', description='' , color=0)
                loadem.set_image(url='https://s-media-cache-ak0.pinimg.com/originals/9b/2b/2a/9b2b2a3a89e55d72d0bd6657cf7c6fd2.gif')
                lem = await self.send_message(message.channel, content=None, embed=loadem)
                await asyncio.sleep(5)
                await self.delete_message(lem)			 
                coiny1 = datac[str(message.author.id)]['coins']
                coiny_getter = coiny1.split(' ')[0]
                coiny_int = int(coiny_getter)
                coiny_int = coiny_int - int(amt)
                if coiny_int < 1:
                   coiny_int = 1
                coiny = str(coiny_int) + " :moneybag:"
                datac[str(message.author.id)]['coins'] = coiny
                if not datac.get(str(user.id)):
                   coiny1 = amt + " :moneybag:" 
                   datac[str(user.id)] = {'name': user.name, 'coins' : coiny1, 'robotcoin' : '0 :robot:', 'timecheck': '24 hours'}
                else:
                   coiny1 = datac[str(user.id)]['coins']
                   coiny_getter = coiny1.split(' ')[0]
                   coiny_int = int(coiny_getter)
                   coiny_int = coiny_int + int(amt)
                   coiny1 = str(coiny_int) + " :moneybag:"
                   datac[str(user.id)]['coins'] = coiny1
                dumpy = json.dumps(datac)
                with open('bot_files/users.json', 'w+') as f:
                   f.write(dumpy)
                await self.send_message(message.channel, "`Transaction Complete!`")
                await self.send_message(message.channel, "Now %s, your current balance is: %s." % (message.author.mention, coiny))
                await self.send_message(message.channel, "Now %s, your current balance is: %s." % (user.mention, coiny1))
	
async def get_buy_horse(self, message):                            #To give a slight edge in the race. Not an OP boost.
   user = message.author
   await self.send_message(message.channel, "`Would you like to purchase a horse? It will give you an edge in the races.\n1. Yes\n2. No`")
   reply = await self.wait_for_message(author=message.author)
   reply = reply.content.strip().lower()
   if "no" in reply:
      await self.send_message(message.channel, "Maybe next time then. :wave:")
   elif "yes" in reply or "yea" in reply or "sure" in reply or "okay" in reply or "1" in reply:
      await self.send_message(message.channel, "`Which horse would you like to buy?\n1. Normal for 1 Robotcoin\n2. Premium for 5 Robotcoins`\n")
      rep2 = await self.wait_for_message(author=message.author)
      rep2 = rep2.content.strip().lower()
      if "1" in rep2 or "normal" in rep2:
         type = "Normal"
      elif "2" in rep2 or "premium" in rep2:
         type = "Premium"	  
      m1 = await self.send_message(message.channel, "`Alright, checking balance....\n`")
      await asyncio.sleep(1)	  
      await self.delete_message(m1)      
      loadem = discord.Embed(title='Accessing', description='' , color=0)
      loadem.set_image(url='https://s-media-cache-ak0.pinimg.com/originals/9b/2b/2a/9b2b2a3a89e55d72d0bd6657cf7c6fd2.gif')
      lem = await self.send_message(message.channel, content=None, embed=loadem)
      await asyncio.sleep(5)
      await self.delete_message(lem)
      datac={}
      with open('bot_files/users.json', 'r+') as f:
         datac = json.load(f)	
      roboty = datac[str(message.author.id)].get('robotcoin')
      roboty_getter = roboty.split(' ')[0]
      roboty_int = int(roboty_getter)
      horsec = {}	  
      horsec[str(user.id)]={}
      if ((roboty_int<1 and type=="Normal") or (roboty_int<5 and type=="Premium")):
         await self.send_message(message.channel, "`Insufficient funds.`\n")
      else:
         if type == "Normal":
            roboty_int -= 1
            horsec[str(user.id)]['Horse'] = "Normal"
         else:
            roboty_int -= 5
            horsec[str(user.id)]['Horse'] = "Premium"
         roboty = str(roboty_int)+" :robot:"      
         datac[str(user.id)]['robotcoin'] = roboty
         dumpy = json.dumps(datac)
         with open('bot_files/users.json', 'w+') as f:
            f.write(dumpy)
         dumpy = json.dumps(horsec)
         with open('bot_files/horses.json', 'w+') as f:                                          #buying a new horse will replace the old one. 
            f.write(dumpy)
         await self.send_message(message.channel, "You've successfully purchased a %s horse! Go Ace those Races now!" % type)			
		 
async def coin_exchange(self,message,user,param):
   if coiny_int > 1000:                       #1RC = 1k HC
      await self.send_message(message.channel, "%s You have more than 1000 Hypercoins. Would you like to exchange them for Robotcoins?\nReply 'Yes' or 'No':\n" % author.mention)
      mrep = await self.wait_for_message(author=user)
      mrep = mrep.content.lower().strip()
      if mrep.startswith('yes') or mrep.startswith('h!yes'):
         coiny_int = coiny_int - 1000
         coiny = str(coiny_int) + " :moneybag:"
         datac[str(user.id)]['coins'] = coiny
         roboty_getter = roboty.split(' ')[0]
         roboty_int = int(roboty_getter)
         roboty_int = roboty_int + 1
         roboty = str(roboty_int) + " :robot:"
         datac[str(user.id)]['robotcoin'] = roboty
         dumpy = json.dumps(datac)
         with open('bot_files/users.json', 'w+') as f:
            f.write(dumpy)   				
         await self.send_message(message.channel, "Hey %s, your current balance is: %s and %s." % (author.mention, roboty, coiny))   
      else:
         await self.send_message(message.channel, "Maybe next time then. :wave:")