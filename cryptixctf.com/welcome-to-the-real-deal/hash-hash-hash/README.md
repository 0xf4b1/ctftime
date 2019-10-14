# Hash Hash Hash

## Welcome to the real deal - Points: 200

> Recently, n00b learned about **Hashing**.<br>
>
> But, he finds nothing special in it. So he decides to make a Hashing algorithm himself.<br>
>
> Now he is boasting about it. He is so confident that he even provided the algorithm and challenges everyone to crack it.<br>
>
> Put him back onto the ground
>
> [hash.py](hash.py)
>
> [hashed.txt](hashed.txt)
>

Each character was hashed separately with a prime number. Since we know the flag format, we know the first character must be `f`, so we can brute-force all prime numbers till the hash function calculates the same value of the first character in the provided hash. When we have found the used prime number we can generate a lookup table for all printable characters that could be part of the `flag` and calculate their hashed values. Then we can simply lookup the hashed values to get the actual characters.

flag: `flag{Pr1m35_4r3_4W3s0m3}`