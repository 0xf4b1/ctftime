[../](../../)

# Corey's core dump 1 (baby)

## RE - Points: 36

> I've seen this challenge maybe too many times...
>
> 
>
> ...but let's do this one more time
>
> 
>
> This is a 2-part challenge. Should be an easy warmup, find the first password!
>
> 
>
> Author: theKidOfArcrania
>
> [core](core)
>

## Solution

	$ strings core | grep -i utc

flag: `utc{im_a_passw0rd}`