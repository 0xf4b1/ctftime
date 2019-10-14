# Packets are wonderful

## Forensics - Points: 500

> All the PLCs programs have a high information value. I just have to get it.
>
> [fieldbus.pcapng](fieldbus.pcapng)

When executing `strings fieldbus.pcapng` you can find the base64 string `e3M3X3IwY2tzfQ==` that gives the flag after decoding.

flag: `{s7_r0cks}`