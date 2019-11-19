from pwn import *
import subprocess

wordlists = ['10-million-password-list-top-1000000.txt', '500-worst-passwords.txt', 'probable-v2-top12000.txt', 'xato-net-10-million-passwords-1000000.txt']

r = remote('ctfchallenges.ritsec.club', 8080)

print r.recvline()
print r.recvline()

text = r.recvline()
print text

while True:

	hash = r.recvline()
	print hash

	with open('hash', 'w') as file:
		file.write(hash)

	cracked = False
	for wordlist in wordlists:
		if wordlist not in text:
			continue

		print 'Using wordlist {}'.format(wordlist)

		result = subprocess.check_output(['john', '--format=NT-opencl' if len(hash) == 32 else '--format=sha512crypt-opencl', '--wordlist={}'.format(wordlist), 'hash'])
		print result
		result = subprocess.check_output(['john', '--format=NT-opencl' if len(hash) == 32 else '--format=sha512crypt-opencl', '--show', 'hash'])
		print result

		if '1 password hash cracked' in result:
			password = result.splitlines()[0][2:]
			print 'PASSWORD: {}'.format(password)
			r.sendline(password)
			print r.recvline()
			cracked = True
			break

	if not cracked:
		print 'FAIL'
		break