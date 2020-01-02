from pwn import *
from PIL import Image


image = Image.new("RGB", (31, 31))
pixels = image.load()

r = remote('challs.xmas.htsp.ro', 13005)

for i in range(960):
	r.recvuntil('f(')
	x = int(r.recvuntil(', ')[:-2])
	y = int(r.recvuntil(')')[:-1])

	r.sendlineafter('=', '0')

	if 'Good!' in r.recvline():
		pixels[x,y] = (255,255,255)
	else:
		pixels[x,y] = (0,0,0)

image.save('image.png')