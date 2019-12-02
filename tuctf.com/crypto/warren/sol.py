from pwn import *
from os import path


r = remote('chal.tuctf.com', 30100)

while True:
	print r.recvuntil('Hey')
	print r.recvline()
	sleep(0.8)

	if path.exists('answer'):
		r.sendline(open('answer', 'r').read())
		while True:
			r.sendline(open('answer', 'r').read())
			print r.recvline()
	else:
		r.sendline('foo')