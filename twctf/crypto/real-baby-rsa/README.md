# real-baby-rsa

## crypto - Points: 40

> [problem.py](problem.py)
>
> [output](output)

Given is a python script, that encrypts a flag with `N` and `e`, and the encrypted `output`. Every character is encrypted separately, so we can create a lookup table by encrypting all possible printable characters with the same parameters and then simply look them up to get the flag.

flag: `TWCTF{padding_is_important}`