import discord
import random

from random import choice
from discord import utils
from discord.utils import find

#ToDO: Change it into message.author <interacts with> user and random.choice over gifs like Miki and Kawaibot.

async def get_punch(self, message, user_mentions):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot punch someone. :P		
    """ 
    await self.send_message(message.channel, "HyperBot punches the shit outta %s " % user_mentions[0].mention)
	  
   
async def get_kick(self, message, user_mentions):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot kick someone. :P		
    """ 
    await self.send_message(message.channel, "HyperBot karate kicks %s to submission." % user_mentions[0].mention)
	  
   
async def get_pat(self, message, user_mentions):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot pat someone. :P		
    """ 
    await self.send_message(message.channel, "HyperBot gives %s an endearing pat." % user_mentions[0].mention)

   
async def get_hug(self, message, user_mentions):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot hug someone. :P		
    """ 
    await self.send_message(message.channel, "HyperBot warmly hugs %s" % user_mentions[0].mention)

   
async def get_kiss(self, message, user_mentions):
    """
    Usage: 
    {command_prefix}punch[@user] 
			 
    Make HyperBot kiss someone. :P		
    """ 
    await self.send_message(message.channel, "HyperBot passionately kisses %s and blushes" % user_mentions[0].mention)	  
	
	
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