# Crack me If You Can

## Misc - Points: 498

> Rev up your GPUs...
>
> 
>
> nc ctfchallenges.ritsec.club 8080
>
> 
>
> Flag format RS{ }
>
> 
>
> Author: Sp1kedshell
>

You have to crack the hashsums with `john` by using the reported wordlists.

I encountered the following wordlists that you can easily get from here: https://github.com/danielmiessler/SecLists

	10-million-password-list-top-1000000.txt, 500-worst-passwords.txt, darkweb2017-top10000.txt, probable-v2-top12000.txt, xato-net-10-million-passwords-1000000.txt

Since I didn't knew how many hashsums need to be cracked, I wrote a script for that. I encountered hashsums of different types, but in the successful run I had only three sha512 hashsums:

```
[+] Opening connection to ctfchallenges.ritsec.club on port 8080: Done
Some moron just breached Meme Corp and decided to dump their passwords...  

In the meantime, prepare your GPUs, and get Ready... Set.... and go CRACK!

However... We have a theory that the passwords might come from darkweb2017-top10000.txt, 500-worst-passwords.txt or xato-net-10-million-passwords-1000000.txt

$6$Y1jSPjRLYsEp.f.M$0fKLx7HKI.87h4fNctH78DLU/asfJBKl0d13jqfw8gFbvEaoYSIgYIX12uJO0i/z9iO.ACsk4ruKGLiPZdc./.

Using wordlist 500-worst-passwords.txt
Device 1@0xf4b1: GeForce GTX 760
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 499 candidates left, minimum 294912 needed for performance.
1g 0:00:00:00 DONE (2019-11-16 04:59) 1.960g/s 978.4p/s 978.4c/s 978.4C/s Dev#1:63°C 123456..albert
Use the "--show" option to display all of the cracked passwords reliably
Session completed
Loaded 1 password hash (sha512crypt-opencl, crypt(3) $6$ [SHA512 OpenCL])
Cost 1 (iteration count) is 5000 for all loaded hashes
trustno1         (?)

Device 1@0xf4b1: GeForce GTX 760
?:trustno1

1 password hash cracked, 0 left

PASSWORD: trustno1
Good job.

$6$fyHZdLjtV9dcNsJa$TMtO1KuBehwfAXBmfYGCiOxWEWHu4/zoo0HJ8Srj2g/o3R.74xIsDIHwTnVpvgFHOKPMJX.OC1ukzx8Fo9x8v.

Using wordlist 500-worst-passwords.txt
Device 1@0xf4b1: GeForce GTX 760
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 499 candidates left, minimum 294912 needed for performance.
0g 0:00:00:00 DONE (2019-11-16 05:00) 0g/s 998.0p/s 998.0c/s 998.0C/s Dev#1:68°C 123456..albert
Session completed
Loaded 1 password hash (sha512crypt-opencl, crypt(3) $6$ [SHA512 OpenCL])
Cost 1 (iteration count) is 5000 for all loaded hashes

Device 1@0xf4b1: GeForce GTX 760
0 password hashes cracked, 1 left

Using wordlist xato-net-10-million-passwords-1000000.txt
Device 1@0xf4b1: GeForce GTX 760
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
1g 0:00:00:21 DONE (2019-11-16 05:01) 0.04587g/s 13528p/s 13528c/s 13528C/s Dev#1:76°C 123456..jeep96
Use the "--show" option to display all of the cracked passwords reliably
Session completed
Loaded 1 password hash (sha512crypt-opencl, crypt(3) $6$ [SHA512 OpenCL])
Cost 1 (iteration count) is 5000 for all loaded hashes
                 (?)

Device 1@0xf4b1: GeForce GTX 760
?:

1 password hash cracked, 0 left

PASSWORD: 
Good job.

$6$NTTKc.uF4PTjXRIW$fYotJewaGcqb6pDZANzlTOj.ebzxkZ1Zc/QpyuhadE2Y0LbVrCN0VMHHTnlIa.o9gI5ByZYk1Ug6FwhJZWrpk0

Using wordlist 500-worst-passwords.txt
Device 1@0xf4b1: GeForce GTX 760
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 499 candidates left, minimum 294912 needed for performance.
0g 0:00:00:00 DONE (2019-11-16 05:01) 0g/s 1134p/s 1134c/s 1134C/s Dev#1:74°C 123456..albert
Session completed
Loaded 1 password hash (sha512crypt-opencl, crypt(3) $6$ [SHA512 OpenCL])
Cost 1 (iteration count) is 5000 for all loaded hashes

Device 1@0xf4b1: GeForce GTX 760
0 password hashes cracked, 1 left

Using wordlist xato-net-10-million-passwords-1000000.txt
Device 1@0xf4b1: GeForce GTX 760
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
1g 0:00:00:22 DONE (2019-11-16 05:02) 0.04474g/s 13195p/s 13195c/s 13195C/s Dev#1:76°C 123456..jeep96
Use the "--show" option to display all of the cracked passwords reliably
Session completed
Loaded 1 password hash (sha512crypt-opencl, crypt(3) $6$ [SHA512 OpenCL])
Cost 1 (iteration count) is 5000 for all loaded hashes
                 (?)

Device 1@0xf4b1: GeForce GTX 760
?:

1 password hash cracked, 0 left

PASSWORD: 
Good job.

NICE JOB.  FLAG:RS{H@$HM31FY0UCAN}
```

The script:

```python
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
```

flag: `RS{H@$HM31FY0UCAN}`