# HD Pepe

## Stego - Points: 300

> Pepe is alpha tier
>
> 
>
> Author: Degenerat3
>
> ctf_pepe.png
>

`exiftool` shows an image description:

	gh:cyberme69420/hdpepe

When checking out that github repo you can find source code to embed a file into the alpha channel of an image. The file to be embedded is first encoded to `base64` and then `255 - value` is applied for each character. In the repo is also an examiner script that you can easily modify to perform `chr(255 - alpha value)` for at least the first 40 characters and you get the `base64` string `UklUU0VDe00zTTNTX0NBTl9CM19NNExJQ0lPVVN9` and after decoding the flag.

flag: `RITSEC{M3M3S_CAN_B3_M4LICIOUS}`