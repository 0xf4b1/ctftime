# Generic Crackme Redux

## Reverse Engineering - Points: 50

> Written by: blevy
>
> 
>
> Note: Enclose the flag with `flag{}`.
>
> [generic_crackme_redux](generic_crackme_redux)
>

Decompile the binary with `Ghidra` and check, how the verification of the input works:

```c
ulong FUN_00101169(int iParm1)
{
  return (ulong)(iParm1 * 10 & 0xffffff00U | (uint)(iParm1 * 10 == 0xac292));
}
```

The input number multiplied by 10 must equal `0xac292`.

flag: `flag{70517}`