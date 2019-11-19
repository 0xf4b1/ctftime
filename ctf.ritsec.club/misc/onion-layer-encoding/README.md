# Onion Layer Encoding

## Misc - Points: 100

> Encoding is not encryption, but what if I just encode the flag with base16,32,64?
>
> If I encode my precious flag for 150 times, surely no one will be able to decode it, right?
>
> 
>
> Author: choi
>
> onionlayerencoding.txt
>

You have to decode a multiple times encoded string with base16, base32, base64, but don't know the order. My solution simply tries to decode the data in each step with base16 first, in case of an error in the second attempt with base32, and in the last attempt with base64, since you can decode a base16 string also with base64 but not a base64 string with base16, that contains characters out of space and results in an error.

First I tried to decode 150 times, but it turned out, that you have the flag already after 32 iterations.

```python
import base64

with open('onionlayerencoding.txt', 'r') as file:
	data = file.read()

for i in range(32):

	try:
		data = base64.b16decode(data)
		print('base16 @ {}'.format(i))
	except TypeError as err:
		print('base16 failed: ' + str(err))
		try:
			data = base64.b32decode(data)
			print('base32 @ {}'.format(i))
		except TypeError as err:
			print('base32 failed: ' + str(err))
			try:
				data = base64.b64decode(data)
				print('base64 @ {}'.format(i))
			except TypeError as err:
				print('base64 failed: ' + str(err))
				break

print data
```

flag: `RITSEC{0n1On_L4y3R}`