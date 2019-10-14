# Programming

## Misc - Points: 489

> <p>A CTF challenge with a touch of competitive programming.</p>
>
> 
>
> <p><i>Note: The flag is split into two parts, you need to find both and concatenate.</i></p>
>
> 
>
> **Author: @miscacc**
>
> [programming.zip](programming.zip)
>

After extracting the ZIP archive, you get a PNG image. Executing `stegoveritas CP.png` finds trailing data after the image data, a ZIP archive, that contains two text files, one of them instructs you to find the longest common subsequence of the two lines in the other file. It turns out that this gives the first part of the flag.

When looking through the different output images, the second part of the flag can be found as part of the image inside the blue color channel.

flag: `rooters{s0m3times_U_h@v3_T0_d1g_deep3R}ctf`