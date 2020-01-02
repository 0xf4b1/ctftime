[../](../../)

# FUNction Plotter

## Misc

> One of Santa's elves found this weird service on the internet. He doesn't like maths, so he asked you to check if there's anything hidden behind it.
>
> nc challs.xmas.htsp.ro 13005

## Solution

When connecting to the service, you are asked to guess 961 function values. Because of the challenge name and since 31 is the square root of 961, we probably have to draw to an 31x31 image.

So lets interpret the function arguments as x and y coordinates and we have to guess the color value. When trying a bit around what values to guess it turns out that you are often right when choosing 0 or 1, so its probably black and white image. The following script always chooses 0 and when it was incorrect it was 1 and draws 0 with white color and 1 with black color on an image.

```python
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
```

The image contains a QR code, that can be read out with the following command and gives the flag.

	$ zbarimg image.png

flag: `X-MAS{Th@t's_4_w31rD_fUnCt10n!!!_8082838205}`