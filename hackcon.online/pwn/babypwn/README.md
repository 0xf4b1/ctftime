# babypwn

> You don't need eip control for every pwn.
>
> Service : nc 68.183.158.95 8990
>
> [q2](q2)

When decompiling the binary you will quickly notice the `nope` function, that is normally called before the binary terminates, and a `win` function, that you have obviously to call to get the flag.

The binary lets you input something via `fgets` and stores it in a 8 bytes buffer that is copied via `strncpy` into another buffer afterwards. The vulnerability is that `fgets` allows to read 0x11 bytes, so you can write out of the target buffer into a variable, that specifies an offset for the target buffer of the `strncpy` operation.

To exploit this we can modify the specific bytes to -2 to write 16 bytes before the target buffer, where the pointer to the `nope` function is stored and overwrite it with the address of the `win` function.

	$ echo -e "\x31\x08\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xff\xff\xff" | ./q2