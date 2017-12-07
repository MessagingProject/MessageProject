import sys
import string

class Morse:
	def __init__ (self, message):
		self.message = message.lower()

		self.morse = [".-","-...","-.-.","-..",".","..-.",
				"--.","....","..",".---","-.-",".-..","--",
				"-.","---",".--.","--.-",".-.","...","-","..-",
				"...-",".--","-..-","-.--","--.."]
		
		self.alph = string.ascii_lowercase

	def To_Morse(self):
		space = ' '

		translated_message = []

		for i in range(0, len(self.message)):
			character = message[i]

			if character != ' ':
				index = self.alph.find(character)
				new_character = self.morse[index]
			else:
				new_character = '/'

			translated_message.append(new_character)

		self.message = space.join(translated_message)

	def To_English(self):
		space = ' '

		translated_message = []

		for i in range(0, len(self.message)):
			character = message[i]

			if character != '/':
				index = self.morse.find(character)
					new_character = self.alph[index]
			else:
				new_character = ' '

			translated_message.append(new_character)

		self.message = space.join(translated_message)
