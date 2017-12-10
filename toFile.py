#toFile
def sendToFile(string):
<<<<<<< HEAD
	file = open("Output.txt","w")
	file.write(string + ' - written to file')
=======
	file = open("Output.txt")
	file.write(string)
	print(message + ' - written to file')
	
>>>>>>> d62c126439f7240b8a56c654bf694e377890177e
def readFile(lineNumber):
	file = open("Output.txt","r")
	return file.read(lineNumber)
