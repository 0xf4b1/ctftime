# 999 Bottles

## PWN - Points: 500

> Well, this is embarassing...
>
> I've accidentally compiled 999 ELF files with my password somewhere along the line, one character at a time.
>
> 
>
> Solve these in order, each accepting one ASCII character.
>
> Keep going...eventually combining these solutions will match the regular expression RITSEC\{.*\}
>
> 
>
> Good luck, and thanks for the help!
>
> 
>
> Author: INGRESSIVE
>
> bottles.zip
>

My solution is a simple script, that brute-forces all printable characters for all the 999 binaries. It took some time to execute but nevertheless revealed the flag.

```python
from pwn import *


text = ''

for i in range(1, 1000):
	found = False
	for c in range(33, 127):
		p = process('{:03d}.c.out'.format(i))
		p.sendlineafter('What is my character?\n', chr(c))
		r = p.recvall()
		if 'Nope!' not in r:
			text += chr(c)
			found = True
			break
	if not found:
		print 'FAIL'
		break

print text
```

flag: `RITSEC{AuT057v}`