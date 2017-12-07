import sys
import string

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

		for i in range(0, len(self.message)):
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

		for i in range(0, len(self.message)):
			character = message[i]

			if character != '/':
				index = self.morse.index(character)
				new_character = self.alph[index]
			else:
				new_character = ' '

			translated_message.append(new_character)

		self.message = no_space.join(translated_message)
		
		return message
	

Morse = Morse()

morse_message = Morse.To_Morse(message)
real_message = Morse.To_English(morse_message)


# TEST
print(morse_message)
print(real_message)
		
		
