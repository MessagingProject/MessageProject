import time
import random

class pigeon:
	global message
	global pigeonart
	def __init__(self,pigeonart,message):
		self.hunger = random.randrange(20,80)
		self.energy = random.randrange(20,80)
		self.message = message
		self.pigeonart = pigeonart

	def eat(self):
		print('Yummy!')
		self.hunger += 30
		if self.hunger > 75:
			print('Your pigeon is full and ready to fly!')
			print(end='')
		else:
			print(end='')

	def rest(self):
		print('Pleased chirp')
		self.energy += 30
		if self.energy > 75:
			print('Your pigeon is fully rested.')
			print(end='')
		else:
			print(end='')

	def newMessage(self):
		self.new_message = self.pigeonart + '\n' + self.message

	def carry(message):
		while mypigeon.hunger < 75 and mypigeon.energy < 75:
			if mypigeon.hunger < 75 and mypigeon.energy < 75:
				print("Your Pigeon is too tired and hungry to deliver your message right now.")
				action = input('Would you like to feed or rest your pigeon? ')
				while action not in ('rest', 'feed'):
					action = input('Please enter rest or feed: ')
				if action in ('feed'):
					mypigeon.eat()
				elif action in ('rest'):
					mypigeon.rest()

			elif mypigeon.hunger < 75:
				print("Your Pigeon is too hungry to deliver your message right now.")
				action = input('Would you like to feed your pigeon? y/n: ')
				while action not in ('y', 'n'):
					action = input('Please enter y or n: ')
				if action in ('y'):
					mypigeon.eat()
				elif action in ('n'):
					print("Ok, but your pigeon can't fly until you feed him.")

			elif mypigeon.energy < 75:
				print("Your Pigeon is too tired to deliver your message right now.")
				action = input('Would you like to rest your pigeon? y/n: ')
				while action not in ('y', 'n'):
					action = input('Please enter y or n: ')
				if action in ('y'):
					mypigeon.rest()
				elif action in ('n'):
					print("Ok, but your pigeon can't fly until you rest him.")

		
		mypigeon.newMessage()
		return mypigeon.new_message



#Morse = Morse()
#Cipher = Cipher()

###############################

print('Welcome to Messenger!')

time.sleep(1)

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
	new_message = Morse.To_Morse(message)

if method == 3:
	new_message = Cipher.Encrypt(message)

#sendToFile(new_message)
print(new_message)