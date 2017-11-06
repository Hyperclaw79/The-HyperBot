import discord
import random

#Not even sure why i wrote this as a separate module XD

async def get_choose(self,message,confy):
       """
       Usage: 
       {command_prefix}choose[Option1?Option2?Option3?.......] 
			 
       Let HyperBot decide for you. ;)		
       """
       args = message.content.strip().replace('%s!choose' % confy,'')
       args = args.split('?')
       print(args)
       res = random.choice(args)
       await self.send_message(message.channel, "**I choose**: `%s`" % res)

