def GetAlphabet():
	File_Alpha = open("_Alphabet.txt", "r")
	Alpha = File_Alpha.read()
	File_Alpha.close()
	return Alpha

def SetAlphabet(Alpha=str()):
	Alpha = Alpha.replace('\n', '')
	File_Alpha = open("_Alphabet.txt", "w")
	File_Alpha.write(Alpha)
	File_Alpha.close()

def RsetAlphadet():
	SetAlphabet('abcdefghijklmnopqrstuvwxyz')

def AddAlphabet(Alpha=str()):
	File_Alpha = open('_Alphabet.txt', "a")
	File_Alpha.write(Alpha)
	File_Alpha.close()

def GenerateVigenereTable(ShowTable):
	Alpha = GetAlphabet()
	File = open("_VigenereTable.txt", "w")
	Alpha = Alpha.replace('\n', '')
	for idx, item in enumerate(Alpha):
		File.write(Alpha+'\n')
		Alpha = Alpha.replace(item, '')
		Alpha += item
		if ShowTable:
			print(Alpha)

	File.close()

def LoadVigenereTable():
	File = open("_VigenereTable.txt", "r")
	VigenereTable = File.readlines()

	for item in VigenereTable:
		VigenereTable[VigenereTable.index(item)] = item.replace('\n', '')

	File.close()
	return VigenereTable
