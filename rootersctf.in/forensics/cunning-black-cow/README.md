# Cunning Black Cow

## Forensics - Points: 497

>  _______
>
> < hahahahahahahhah >
>
>  -------
>
>         \   ^__^
>
>          \  (oo)\_______
>
>             (__)\       )\/\
>
>                 ||----w |
>
>                 ||     ||
>
> 
>
> <br/><p>Wrap the flag in rooters{}ctf</p>
>
> **Author**
>
> 
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@miscacc
>
> [cunningblackcow.zip](cunningblackcow.zip)
>

After unpacking in archive, you get two PNG images. Checking both files with `exiftool` shows both images have base64 encoded comments. Additionally one of them has trailer data after the PNG image data. Extracting that data with `binwalk -e CunningBlackCow1.png` gives an encrypted ZIP archive that contains the `flag.txt`.

The first comment is `y0uw@ntk3y?AESe_K@iS3_D3_DuUuU!!`, the second one contains none-printable characters. The first comment hints you that it might be encrypted with AES and both comments have a size of 32 characters. So decrypting the second comment in AES ECB mode with the first comment as key leads to the plaintext `n0ty0ur4l@6OOPS!` with some additional trailing non-printable characters. Using only the printable part as password for the archive lets you extract the `flag.txt`.

flag: `rooters{D7d_U_L3k3_Th4_Ch@l73ng3?}ctf`