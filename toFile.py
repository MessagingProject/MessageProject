#toFile
def sendToFile(string):
	file = open("Output.txt")
	file.write(string)
	print(message + ' - written to file')
	
def readFile(lineNumber):
	file = open("Output.txt","r")
	return file.read(lineNumber)
