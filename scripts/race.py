import discord
import random
import asyncio

#ToDo List: 1) Custom Horses emojis. 2) Betting System 3) Cash Prize for the first winner which will be equal to 0.1 * amount generated by total placed bets.

async def play_race(self, message, user_mentions):
   """
   Usage:
        {command_prefix}race[@user1,@user2,@user3,......]
   A race minigame betweens users.
   """
   racebase ='🏁---------------|-----------|---------------🏇' #a base everyone starts with, now with hurdles
   winningpos = 1 #counter to maintain who finished at what position
   racer = {}
   tempy = {}
   rm = {}
   msgc = ""
   for user in user_mentions: 
      racer[str(user)] = {'position' : len(racebase), 'place' : 0, 'scenario' : racebase, 'modifier' : 0} # template of every user in the dict, position holds len(racebase), endofline, place is the finishing pos, obvio at 0, race holds the racebase for each person, modifier is used if the user has custom horses.
      #msgc = msgc +  racer[str(user)]['scenario'] + ": " + str(user.display_name) + "\n"
      try:
         with open('bot_files/horses.json', 'r+') as f: #this to load and check for horses
            tempy = json.load(f)
         if tempy[(user.id)]['Horse'] == "Normal": #ToDo change "Normal" and "Premium" to custom horse emojis
            racer[str(user)]['modifier'] = 2
         elif tempy[(user.id)]['Horse'] == "Premium":
            racer[str(user)]['modifier'] = 5
         else:
            racer[str(user)]['modifier'] = 0
         print(racer[str(user)]['modifier'])
      except:
         racer[str(user)]['modifier'] = 0
          #await self.send_message(message.channel,(racer[str(user)]['scenario'],user.display_name)		  
   print(msgc)
   #msgc = await self.send_message(message.channel,msgc)
   while True: # infinite loop
      counter = 1 # this works in the way that, if everyone has finished, multiple of all counter will not give you 0, because 0 * anything is 0, so if everyone finished at a position it will never be 0
          #await asyncio.sleep(1)		  
      for user in user_mentions: # self explanatory
         counter = counter * racer[str(user)]['place']
      if counter == 0: # checks if theres anyone whos still racing
         pass
      else: # if not, lets break we're done
         break
      for user in user_mentions: 
         if racer[str(user)]['place'] == 0: # if you havent won, lets see how many steps you're going to take
            ran = random.randint(3,9) + racer[str(user)]['modifier'] # random steps between 1 to 7
            if racer[str(user)]['position'] - ran <= 0: # ok if this is going in the negative, change it to 0, negative will fuck code up
               racer[str(user)]['position'] = 0 
            else: # if not, change position to new position with x steps moved forward , as we're going right to left its minus and not adding
               racer[str(user)]['position'] = racer[str(user)]['position'] - ran
            if racer[str(user)]['scenario'][racer[str(user)]['position']] == '|':
               #obstacle = '|'
               racer[str(user)]['modifier'] =  - 1
               racer[str(user)]['position'] += 1
            #else:
                   #obstacle = '-'				
            racer[str(user)]['scenario'] = racer[str(user)]['scenario'].replace('🏇','-') # theres only one horse in the entire string, change it to - cause swapping - and the horse is tough
            racer[str(user)]['scenario'] = self.value_editor(racer[str(user)]['scenario'], index =racer[str(user)]['position'], modify_to = '🏇') # use the custom function, new index was made using ran, use that index, replace it with a horse
            #rm[user] = racer[str(user)]['scenario'] + ": " + str(user.display_name) + "\n"
            #msg = ''.join(rm[user])
            
            if racer[str(user)]['position'] == 0: # if you've won
               racer[str(user)]['place'] = winningpos # your dict gets a value other than 0
               winningpos += 1 # add 1 to winningpos everytime someone wins
            if racer[str(user)]['place'] == 1: #:first_place: :second_place: :third_place: #cases to replace winners with trophies #ToDo use different trophy emojis, probably custom
               racer[str(user)]['scenario'] = self.value_editor(racer[str(user)]['scenario'], index =racer[str(user)]['position'], modify_to = ':first_place:')
            if racer[str(user)]['place'] == 2: #:first_place: :second_place: :third_place:
               racer[str(user)]['scenario'] = self.value_editor(racer[str(user)]['scenario'], index =racer[str(user)]['position'], modify_to = ':second_place:')
            if racer[str(user)]['place'] == 3: #:first_place: :second_place: :third_place:
               racer[str(user)]['scenario'] = self.value_editor(racer[str(user)]['scenario'], index =racer[str(user)]['position'], modify_to = ':third_place:')
            #await self.edit_message(msgc,msg)
			#await self.edit_message(msgc,"%s %s" % (racer[str(user)]['scenario'],user.display_name))
      announcement = "" #This will become the announcement message.
      for user in user_mentions: 
         announcement += racer[str(user)]['scenario'] +' ' + user.name + '\n' # add to that empty string, racebase for the user, a space, their name and linebreak
      await asyncio.sleep(1) #sleep 2 sec, cause bombarding with messages is lame. And thanks to fkin rate limit.
      try:
         await self.edit_message(rx, announcement) # if the message exists , edit it #not really sure why it will exist in the first place if we are using rx as a local variable. ?-?
      except: # if it doesnt, send a message, save it in rx
         rx = await self.send_message(message.channel, announcement) #tbh, not even sure why we have to save this.
   winners = {} # This will become the winner position log
   for user in user_mentions: 
      winners[racer[str(user)]['place']] = user #save users, by position place holds position
   winstr = '%s finished 1st :first_place:\n%s finished 2nd :second_place:\n%s finished 3rd :third_place:' % (winners[1].name,winners[2].name,winners[3].name) # add trophies for 3
   for x in range(4, len(winners)+1): #values between 4th and last, add to string as %sth +1 cause index starts from 0.
      winstr +='\n%s finished %sth' % (winners[x].display_name, x) #changed to display_name to accomodate nicknames.
   await self.send_message(message.channel, winstr) # send winstr