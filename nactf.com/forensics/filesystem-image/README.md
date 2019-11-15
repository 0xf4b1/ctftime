# Filesystem Image

## Forensics - Points: 200

> Put the path to flag.txt together to get the flag! for example, if it was located at `ab/cd/ef/gh/ij/flag.txt`, your flag would be `nactf{abcdefghij}`
>
> [fsimage.iso.gz](fsimage.iso.gz)
>

Mount the image and run inside the root:

	$ find . | grep flag
	./lq/wk/zo/py/hu/flag.txt

flag: `nactf{lqwkzopyhu}`