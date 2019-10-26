with open('out', 'r') as file:
	data = file.read().splitlines()[1]

key = ''
flag = ''
guess = 'flag{'

for i in range(5):
	key += chr(ord(data[i]) ^ ord(guess[i]))

for k in range(5):
	for i in range(10*k,10*k+5):
		flag += chr(ord(data[i]) ^ ord(key[i%10]))
	flag += '?????'

print flag

guess = '_th3_'

for i in range(35,40):
	key += chr(ord(data[i]) ^ ord(guess[i-35]))

flag = ''
for i in range(49):
	flag += chr(ord(data[i]) ^ ord(key[i%10]))

print flag