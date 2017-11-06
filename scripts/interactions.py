import discord
import random

from random import choice
from discord import utils
from discord.utils import find
from googleapiclient.discovery import build


#ToDO: gifs like Miki and Kawaibot.

class Gifs:
   def __init__(self):
      self.punchlist = []
      self.kicklist = []
      self.kisslist = []
      self.patlist = []
      self.huglist = []
      self.shootlist = []  
   
   def set_punch(self,giflist):
      self.punchlist = giflist   
   
   def set_kick(self,giflist):
      self.kicklist = giflist
   
   def set_kiss(self,giflist):
      self.kisslist = giflist	  
   
   def set_pat(self,giflist):
      self.patlist = giflist

   
   def set_hug(self,giflist):
      self.huglist = giflist	  

   def set_shoot(self,giflist):
      self.shootlist = giflist
	  
def giffetcher(interaction):
    my_api_key = "AIzaSyAishFW1txIAPKkBJSEZ9lAHtwKa4qN4dc"
    my_cse_id = "005813838392370806768:primejbnnqs"

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, searchType="image", fileType="gif", cx=cse_id, **kwargs).execute()
        return res['items']

    query = "anime+"
    query = query + interaction
    results = google_search(
        query, my_api_key, my_cse_id, num=10)
    giflist = []
    for result in results:
        giflist.append(result['link'])
    return giflist

gifs = Gifs()	
	
async def get_punch(self, message, user_display_names):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot punch someone. :P		
    """ 
    action = message.author.display_name + " punches the shit outta " + user_display_names[0].display_name	
    
    if gifs.punchlist == []:
       gifs.punchlist = giffetcher("punch")
    relv = gifs.punchlist[random.randint(0,len(gifs.punchlist)-1)]	
    puncher = discord.Embed(title=action,description="",color=7995392)
    puncher.set_image(url=relv)
    await self.send_message(message.channel,content=None,embed=puncher) 
   
async def get_kick(self, message, user_display_names):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot kick someone. :P		
    """ 
    action = message.author.display_name + " karate kicks " + user_display_names[0].display_name + " to submission."	
    if gifs.kicklist == []:
       gifs.kicklist = giffetcher("kick")
    relv = gifs.kicklist[random.randint(0,len(gifs.kicklist)-1)]	
    kicker = discord.Embed(title=action,description="",color=7995392)
    kicker.set_image(url=relv)
    await self.send_message(message.channel,content=None,embed=kicker)

async def get_shoot(self, message, user_display_names):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot shoot someone. :P		
    """ 
    action = message.author.display_name + " locks, loads and shoots " + user_display_names[0].display_name	
    if gifs.shootlist == []:
       gifs.shootlist = giffetcher("shoot")
    relv = gifs.shootlist[random.randint(0,len(gifs.shootlist)-1)]	
    shooter = discord.Embed(title=action,description="",color=7995392)
    shooter.set_image(url=relv)
    await self.send_message(message.channel,content=None,embed=shooter)
	
async def get_pat(self, message, user_display_names):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot pat someone. :P		
    """ 
    action = message.author.display_name + " gives " + user_display_names[0].display_name + " an endearing pat."
    if gifs.patlist == []:
       gifs.patlist = giffetcher("pat")
    relv = gifs.patlist[random.randint(0,len(gifs.patlist)-1)]		
    patter = discord.Embed(title=action,description="",color=7995392)
    patter.set_image(url=relv)
    await self.send_message(message.channel,content=None,embed=patter)
   
async def get_hug(self, message, user_display_names):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot hug someone. :P		
    """ 
    action = message.author.display_name + " warmly hugs " + user_display_names[0].display_name	
    if gifs.huglist == []:
       gifs.huglist = giffetcher("hug")
    relv = gifs.huglist[random.randint(0,len(gifs.huglist)-1)]		
    hugger = discord.Embed(title=action,description="",color=7995392)
    hugger.set_image(url=relv)
    await self.send_message(message.channel,content=None,embed=hugger)
   
async def get_kiss(self, message, user_display_names):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot kiss someone. :P		
    """ 
    action = message.author.display_name + " passionately kisses " + user_display_names[0].display_name + " and blushes."	
    if gifs.kisslist == []:
       gifs.kisslist = giffetcher("kiss")
    relv = gifs.kisslist[random.randint(0,len(gifs.kisslist)-1)]		
    kisser = discord	.Embed(title=action,description="",color=7995392)
    kisser.set_image(url=relv)
    await self.send_message(message.channel,content=None,embed=kisser)
	
async def get_flip(self, message, user_mentions):             #most used command XD
            """
            Usage: 
            {command_prefix}flip[@user] 

            Flip a user cause....why not!		
            """ 
            
            msg = ""
            userc = user_mentions[0]
            print(userc)
            if userc == self.user:
                userc = message.author
                msg = "Nice try. You think this is funny? How about *this* instead:\n\n"
            
            char = "abcdefghijklmnopqrstuvwxyzɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"                       #flipping and unflipping already flipped characters
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎzabcdefghijklmnopqrstuvwxyz"                       #only english letters supported :/
            table = str.maketrans(char, tran)
            name = userc.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.send_message(message.channel, " %s (╯°□°）╯︵  %s" % (msg, name[::-1]))