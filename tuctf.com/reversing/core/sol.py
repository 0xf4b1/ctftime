string = 'UTBUGzb1s2^etlq>^O2w2s^i25se^1g^x1t|'

flag = ''
for c in string:
	flag += chr(ord(c) ^ 1)

print flag