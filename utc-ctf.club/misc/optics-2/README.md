[../](../../)

# Optics 2

## Misc - Points: 186

> You seem to be professional in Forensics & Optics. Now, the things will get tedious. Let's see what you got.
>
> 
>
> By: knapstack
>
> [challenge_2.zip](challenge_2.zip)
>

## Solution

After unpacking the ZIP archive, you get a lot of images that look like snippets of a QR code. The following script reassembles the QR code image:

```python
import os
from PIL import Image

new_im = Image.new('RGB', (21*55, 21*55))

i = 0

for y in range(21):
	for x in range(21):
		image = Image.open('chall_{}.png'.format(i))
		new_im.paste(image, (x*55,y*55))
		i += 1

new_im.save('qr.png')
```

Then decode the QR code:

	$ zbarimg qr.png

flag: `utc{merge_and_merge_until_you_decode_it}`