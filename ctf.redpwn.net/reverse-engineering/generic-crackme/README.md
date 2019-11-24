# Generic Crackme

## Reverse Engineering - Points: 50

> Written by: blevy
>
> 
>
> Note: Enclose the flag with `flag{}`.
>
> [generic_crackme](generic_crackme)
>

Decompile the binary with `Ghidra` and check, how the verification of the input works:

```c
  iVar1 = FUN_00101159((ulong)(uint)(int)*pcParm1);
  if (iVar1 == 0x65) {
    iVar1 = FUN_00101159((ulong)(uint)(int)pcParm1[1]);
    if (iVar1 == 0x70) {
      iVar1 = FUN_00101159((ulong)(uint)(int)pcParm1[2]);
      if (iVar1 == 0x68) {
        iVar1 = FUN_00101159((ulong)(uint)(int)pcParm1[3]);
        if (iVar1 == 0x68) {
          iVar1 = FUN_00101159((ulong)(uint)(int)pcParm1[4]);
          if (iVar1 == 0x7a) {
            uVar2 = 1;
          }
```

`FUN_00101159` simply increments the value by one.

flag: `flag{doggy}`