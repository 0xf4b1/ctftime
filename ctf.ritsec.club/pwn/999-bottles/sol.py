from pwn import *


text = ''

for i in range(1, 1000):
	found = False
	for c in range(33, 127):
		p = process('{:03d}.c.out'.format(i))
		p.sendlineafter('What is my character?\n', chr(c))
		r = p.recvall()
		if 'Nope!' not in r:
			text += chr(c)
			found = True
			break
	if not found:
		print 'FAIL'
		break

print text