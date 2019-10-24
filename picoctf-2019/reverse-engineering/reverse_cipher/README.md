# reverse_cipher

## Reverse Engineering - Points: 300

> We have recovered a binary and a text file. Can you reverse the flag.
>
> [rev](rev)
>
> [rev_this](rev_this)

The binary shifted the characters between 8 and 23 either 5 forwards if it is an even character or 2 backwards if it is an odd character. Since there are only odd characters in the rev string, there are always two possibilities, after the first characters you quickly observe the pattern always alternating both possibilities.

    picoCTF{w1{1wq83k055j5f}
		 1) r,v,rl3.f+00e0a
		 2) y3}3ys:5m277l7h

flag: `picoCTF{r3v3rs35f207e7a}`