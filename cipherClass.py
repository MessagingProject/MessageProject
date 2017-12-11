
import random
import string
#toFile
def sendToFile(string):
	file = open("Output.txt","w")
	file.write(string + ' - written to file')
def readFile(lineNumber):
	file = open("Output.txt","r")
	return file.read(lineNumber)

class cipher:
	def __init__(self, type, message):
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
					finder = (self.alphabet.find(character))
					newCharacter = (finder)
				else:
					newCharacter = space
				finalMessage.append(newCharacter)
				nospace = ""
				self.message = str(nospace.join(finalMessage))
				return self.message
				'''this is a classic cesear cipher
				takes the message and shifts each character by three letters to the right
				'''
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
				self.message = str(nospace.join(finalMessage))
				return self.message
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
				return self.message

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
				return self.message
##Main Code
typ = input("What type of encryption do you want(cesear or alpharando)? ")
if typ != "cesear" or "alpharando":
	typ = "cesear"

message = input("message: ")
theCipher = cipher(typ, message)
sendToFile(theCipher.scramble(typ))
#sendToFile(theCipher.unscramble(type))
