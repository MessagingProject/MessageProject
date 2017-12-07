import time

Pigeon = Carrier_Pigeon()
Morse = Morse()
Cipher = Cipher()

###############################

print('Welcome to Messenger!')

time.sleep(1)

print('	')
message = input('What message do you want to send today? ')
print('	')

method_chosen = False

while method_chosen != True:
	method = input('How do you want your message sent? \n  1: Carrier Pigeon \n  2: Telegraph \n  3: Encryption \n[Please type the number of the method you wish to use] ')

	try:
		method = int(method)

		if 0 < method <= 3:
			method_chosen = True
		else:
			print('	')
			print('Please type a valid number.')
			print('	')

	except ValueError:
		print('	')
		print('Please type a valid number.')
		print('	')
		time.sleep(1)

if method == 1:
	new_message = Pigeon.Carry(message)

if method == 2:
	new_message = Morse.To_Morse(message)

if method == 3:
	new_message = Cipher.Encrypt(message)

sendToFile(new_message)
