# Stringy

## Binary / Reversing - Points: 100

> Take it as a gift :)<br><br> Author: z0m31en7
>
> [stringy](stringy)
>

The binary contains base64 encoded strings:

	$ strings stringy
	[...]
	c2VjYXJtH
	eXtsMDBrH
	X2E3X3RoH
	M19zdHIxH
	bmc1ISF9H
	[...]

Put them together and get the flag.

	$ echo "c2VjYXJteXtsMDBrX2E3X3RoM19zdHIxbmc1ISF9" | base64 -d

flag: `secarmy{l00k_a7_th3_str1ng5!!}`