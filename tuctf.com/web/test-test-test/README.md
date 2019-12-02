# Test Test Test

## Web - Points: 500

> There are so many tests going on right now, why don't take a deep breath and list them out before you forget one?
>
> 
>
> chal.tuctf.com:30004
>

Look at the sources and visit `http://chal.tuctf.com:30004/img` and you get a hint for `flag.php`, then request it:

	$ curl http://chal.tuctf.com:30004/flag.php

flag: `TUCTF{d0nt_l34v3_y0ur_d1r3ct0ry_h4n61n6}`