# Weird machine

## Still Manageable - Points: 150

> Recently, H4c3R1337 came across a weird machine, which keeps spitting 0 or 1. He wrote down the complete sequence in a file<br>
>
> 
>
> He decided to find out what it means, but could barely manage to recover an incomplete python script from the machine.<br>
>
> Help him to find out 
>
> [encrypt.py](encrypt.py)
>
> [seq.txt](seq.txt)
>

The data was encrypted via XOR with a random generated string as key, while the seed was a random int in range(1,10000), so we need to brute-force all possible seeds and apply XOR on the encrypted data and the generated strings till we get an output that starts with `flag`.

flag: `flag{R4nd0m_s33d_s4v3d_y0u}`