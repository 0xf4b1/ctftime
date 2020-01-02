[../](../../)

# Matryoshka

## misc - Points: 157

> Look at this picture. Can you get the flag?
>
> [matryoshka.jpg](matryoshka.jpg)

## Solution

	$ exiftool -b -ThumbnailImage matryoshka.jpg > thumb.jpg
	$ exiftool -b -ThumbnailImage thumb.jpg > thumb2.jpg
	$ exiftool -b -ThumbnailImage thumb2.jpg > thumb3.jpg

flag: `justCTF{d1d_y0u_kn0w_7h47_f1r57_m47ry05hk4_d0ll_w45_m4d3_129_y34r5_4g0}`
