[../](../../)

# Fortnite

## crypto

> Jeez, these damn security researchers never publish key material when they find it...
>
> Since OTP is perfect, I guess there is no way to get the key... Maybe still give it a try.
>
> Flag format is flag{key}.
>
> [fortnite.txt](fortnite.txt)

## Solution

XOR the unencrypted bytes and the encrypted bytes to reveal the used key. Since the key is shorter than the message and is reused in a cyclic way, the key is only the part till it repeats.

flag: `flag{kjwkdnwl}`