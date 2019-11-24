# Super Hash

## Cryptography - Points: 50

> Written by: NotDeGhost
>
> 
>
> Does hashing something multiple times make it more secure? I sure hope so. I've hashed my secret ten times with md5! Hopefully this makes up for the fact that my secret is *really* short. Wrap the secret in `flag{}`.
>
> 
>
> Note: Follow the format of the provided hash exactly
>
> 
>
> Hash: `CD04302CBBD2E0EB259F53FAC7C57EE2`
>

Brute-force all printable characters, hash them 10 times and compare with the target hash.

```python
import hashlib
import string

target = 0xCD04302CBBD2E0EB259F53FAC7C57EE2

for c in string.printable:
	m = hashlib.md5(c).hexdigest().upper()
	for i in range(9):
		m = hashlib.md5(m).hexdigest().upper()

	if int(m, 16) == target:
		print c
		break
```

flag: `flag{^}`