# Unzip Me

## Forensics - Points: 150

> I stole these files off of The20thDucks' computer, but it seems he was smart enough to put a password on them. Can you unzip them for me?
>
> [zip1.zip](zip1.zip)
>
> [zip2.zip](zip2.zip)
>
> [zip3.zip](zip3.zip)
>

Crack passwords with `john`:

	$ zip2john zip1.zip zip2.zip zip3.zip > hashes
	$ john hashes

Passwords are `dictionary`, `rock`, and `dog`.

flag: `nactf{w0w_y0u_unz1pp3d_m3}`