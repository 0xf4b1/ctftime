import base64

with open('onionlayerencoding.txt', 'r') as file:
	data = file.read()

for i in range(32):

	try:
		data = base64.b16decode(data)
		print('base16 @ {}'.format(i))
	except TypeError as err:
		print('base16 failed: ' + str(err))
		try:
			data = base64.b32decode(data)
			print('base32 @ {}'.format(i))
		except TypeError as err:
			print('base32 failed: ' + str(err))
			try:
				data = base64.b64decode(data)
				print('base64 @ {}'.format(i))
			except TypeError as err:
				print('base64 failed: ' + str(err))
				break

print data