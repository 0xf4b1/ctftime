# GOT Milk?

## pwn - Points: 50

> GlobalOffsetTable milk? 
>
> `nc pwn.chal.csaw.io 1004`
>
> [gotmilk](gotmilk)
>
> [libmylib.so](libmylib.so)
>

Exploit the format string to modify the address of the `lose` function in the `GOT` and let it point to the `win` function.

flag: `flag{y0u_g00000t_mi1k_4_M3!?}`