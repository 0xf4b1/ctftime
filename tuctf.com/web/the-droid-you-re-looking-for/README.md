# The Droid You're Looking For

## Web - Points: 498

> Sometimes you need a little Star Wars in your life to come across the flag.
>
> 
>
> chal.tuctf.com:30003
>

Check `robots.txt` and do the following:

	$ curl http://chal.tuctf.com:30003/robots.txt -H 'User-Agent: googlebot'
	$ curl http://chal.tuctf.com:30003/googleagentflagfoundhere.html

flag: `TUCTF{463nt_6006l3_r3p0rt1n6_4_r0b0t}`