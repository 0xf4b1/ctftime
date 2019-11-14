# mycat

## misc

> My cat is planing something, find the hidden msg
>
> [mycat](mycat)

The given file is a PDF document. `binwalk` reveals additional embedded data, another PDF file that contains an image of a cat. It contains hidden text with black font color on black background, `CTRL+A` (select all) in your PDF viewer should already reveal it, alternatively `pdf2txt` prints it out.

flag: `SECT{3mb3dd3d_f1l3s_c0uld_b3_tr1cky}`