#toFile
def sendToFile(string):

	file = open("Output.txt","w")
	file.write(string + ' - written to file')
def readFile(lineNumber):
	file = open("Output.txt","r")
	return file.read(lineNumber)
