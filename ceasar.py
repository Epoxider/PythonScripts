import string

alphabet = list(string.ascii_uppercase)
alphadict = {}
for value, char in enumerate(alphabet):
	alphadict[char] = value

def encryptCeasar(plaintext, key):
	newText = ''
	for c in plaintext:
		if c != ' ':
			newValue = alphadict[c] + key % 25
			newC = list(alphadict.keys())[list(alphadict.values()).index(newValue % 26)]
			newText = newText + newC
	return str(newText)

def decryptCesar(cyphertext):
	newText = ''
	for i in range(0,25):
		for c in cyphertext:
			newValue = alphadict[c] - i % 25
			newC = list(alphadict.keys())[list(alphadict.values()).index(newValue % 26)]
			newText = str(newText) + str(newC)

		print('KEY VALUE: ' + str(i) + ' ' + newText + '\n')
		newText=''

e = 'PRYFFZJGCREEZEXFETFDSRKZEXJGRDSPIVHLZIZEXVDRZCKFSVRLKYVEKZTRKVUKYVGIFSCVDKYVPTCRZDZJKYRKKYVIVJEFNRPFWBEFNZEXNYFKYVJVEUVIIVRCCPZJZKJVVDJFSMZFLJKFDVKYRKKYZJNFEKJKFGJGRDRKRCCJGRDDVIJRIVRCIVRUPSIVRBZEXZEKFTFDGLKVIJREUYZARTBZEXCVXZKZDRKVLJVIJVDRZCJPJKVDJJGRDDVIJRIVRCIVRUPJVEUZEXDRZCFLKFWIREUFDTFLEKIZVJREUJKFCVERTTFLEKJYFNVORTKCPNZCCKYZJDRBVKYZEXJSVKKVI'
decryptCesar(e)

'''if __name__ == "__main__":
	while True:
		val = input("Enter text to encrypt: ")
		if val == 'stop':
			break
		key = input("Enter encryption key: ")
		key = int(key)
		cypher = encrypt(val,key)
		print('Encryption is: ' + encrypt(str(val),key))
		decrypt(cypher)
'''
	