# rerere

## reversing - Points: 240

> re rere rerere. Find the magic key, and encapsulate in SECT{...} to get the flag
>
> [chal](chal)

We are given a binary and need to find the correct key, I decompiled it in `Ghidra` and slightly modified and reduced the interesting part to the following code:

```C
void main(void) {
  double data[13] = {-1.61774E-5, -2.438196E-4, 0.001658882, 0.02094839, -0.06191985, -0.62766, 1.013856, 7.805292, -6.77945, -36.45974, 11.32587, 38.7614, 99.0};

  int result;
  double distance;
  char input [88];
  
  gets(input);
  result = 0;
  for (int i = 0; i < 13; i++) {
    distance = 0.00000000;
    for (int j = 0; j < 13; j++) {
      distance = (double)(i - 6) * distance + data[j];
    }
    if (distance <= 0.00000000) {
      distance = distance - 0.50000000;
    }
    else {
      distance = distance + 0.50000000;
    }
    result = result + ((int)input[(long)(int)i] - (int)distance);
    printf("%d, %d, %d\n", (int)distance, (int)input[(long)(int)i], result);
  }
  printf("%d\n", result);
  if (result == 0) {
    puts("Y");
  }
  else {
    puts("N");
  }
  return;
}
```

The binary contains a data array with 13 values and the `for` loops iterate over it and calculate distances with our input, sums them up and checks at the end if there were any differences. With the added `printf` at the end of each iteration it now shows the distance of the entered character and the expected character, so we can now easily infer the correct characters.

flag: `SECT{p0l1y_cr4ck3r}`