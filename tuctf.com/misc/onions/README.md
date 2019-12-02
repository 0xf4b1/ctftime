# Onions

## Misc - Points: 498

> Ogres are like files -- they have layers!
>
> [shrek.jpg](shrek.jpg)
>

Successively extract data from the files you get:

	$ binwalk -e shrek.jpg
	$ tar -xzvf flag.tar.gz
	$ cpio -idmv < flag.cpio
	$ unlzma flag.lzma
	$ ar x flag
	$ binwalk -e flag1.txt // tar -xf did not worked
	$ xz -d 0.xz

flag: `TUCTF{F1L3S4R3L1K30N10NSTH3YH4V3L4Y3RS}`