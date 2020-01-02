from sys import stdout

ram = bytearray(0x1000) # 0x000 - 0xFFF

A = 0
PC = 0x100

blocked = []

with open('rom', 'rb') as file:
	ram[0x100:0xFFF] = file.read()

while True:

	first = ram[PC]
	second = ram[PC+1]

	address = (first & 0xF) << 8 | second

	PC += 2

	# 2.3.1 Arithmetic

	if first == 0x0:
		# Add XX to A and store the result in A
		A += second
		A &= 0xFF

	elif first == 0x1:
		# Set A = XX
		A = second

	elif first == 0x2:
		# Xor A with XX and store the result in A
		A ^= second

	elif first == 0x3:
		# Or A with XX and store the result in A
		A |= second

	elif first == 0x4:
		# And A with XX and store the result in A
		A &= second

	elif first >> 4 == 0x8:
		# Set A = [XXX]
		A = ram[address]

	elif first >> 4 == 0xD:
		# Xor [XXX] with A and store the result in [XXX]
		if address not in blocked:
			ram[address] ^= A

	elif first >> 4 == 0xF:
		# Set [XXX] = A
		if address not in blocked:
			ram[address] = A

	# 2.3.2 I/O

	elif first == 0x13 and second == 0x37:
		# Send A to Serial Out
		stdout.write(hex(A)[2:].decode('hex'))
		stdout.flush()

	# 2.3.3 Control Flow

	elif first >> 4 == 0x2:
		# Jump to Address XXX
		PC = address

	elif first >> 4 == 0x3:
		# Jump to Address XXX if A = 0
		if A == 0:
			PC = address

	elif first >> 4 == 0x4:
		# Jump to Address XXX if A = 1
		if A == 1:
			PC = address

	elif first >> 4 == 0x5:
		# Jump to Address XXX if A = 255
		if A == 255:
			PC = address

	elif first == 0x60:
		# Compare A to XX and store comparison result in A
		if A == second:
			A = 0
		elif A < second:
			A = 1
		elif A > second:
			A = 255

	elif first >> 4 == 0x7:
		# Compare A to [XXX] and store comparison result in A
		value = ram[address]
		if A == value:
			A = 0
		elif A < value:
			A = 1
		elif A > value:
			A = 255

	elif first == 0xBE and second == 0xEF:
		# Jump to 0x100 and set A = 0x42
		PC = 0x100
		A = 0x42

	elif first >> 4 == 0x9:
		# Block Writes to [XXX]
		blocked.append(address)

	elif first >> 4 == 0xA:
		# Unblock Writes to [XXX]
		blocked.remove(address)

	elif first >> 4 == 0xC:
		# Frobnicate [XXX] and store the result in [XXX]
		if address not in blocked:
			ram[address] ^= 0x42

	elif first == 0xEE and second == 0xEE:
		# No Operation
		pass

	else:
		# Note: A known quirk of this microprocessor is that any undefined instruc-
		# tion has the unique effect of decrementing register A.
		A -= 1
		A &= 0xFF
