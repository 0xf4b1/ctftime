[../](../../)

# Dinary

## Misc - Points: 15

> My kipod is gone :(
>
> dinary.png
>

## Solution

Interpret the black and white color pixels as zeros and ones and convert the binary string to byte string. There is readable text right at the beginning with the flag.

```python
from PIL import Image


im = Image.open('dinary.png')

pixels = list(im.getdata())

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

with open('data', 'wb') as file:
	data = ''
	for pixel in pixels:
		if pixel == (0,0,0):
			data += '0'
		else:
			data += '1'
		if len(data) == 8:
			file.write(bitstring_to_bytes(data))
			data = ''

```

flag: `KAF{wh3r3_1s_my_k1p0d?}`