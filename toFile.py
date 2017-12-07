#toFile
def sendToFile(string):
	file = open("Output.txt")
	file.write(string)
def readFile(lineNumber):
	file = open("Output.txt","r")
	return file.read(lineNumber)
