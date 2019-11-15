# beleaf

## rev - Points: 50

> tree sounds are best listened to by https://binary.ninja/demo or ghidra
>
> [beleaf](beleaf)
>

When opening the binary in `Ghidra` you will find two data fields.

The first array has the following characters at the specified index position:

```
0: w
1: f
2: {
3: _
4: n
5: y
6: }
8: b
9: l
a: r
11: a
12: e
13: i
15: o
16: t
27: g
2e: u
```

The second array is a sequence of indexes to the first array:

    1 9 11 27 2 0 12 3 8 12 9 12 11 1 3 13 4 3 5 15 2E A 3 A 12 3 1 2E 16 2E A 12 6

Replacing the indexes with the corresponding characters gives the flag.

flag: `flag{we_beleaf_in_your_re_future}`