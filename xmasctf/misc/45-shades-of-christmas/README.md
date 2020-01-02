[../](../../)

# 45 Shades of Christmas

## Misc

> I wish I could get the last 5 shades this year...
>
> [grey.bmp](grey.bmp)

## Solution

Open the image with `stegsolve`, then goto `Analyze->Data Extract` and select all 8 bits of one of the RGB color channels (all color channels contain the same data). You can see that the data contains only printable characters and looks like `base64` encoded. Extracting the data by row results in garbage after decoding, but when you extract the data by column you get some readable text and the flag at the end.

flag: `X-MAS{Gl43d3ligJul0gG0dtNyt4r}`