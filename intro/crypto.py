def vigenere(key, ciphertext):
	message_code = ""
	for i,c in enumerate(ciphertext) :
		d = key[ i % len(key) ]
		d = ord(d) - 65
		message_code += chr((ord(c)-65+d)%26+65)
	return message_code

def vernam(key, msg):
	return hex(bin(int(key,16)) % bin(int(msg,16)))
	


print(vigenere("google", "himezyzipk"))
# print(vernam("0x6B9D","0x9AC3"))