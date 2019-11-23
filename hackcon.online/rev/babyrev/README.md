# babyrev

> What comes before main , I wonder .... Note: flag format : flag{XXXXXXX}
>
> [q1](q1)

Debug binary in `gdb` and get the `pass` bytes:

```
0x555555755450 <pass>:		0x26202d27	0x7029153a	0x74701e74	0x7533021e
0x555555755460 <pass+16>:	0x003c383b	0x00000000	0x00000000	0x00000000
```

The bytes are `XOR`ed with `0x41` and contain the flag.

flag: `flag{Th15_15_Cr4zy}`