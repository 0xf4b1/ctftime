# Small icon much wow

> One of my friends like to hide data in images.
>
> Help me to find out the secret in image.
>
> [stego.jpg](stego.jpg)

Analyse metadata of image with `exiftool` and extract the thumbnail image with:

	$ exiftool -b -ThumbnailImage stego.jpg > image.jpg

It contains a QR code, the decoded content is the flag.

	$ zbarimg thumbnail.jpg

flag: `d4rk{flAg_h1dd3n_1n_th3_thumbnail}c0de`