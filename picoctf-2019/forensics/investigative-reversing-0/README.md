# Investigative Reversing 0

## Forensics - Points: 300

> We have recovered a binary and an image. See what you can make of it. There should be a flag somewhere.
>
> [mystery](mystery)
>
> [mystery.png](mystery.png)

Running `exiftool` on the image reports trailing data after the image data:

    picoCTK�k5zsid6q_57d0d47c}

When opening the binary in `Ghidra` you can find that it shifts the characters of the flag between position 7 and 15 by 5 forwards and appends that data to the image, so moving them backwards gives the flag.

flag: `picoCTF{f0und_1t_57d0d47c}`