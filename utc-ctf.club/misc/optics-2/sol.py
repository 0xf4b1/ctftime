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