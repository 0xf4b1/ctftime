from PIL import Image

with open('radio_capture.txt', 'r') as file:
	data = file.read().splitlines()


image = Image.new("RGB", (600, 400))
pixels = image.load()

for line in data:
	x, y = line.split(',')
	x = int(x)
	y = int(y)
	pixels[x, y] = (255,255,255)

image.save('image.png')