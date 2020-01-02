[../](../../)

# Santa's crackme

## Reverse Engineering

> I bet you can't crack this!
>
> [main](main)

## Solution

The binary contains a data array whose values need to be `XOR`ed with 3 to get the flag.

```python
data = '5b 00 2e 00 4e 00 42 00 50 00 78 00 36 00 37 00 6d 00 34 00 37 00 5c 00 32 00 36 00 5c 00 61 00 37 00 67 00 5c 00 37 00 34 00 5c 00 6f 00 32 00 60 00 30 00 6d 00 36 00 30 00 5c 00 60 00 6b 00 30 00 60 00 68 00 32 00 6d 00 35 00 7e 00'

flag = ''
for c in data.split(' ')[::2]:
	flag += chr(int(c, 16) ^ 3)

print flag
```

flag: `X-MAS{54n74_15_b4d_47_l1c3n53_ch3ck1n6}`