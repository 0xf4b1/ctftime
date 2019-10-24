# WhitePages

## Forensics - Points: 250

> I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!
>
> [whitepages.txt](whitepages.txt)

The text contains spaces with byte 0x20, and unicode u2003, that can be interpreted as 0 and 1.

flag: `picoCTF{not_all_spaces_are_created_equal_f71be4d2457dc2d068e8b1e7a51ed39a}`