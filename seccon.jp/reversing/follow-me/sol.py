import json


with open('calc.trace', 'r') as file:
	data = json.loads(file.read())

formula = ""

for x in data:
	if x['event'] == 'branch':
		inst_addr = int(x['inst_addr'], 16)
		result = x['branch_taken']

		if inst_addr == 0x55f6b4d44c4f:
			formula += 'd'

		elif inst_addr == 0x55f6b4d44be9 and not result:
			formula += ','

		elif inst_addr == 0x55f6b4d44c58 and not result:
			formula += '+'

		elif inst_addr == 0x55f6b4d44caf and not result:
			formula += '-'

		elif inst_addr == 0x55f6b4d44d06 and not result:
			formula += '*'

		elif inst_addr == 0x55f6b4d44d5d and not result:
			formula += 'm'

		elif inst_addr == 0x55f6b4d44db4 and not result:
			formula += 'M'

		elif inst_addr == 0x55f6b4d44e08 and not result:
			formula += 'C'

		elif inst_addr == 0x55f6b4d44a1f:
			formula += 'A' if result else 'B'

		elif inst_addr == 0x55f6b4d44a81:
			formula += 'C' if result else 'D'

print formula