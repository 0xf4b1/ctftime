[../](../../)

# ezip (baby)

## Misc - Points: 31

> Crack the password protected zip for me
>
> 
>
> By: knapstack
>
> [flag.zip](flag.zip)
>
> [cat.png](cat.png)
>

## Solution

The image contains the password for the ZIP file as comment:

	$ exiftool cat.png
	Comment : e4syp4ssf0rz1p

Then unzip the flag from the ZIP archive.

flag: `utc{ex1f_ru135_4ll_7h3_w4y}`