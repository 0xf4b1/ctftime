# Take it to the Cleaners

## Forensics - Points: 100

> Author: Impos73r
>
> Description: People hide things in images all the time! See if you can find what the artist forgot to take out in this one!
>
> [ritsec_logo2.png](ritsec_logo2.png)
>

Running `exiftool` on the image shows that it contains a comment:

	RVZHRlJQe1NCRVJBRlZQRl9TTlZZRl9KQkFHX1VSWUNfTEJIX1VSRVJ9

It is base64 encoded:

	$ echo "RVZHRlJQe1NCRVJBRlZQRl9TTlZZRl9KQkFHX1VSWUNfTEJIX1VSRVJ9" | base64 -d
	EVGFRP{SBERAFVPF_SNVYF_JBAG_URYC_LBH_URER}

After decoding it already looks like the flag format, but it is somehow shifted. Since we know the first characters of the flag format, we can calculate the shift for the first character. It is 13, so maybe ROT13? Yes!

flag: `RITSEC{FORENSICS_FAILS_WONT_HELP_YOU_HERE}`