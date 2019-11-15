# Callsite

## rev - Points: 100

> Call me maybe? `nc rev.chal.csaw.io 1001`
>
> [callsite](callsite)
>

The binary expects two arguments, the first is an address and the second one a key. If you open the binary in `gdb` you see that it directly jumps to the address you specify. Okay we need to find an interesting address were we have to jump to.

Open the binary in `Ghidra`, find the string `flag.txt` and check where it is used. There is an unused function at `0x400ca0`, it has one parameter that is probably the key you provide via second argument and it is compared against a string. You can skip the check and directly jump behind it to address `0x400cbb`, so the key does not matter.

	./callsite 400cbb 123

flag: `flag{you_got_the_call_site}`