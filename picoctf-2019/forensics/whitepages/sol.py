import codecs

with open('whitepages.txt', 'r') as file:
	data = file.read()

data = data.replace('\u2003', '0').replace('\x20', '1')

print(codecs.decode('0'+hex(int(data,2))[2:], 'hex'))