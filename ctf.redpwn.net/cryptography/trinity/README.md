# Trinity

## Cryptography - Points: 77

> Written by: blevy
>
> 
>
> redpwn claims to have invented an unbreakable "trinity encoding."
>
> Security by obscurity!
>
> 
>
> ```
>
> 1202010210201201021011200200021121112010202012010210102012102021000200121200210002021210112111200121200002111200121102000021211120010200212001020020102000212
>
> ```
>
> 
>
> NB: This challenge does not use the flag{...} format. The flag is only lowercase letters.
>
> 
>
> Hint: The encoding is so simple, even your grandma knows about it!
>

Interpret the three numbers as morse code with the following mapping:

	'0': '.', '1': '-', '2': ' '

The resulting morse code:

	- . .-. -. .- .-. -.-- .. ... -- --- .-. . .- .-. -.-. .- -. . -... ..- - .. -... . - -.-- --- ..- - .... --- ..- --. .... - --- ..-. .. - ..-. .. .-. ... - 

Decode it with some online decoder gives the flag.

flag: `flag{TERNARYISMOREARCANEBUTIBETYOUTHOUGHTOFITFIRST}`