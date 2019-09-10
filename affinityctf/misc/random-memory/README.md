# Random Memory

## Misc - Points: 300

> nc 165.22.22.11 5566
>

When connecting it says that a system is booted with a given timestamp and because of a required memory check, random values are pushed to 31137 memory cells. Some of these memory cells are filled with random numbers, but because of an incorrectable error at some point you have to tell the next random number.

So this challenge is about random number generation, basic random number generators use the current system time as seed for the generation. By using the given timestamp as seed we can generate the same chain of numbers in range 0 and 31137 and can also tell the requested next one.

It's important to note that random from python2 and python3 generate different numbers for the same seed and python3 needs to be used here.

flag: `AFFCTF{d0n7_l0s3_y0ur_m3m0ry}`