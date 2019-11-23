from PIL import Image

with open('response.txt', 'r') as file:
	data = file.read().splitlines()[1:-1]


image = Image.new("RGB", (200, 200))
pixels = image.load()

for y in range(200):
	for x in range(200):
		pixels[x,y] = (255,255,255) if data[y][x] == 'B' else (0,0,0)

image.save('image.png')