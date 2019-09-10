# Download me ...

## Web - Points: 150

> http://165.22.22.11:25632
>

On the website you can download four files, one of them is a flag.txt. You can download the first three files, but for the flag.txt the token parameter is missing.

The content of the files is some lorem ipsum text, nothing interesting, but the tokens look like MD5 hashsums. Let's check if we can reverse them, for example [here](https://md5.gromweb.com/). The reverse of the hashsums is a number that represents the number of characters in the file.

Okay we can generate the missing token for the flag.txt ourselves but need the length of the file. This can easily be bruteforced. The length of the file is 34 and the missing token is `e369853df766fa44e1ed0ff613f563bd`.

flag: `AFFCTF{Pr3dic71bl3_t0k3n5_4r3_b4d}`