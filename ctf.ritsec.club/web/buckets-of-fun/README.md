# Buckets of fun

## Web - Points: 100

> http://list-s3.scriptingis.life.ctf.s3-website-us-east-1.amazonaws.com
>
> 
>
> Author: scriptingislife
>

Accessing the following url enumerates the contents of the bucket:

	$ curl http://bucketsoffun-ctf.s3.amazonaws.com/

You will notice besides the `index.html` the `youfoundme-asd897kjm.txt` text file, lets check that out:

	$ curl http://bucketsoffun-ctf.s3.amazonaws.com/youfoundme-asd897kjm.txt

flag: `RITSEC{LIST_HIDDEN_FILES}`