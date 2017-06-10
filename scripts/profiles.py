import datetime
import json
import discord
import asyncio
import PIL
import requests

from io import BytesIO
from PIL import ImageDraw, Image, ImageFont
from discord import utils
from discord.object import Object
from discord.utils import find
from collections import defaultdict, OrderedDict

async def get_profile(self,message,author,user_mentions):
       """
       Usage:
           {command_prefix}profile[@user or none] 
			
       View your profile or a mentioned user's profile.
       """
       prof = OrderedDict()
       with open('bot_files/user_profiles.json', 'r+') as f:
          prof = json.load(f)
       if not user_mentions:
          userc = message.author
       else:
          userc = user_mentions[0]
       datac={}
       with open('bot_files/users.json', 'r+') as f:
          datac = json.load(f) 
       try:
          coiny = datac[str(userc.id)].get('coins',"100 :moneybag:")
          roboty = datac[str(userc.id)].get('robotcoin',"0 :robot:")
          timey = datac[str(userc.id)].get('timecheck',datetime.datetime.now().strftime('%B %d,%Y %H:%M:%S'))		  
       except:
          coiny = "100 :moneybag:"
          roboty = "0 :robot:"
          timey = datetime.datetime.now().strftime('%B %d,%Y %H:%M:%S')
       try:
          marryc = prof[str(userc.id)].get('Married To:',"Single.")
       except:
          marryc = "Single"
       bioc = prof[str(userc.id)].get('Bio',"Yet to show creativity.")
       namec = str(userc.name)
       statusc = str(userc.status)      
       accdate = userc.created_at.strftime('%B %d,%Y %H:%M:%S')
       avatarc = userc.avatar_url
       servdate = userc.joined_at.strftime('%B %d,%Y %H:%M:%S')
       servperms = str(userc.top_role)
       nicknames = str(userc.nick)
       rolesc = userc.roles
       rolest = []   
       for i in rolesc:
          rolest.append(i.name)
       rolest = ', '.join(rolest)		  
       gamey = str(userc.game)	 
       lvlc = int(prof[str(userc.id)].get('Level:',"1"))
       xpc = int(prof[str(userc.id)].get('XP:',"0"))
       xpt = int(prof[str(userc.id)].get('Target:',"700"))	   
       profl = [("Name",namec), ("Status",statusc), ("Account Created On",accdate), ("Joined Server on",servdate), ("Guild Level",servperms), ("Nickname",nicknames), ("Role List",rolest),("Married To:",marryc), ("Currently Playing",gamey), ("Bio",bioc), ("Hypercoins",coiny), ("Robotcoins",roboty), ("Daily last collected on",timey), ("Level:",lvlc), ("XP:",xpc), ("Target:",xpt)]
       prof[str(userc.id)] = OrderedDict(profl)
       dumpy = json.dumps(prof)
       with open('bot_files/user_profiles.json', 'w+') as f:
          f.write(dumpy)   		  
       bg = Image.open('images/prof_bg2.png').convert('RGBA')
       response = requests.get(avatarc)
       im = Image.open(BytesIO(response.content))
       im = im.resize((125,125))
       bg.paste(im,box=(636,180),mask = None)
       txt = Image.new('RGBA', bg.size, (255,255,255,0))
       fnt = ImageFont.truetype('arial.ttf', 16)
       fnt2 = ImageFont.truetype('segoesc.ttf', 20)
       fnt3 = ImageFont.truetype('JOKERMAN.TTF', 18)
       d = ImageDraw.Draw(txt)
       tt = ""	   
       tt2 = ""
       rep1 = prof[str(userc.id)]['Hypercoins'].replace(':moneybag:','Hypercoins')
       rep2 = prof[str(userc.id)]['Robotcoins'].replace(':robot:','Robotcoins')
       d.text((190,21), text = "%s's Profile:" % namec, font=fnt3, fill=(255,0,0,255), align = "left")
       d.text((87,31), text = str(lvlc), font=fnt2, fill=(255,0,0,255), align = "left")
       d.text((513,23), text = str(xpc), font=fnt, fill=(255,0,0,255), align = "left")
       d.text((511,56), text = str(xpt), font=fnt, fill=(255,0,0,255), align = "left")
       d.text((55,134), text = "Name:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((55,154), text = namec, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((55,184), text = "Status:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((55,204), text = statusc, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((55,234), text = "Account Created On:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((55,254), text = accdate, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((55,284), text = "Joined Server On:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((55,304), text = servdate, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((55,334), text = "Currently Playing:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((55,354), text = gamey, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((55,384), text = "Server Level:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((55,404), text = servperms, font=fnt, fill=(255,255,255,128), align = "left")
       
       d.text((328,134), text = "Nickname:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((328,154), text = nicknames, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((328,184), text = "Bio:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((328,204), text = bioc, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((328,234), text = "Married To:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((328,254), text = marryc, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((328,310), text = "Robotcoins:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((328,328), text = rep2, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((328,358), text = "Hypercoins:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((328,378), text = rep1, font=fnt, fill=(255,255,255,128), align = "left")
       d.text((328,408), text = "Daily last collected on:", font=fnt, fill=(255,255,255,255), align = "left")
       d.text((328,428), text = timey, font=fnt, fill=(255,255,255,128), align = "left")
       roundy = Image.open('images/circler.png').convert('RGBA')
       juice = Image.open('images/juice.png').convert('RGBA')
       bg.paste(roundy,box=(0,0),mask = roundy)
       x,y = juice.size
       ratio = xpc/xpt
       juice1 = juice.crop(box=(0,0,int(ratio * x),y))
       bg.paste(juice1,box=(174,61),mask = juice1)
       out = Image.alpha_composite(bg, txt)
       out.save('images/res.png')
       with open('images/res.png', 'rb') as fp:
          await self.send_file(message.channel,fp,content = "%s's Profile." % userc.display_name)	   
		  

async def get_setbio(self,message):
       """
       Usage:
           {command_prefix}setbio[your bio] 
			
       Update your bio in the profile.
       """	
       with open('bot_files/user_profiles.json', 'r+') as f:
          prof = json.load(f)
       bioc = message.content.strip()
       bioc = bioc.replace("H!setbio","")
       prof[str(message.author.id)]['Bio'] = bioc
       dumpy = json.dumps(prof)
       with open('bot_files/user_profiles.json', 'w+') as f:
          f.write(dumpy) 
       await self.delete_message(message)
       msg = await self.send_message(message.channel, "Done :thumbsup::skin-tone-1:")
       await asyncio.sleep(1)
       await self.delete_message(msg)

async def get_marry(self,message,user_mentions):
       """
       Usage:
           {command_prefix}marry[@user] 
			
       Marry a discord user.
       """	
       userc = user_mentions[0]
       with open('bot_files/user_profiles.json', 'r+') as f:
          prof = json.load(f)
       if message.author == userc:
          await self.send_message(message.channel, "Marrying your right hand isn't a valid thing ya know XD\n")
       elif (not prof.get(str(message.author.id)) or not prof.get(str(userc.id))):
          await self.send_message(message.channel,"You or they don't seem to have a profile in HyperRealm yet. Use H!profile to get a valid profile before marriage.\n")
       elif prof[str(message.author.id)]['Married To:'] == str(userc):
          await self.send_message(message.channel, "Hey %s, you're already married to %s !" % (message.author.mention, userc.mention))	
       elif userc.bot==True:
          await self.send_message(message.channel, "Hey %s, you can't marry a bot you despo!" % message.author.mention)	
       elif not(prof[str(userc.id)]['Married To:'] == "Single."):
          await self.send_message(message.channel, "Sorry %s, but %s is already married to %s. Ask them to get divorced first. :smiling_imp:" % (message.author.mention, userc.mention, prof[str(userc.id)]['Married To:']))   
       elif not(prof[str(message.author.id)]['Married To:'] == "Single."):
          await self.send_message(message.channel, "Hey %s! You are married to %s. Get divorced first, you cheater. =_=" % (message.author.mention, prof[str(message.author.id)]['Married To:']))    		  
       else:
          await self.send_message(message.channel,"Hey %s! %s has proposed to you. :ring: \n Type 'Accept' or 'Decline' to respond to their proposal. " % (userc.mention, message.author.mention))
          answer = await self.wait_for_message(author=userc)
          answer = answer.content.lower().strip()
          if ("accept" in answer) or ("yes" in answer):
             await self.send_message(message.channel, "Wow congrats %s and %s! You both are now married:heart_exclamation: Planning to kiss now? :smirk: " % (message.author.mention,userc.mention))
             marryem = discord.Embed(title='',description='',color=0)
             marryem.set_image(url="http://pa1.narvii.com/5853/5c7e481b8549c4c2c829e2061559a3834587a406_hq.gif")	
             await self.send_message(message.channel,content=None,embed=marryem)		  
             prof[str(userc.id)]['Married To:'] = str(message.author)
             prof[str(message.author.id)]['Married To:'] = str(userc)
             dumpy = json.dumps(prof)
             with open('bot_files/user_profiles.json', 'w+') as f:
                f.write(dumpy)
          else:
             await self.send_message(message.channel, "Awww %s, better luck next time!" % message.author.mention)	   
			 

async def get_divorce(self,message,user_mentions):
       """
       Usage:
           {command_prefix}marry[@user] 
			
       Divorce your husbando/waifu. Psst. Sorry to hear that btw.
       """	
       userc = user_mentions[0]
       with open('bot_files/user_profiles.json', 'r+') as f:
          prof = json.load(f)
       if not(prof[str(message.author.id)]['Married To:'] == str(userc)):
          await self.send_message(message_channel,"Hey %s! You're not even married to %s." % (message.author.mention, userc.mention))
       else:
          prof[str(userc.id)]['Married To:'] = "Single."
          prof[str(message.author.id)]['Married To:'] = "Single."
          await self.send_message(message.channel, "Awww %s, you've been divorced by %s. Here, have a cookie to cheer up: :cookie:" % (userc.mention, message.author.mention))
          dumpy = json.dumps(prof)
          with open('bot_files/user_profiles.json', 'w+') as f:
                f.write(dumpy)

async def make_profile(self,user):
       """
       Usage:
           {command_prefix}profile
       """
       prof = OrderedDict()
       with open('bot_files/user_profiles.json', 'r+') as f:
          prof = json.load(f)
       userc = user
       try:
          prof[str(user.id)] = prof.get(str(userc.id))
       except:
          datac={}
          with open('bot_files/users.json', 'r+') as f:
             datac = json.load(f)
          try:    
             coiny = datac[str(userc.id)]['coins']
             roboty = datac[str(userc.id)]['robotcoin']
             timey = datac[str(userc.id)]['timecheck']	   
          except:
             coiny = "1000 :moneybag:"
             roboty = "0 :robot:"
             timey = datetime.datetime.now().strftime('%B %d,%Y %H:%M:%S')
          try:
             bioc = prof[str(userc.id)]['Bio']
          except:		  
             bioc = "Yet to show creativity."
          try:
             marryc = prof[str(userc.id)]['Married To:']
          except:		  
             marryc = "Single."		  
          namec = str(userc.display_name)
          statusc = str(userc.status)      
          accdate = userc.created_at.strftime('%B %d,%Y %H:%M:%S')
          avatarc = userc.avatar_url
          servdate = userc.joined_at.strftime('%B %d,%Y %H:%M:%S')
          servperms = str(userc.top_role)
          nicknames = str(userc.nick)
          rolesc = userc.roles
          rolest = []   
          for i in rolesc:
             rolest.append(i.name)
          rolest = ', '.join(rolest)		  
          try:
             gamey = str(userc.game.name)	   
          except:
             gamey = discord.Game(name="None").name
          try:
             lvlc = int(prof[str(userc.id)].get('Level:',"1"))
             xpc = int(prof[str(userc.id)].get('XP:',"0"))
             xpt = int(prof[str(userc.id)].get('Target:',"700"))	   
          except:
             lvlc = 1
             xpc = 0
             xpt = 700
          profl = [("Name",namec), ("Status",statusc), ("Account Created On",accdate), ("Joined Server on",servdate), ("Guild Level",servperms), ("Nickname",nicknames), ("Role List",rolest),("Married To:",marryc), ("Currently Playing",gamey), ("Bio",bioc), ("Hypercoins",coiny), ("Robotcoins",roboty), ("Daily last collected on",timey), ("Level:",lvlc), ("XP:",xpc), ("Target:",xpt)]
          prof[str(userc.id)] = OrderedDict(profl)
       dumpy = json.dumps(prof)
       with open('bot_files/user_profiles.json', 'w+') as f:
          f.write(dumpy)   		  

#mass creation of profiles:		  
async def get_create_profs(self, message):
   for memberc in message.server.members:
      await make_profile(self, memberc)
   await self.send_message(message.channel, "Done! :thumbsup::skin-tone-1: ")
   
async def get_serv_profs(self, server):
   for memberc in server.members:
      await make_profile(self, memberc)
   await self.send_message(server.default_channel, "Thanks for adding me! :metal::skin-tone-1:  ")