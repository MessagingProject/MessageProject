import toFile
import random
class cipher:
	def __inint__(self, type, message):
		self.message = message.lower()
		self.type = "cesear"
		self.scrambled = False
		self.alphabet = string.ascii_lowercase
		self.shift = []

	def scramble(self, type):
		space = " "
		finalMessage = []
		if type == "cesear":
			for j in range(0, len(self.message)):
				character = message[j]
				if character != space:
					finder = self.alphabet.find(character)
					newCharacter = (finder+3)
				else:
					newCharacter = space
				finalMessage.append(newCharacter)
				self.message = finalMessage

		if type == "alpharando":
			for j in range(0, len(self.message)):
				character = message[j]
				if character != space:
					finder = self.alphabet.find(character)
					shift.append(random.randint(0,25))
					newIndex = finder + shift[j]
					if newIndex > 25:
						newIndex = newIndex - 26
					newCharacter = self.alphabet.find(newIndex)

					'''first letter of message, find in alphabet
					generate random number, save it to shift
					wrapping: if index + shift is greater than 26, subtract 26
					find character at index (index of original letter plus shift)
					put character  in message

					determine index of character in messsage
					find number at that index in shift list
					find index of character in alphabet
					find character in alphabet at index (index of character minus shift)
					put character in message
					'''
				else:
					newCharacter = space
				finalMessage.append(newCharacter)

				nospace = ""
				self.message = nospace.join(finalMessage)
	def unscramble(self, type):
		space = " "
		finalMessage = []
		if type == "cesear":
			for j in range(0, len(self.message)):
				character = message[j]
				if character != space:
					finder = self.alphabet.find(character)
					newCharacter = (finder-3)
				else:
					newCharacter = space
				finalMessage.append(newCharacter)
				self.message = finalMessage

		if type == "alpharando":
			for j in range(0, len(self.message)):
				character = message[j]
				if character != space:
					finder = self.alphabet.find(character)
					newCharacter = alphabet[finder-shift[j]]

				else:
					newCharacter = space
				finalMessage.append(newCharacter)

				nospace = ""
				self.message = nospace.join(finalMessage)
type = input("What type of scramble do you want(cesear or alpharando)?")
if type != "cesear" or "alpharando":
	type = "cesear"

message = input("message: ")
cipher = cipher(type, message)
cipher.scramble(type)
