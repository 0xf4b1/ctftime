with open('substitution.csv', 'r') as file:
	data = file.read().splitlines()

dictionary = dict(zip(data[1].split(','), data[0].split(',')))

with open('hwangshandiwork.txt', 'r') as file:
	data = file.read()

flag = ''
for c in data[:-3]:
	flag += dictionary[c]

print flag