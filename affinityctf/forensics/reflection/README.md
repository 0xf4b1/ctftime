# Reflection

## Forensics - Points: 50

> [task.gif](task.gif)
>

Using `binwalk` on the image shows that there are gzip compressed data in it, `binwalk -e task.gif` extracts them and the flag can directly read out of the output.

flag: `AFFCTF{m@k3s_y0u__th0nk}`