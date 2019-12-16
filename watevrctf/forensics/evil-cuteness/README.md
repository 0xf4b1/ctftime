[../](../../)

# Evil Cuteness

## forensics - Points: 23

> Omg, look at that cute kitty! It's so cute I can't take my eyes off it! Wait, where did my flag go?
>
> [kitty.jpg](kitty.jpg)

## Solution

	$ binwalk -e kitty.jpg
	$ cat _kitty.jpg.extracted/abc

flag: `watevr{7h475_4c7u4lly_r34lly_cu73_7h0u6h}`