import time
import random
import sys
import string

pigeonart = """ 
                                                 ,::::.._
                                               ,':::::::::.
                                           _,-'`:::,::(o)::`-,.._
                                        _.', ', `:::::::::;'-..__`.
                                   _.-'' ' ,' ,' ,\:::,'::-`'''
                               _.-'' , ' , ,'  ' ,' `:::/
                         _..-'' , ' , ' ,' , ,' ',' '/::
                 _...:::'`-..'_, ' , ,'  , ' ,'' , ,'::|
              _`.:::::,':::::,'::`-:..'_',_'_,'..-'::,'|
      _..-:::'::,':::::::,':::,':,'::,':::,'::::::,':::;
        `':,'::::::,:,':::::::::::::::::':::,'::_:::,'/
        __..:'::,':::::::--''' `-:,':,':::'::-' ,':::/
   _.::::::,:::.-''-`-`..'_,'. ,',  , ' , ,'  ', `','
 ,;;;;:''''`                 \:. . ,' '  ,',' '_,'
                               ``::._,'_'_,',.-'
                                   \\\\ \\\\
                                    \\\\_\\\\
                                     \\\\`-`.-'_
                                  .`-.\\\\__`. ``
                                     ``-.-._
                                         ` """


def sendToFile(string):
	file = open("Output.txt","w")
	file.write(string + ' - written to file')

	for x in range(12):
		sys.stdout.write("\033[K")
	for x in range(5):
		y = 0
		for y in range (0,6):
			if y == 0:
				b = ''
			else:
				b = '*' * (y-1)
			print(b, end="\r")
			time.sleep(.2)
		sys.stdout.write("\033[K")
	print('Message Sent!')

class pigeon: #pigeon class
	global message
	global pigeonart
	def __init__(self,pigeonart,message): #init variables for later
		self.hunger = random.randrange(20,80) #generates a random value between 20 and 80
		self.energy = random.randrange(20,80) #anything above 75 means the pigeon is full/rested enough to fly
		self.message = message
		self.pigeonart = pigeonart #this and above needed to create the new message 

	def eat(self): #feeding the pigeon enough so he can fly
		print('Yummy!')
		self.hunger += 30 #add 30 to hunger
		if self.hunger > 75: #if greater than 75, pigeon is full
			print('Your pigeon is full and ready to fly!')
			print(end='')
		else: #else nothing, have a pigeon still hungry prompt below
			print(end='')

	def rest(self): #same as above but with rest/sleep instead of flight
		print('Pleased chirp')
		self.energy += 30
		if self.energy > 75:
			print('Your pigeon is fully rested.')
			print(end='')
		else:
			print(end='')

	def newMessage(self): #combines the old message with the pigeon ascii art
		self.new_message = self.pigeonart + '\n' + self.message

	def carry(message): #start of pigeon loop
		while mypigeon.hunger < 75 and mypigeon.energy < 75: #while pigeon is not rested and fed
			if mypigeon.hunger < 75 and mypigeon.energy < 75: #both 
				print("Your Pigeon is too tired and hungry to deliver your message right now.")
				action = input('Would you like to feed or rest your pigeon? ') 
				while action not in ('rest', 'feed'):
					action = input('Please enter rest or feed: ') 
				if action in ('feed'):
					mypigeon.eat()
				elif action in ('rest'):
					mypigeon.rest()

			elif mypigeon.hunger < 75: #just hungry
				print("Your Pigeon is too hungry to deliver your message right now.")
				action = input('Would you like to feed your pigeon? y/n: ')
				while action not in ('y', 'n'):
					action = input('Please enter y or n: ')
				if action in ('y'):
					mypigeon.eat()
				elif action in ('n'):
					print("Ok, but your pigeon can't fly until you feed him.")

			elif mypigeon.energy < 75: #just tired
				print("Your Pigeon is too tired to deliver your message right now.")
				action = input('Would you like to rest your pigeon? y/n: ')
				while action not in ('y', 'n'):
					action = input('Please enter y or n: ')
				if action in ('y'):
					mypigeon.rest()
				elif action in ('n'):
					print("Ok, but your pigeon can't fly until you rest him.")

		
		mypigeon.newMessage() #after the carry function is done, combine the old message with pigeon ascii art
		return mypigeon.new_message # returns the new pigeon message


class Morse:
	def __init__ (self):
		self.morse = [".-","-...","-.-.","-..",".","..-.",
				"--.","....","..",".---","-.-",".-..","--",
				"-.","---",".--.","--.-",".-.","...","-","..-",
				"...-",".--","-..-","-.--","--.."]
		
		self.alph = string.ascii_lowercase

	def To_Morse(self, message):
		space = ' '
		
		message = message.lower()
		
		translated_message = []

		for i in range(0, len(message)):
			character = message[i]

			if character != ' ':
				index = self.alph.find(character)
				new_character = self.morse[index]
			else:
				new_character = '/'

			translated_message.append(new_character)

		message = space.join(translated_message)
		
		return message

	def To_English(self, message):
		no_space = ''

		message = message.split(' ')
		
		translated_message = []

		for i in range(0, len(message)):
			character = message[i]

			if character != '/':
				index = self.morse.index(character)
				new_character = self.alph[index]
			else:
				new_character = ' '

			translated_message.append(new_character)

		self.message = no_space.join(translated_message)
		
		return message

###############################

print('Welcome to Messenger!')

time.sleep(1)

print('	')
message = input('What message do you want to send today? ')
print('	')

method_chosen = False

while method_chosen != True:
	method = input('How do you want your message sent? \n  1: Carrier Pigeon \n  2: Telegraph \n  3: Encryption \n[Please type the number of the method you wish to use] ')

	try:
		method = int(method)

		if 0 < method <= 3:
			method_chosen = True
		else:
			print('	')
			print('Please type a valid number.')
			print('	')

	except ValueError:
		print('	')
		print('Please type a valid number.')
		print('	')
		time.sleep(1)

if method == 1:
	mypigeon = pigeon(pigeonart, message)
	new_message = mypigeon.carry()

if method == 2:
	Morse = Morse()
	new_message = Morse.To_Morse(message)

if method == 3:
	new_message = Cipher.Encrypt(message)

sendToFile(new_message)
#print(new_message)



