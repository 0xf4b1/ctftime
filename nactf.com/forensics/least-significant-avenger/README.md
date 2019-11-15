# Least Significant Avenger

## Forensics - Points: 50

> I hate to say it but I think that Hawkeye is probably the Least Significant avenger. Can you find the flag hidden in this picture?
>
> [insignificant_hawkeye.png](insignificant_hawkeye.png)
>


`stegsolve` reveals text in the image in the LSBs of the RGB channels:

```
6e616374667b6834 776b3379335f3135  nactf{h4 wk3y3_15
5f7468335f6c3334 73745f3531676e31  _th3_l34 st_51gn1
663163346e745f62 31747d0000000000  f1c4nt_b 1t}.....
```

flag: `nactf{h4wk3y3_15_th3_l34st_51gn1f1c4nt_b1t}`