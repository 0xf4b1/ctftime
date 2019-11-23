with open('flagmain.txt', 'r') as file:
	chunks = file.readline().split(' ')

res = ''
for chunk in chunks:
	res += chr(int(chunk, 2))

print(res)