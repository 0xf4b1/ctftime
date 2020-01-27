[../](../../)

# ADMIN UI 2

## pwn-re

> That first flag was a dud, but I think using a similar trick to get the full binary file might be needed here. There is a least one password in there somewhere. Maybe reversing this will give you access to the authenticated area, then you can turn up the heat… literally.

We need to find a way to dump the binary for analysis. With the path traversal bug, we can print out the binary by reading the following path:

	../../../proc/self/exe

It will print the binary data in the console, so it works. With the following script, we can save the binary in a file:

```python
from pwn import *


r = remote('mngmnt-iface.ctfcompetition.com', 1337)

r.recvuntil('Quit\n')
r.sendline('2')
r.recvuntil('?\n')
r.sendline('../../../proc/self/exe')
binary = r.recvuntil('Quit\n')

with open('admin-ui', 'wb') as file:
	file.write(binary)
```

Now we can analyze the binary in `Ghidra` and see, how the authentication for the `Service access` option works. First, it expects a password, that is stored in the `flag` we previously read out. Then it expects another password that is generated from data, that are stored in the binary:

	84,93,81,BC,93,B0,A8,98,97,A6,B4,94,B0,A8,B5,83,BD,98,85,A2,B3,B3,A2,B5,98,B3,AF,F3,A9,98,F6,98,AC,F8,BA

For our input, each character is `XOR`ed with 199 and the result is then compared to that data array, so in order to get the password, we just need to `XOR` each byte of the data array with 199 to get the flag.

flag: `CTF{Two_PasSworDz_Better_th4n_1_k?}`