import toFile

class cipher:
	def __inint__(self, type):
		self.type = type
		self.scrambled = False
	#def scramble:

	#def unscrambled:


message = input("What you want to send: ")
toFile.sendToFile(message)