data = 'n9ain9ain9ai_n9aik9l'

text = ''
for c in data:
	code = ord(c)
	if code < ord('a') or code > ord('z'):
		# no lowercase character
		if code < ord('0') or code > ord('9'):
			# no digits
			pass
		else:
			# digits
			code -= 5
	else:
		# lowercase character
		code += 2

	text += chr(code)

print text