import discord
import asyncio
import random
	  
async def get_minesweeper(self, message):
#ToDO: replace thumbs up emojis with proximity numbers.
   emoji_dict = {1 : ':one:', 2 : ':two:', 3 : ':three:', 4 : ':four:', 5 : ':five:', 6 : ':six:', 7 : ':seven:', 8 : ':eight:', 9 : ':nine:'}
   sendstr = ':one: :two: :three:\n:four: :five: :six:\n:seven: :eight: :nine:'
   sent = await self.send_message(message.channel, sendstr)
   bomb = str(random.choice(list(emoji_dict.keys())))
   count = 0
   while True:
      ex = await self.wait_for_message(channel = message.channel, author = message.author)
      try:
        if int(ex.content)<=9:
            if ex.content == bomb and count<9:
              sendstr = sendstr.replace(emoji_dict[int(ex.content)], ':bomb:')
              await self.edit_message(sent, new_content = sendstr)  
              await self.send_message(message.channel, '\n%s,Better luck next time! Your score is: %s' % (message.author.mention,count))
              break
            elif ex.content == bomb and count>=9:
              sendstr = sendstr.replace(emoji_dict[int(ex.content)], ':trophy:')
              await self.edit_message(sent, new_content = sendstr)  
              await self.send_message(message.channel, '\nCongratulations %s you won it!' % message.author.mention)			
            else:
              sendstr = sendstr.replace(emoji_dict[int(ex.content)], ':thumbsup::skin-tone-1:')
              await self.edit_message(sent, new_content = sendstr)
            count += 1
            await self.delete_message(ex)			
      except:
        continue 		