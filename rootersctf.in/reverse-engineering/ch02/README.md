# ch02

## Reverse Engineering - Points: 477

> ## **not so good encryption**
>
> 
>
> > my crypto ends at xor (｡•̀ᴗ-)✧
>
> 
>
> 
>
> **Author**
>
> 
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X3eRo0
>
> 
>
> [nsge](nsge)
>

The input is xor'ed with 0x21, then xor'ed with data field in binary and should result zero for equality, so xor'ing this data with 0x21 gives the flag.

flag: `rooters{x0r_e4x_e4x}ctf`