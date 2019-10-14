data = "53 4e 4e 55 44 53 52 5a 59 11 53 7e 44 15 59 7e 44 15 59 5c 42 55 47 00"

text = ""
for i in [int(c, 16) for c in data.split(' ')]:
	text += chr(i ^ 0x21)

print(text)