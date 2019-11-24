# Rot26

## Pwn - Points: 50

> Written by: blevy
>
> 
>
> `nc chall2.2019.redpwn.net 4003`
>
> [rot26.c](rot26.c)
>
> [rot26](rot26)
>

Get the address of `winners_room` function:

	$ objdump -D rot26 | grep winners_room
	  08048737 <winners_room>:

Get the address of `exit` function in GOT:

	$ objdump -R rot26
	  0804a020 R_386_JUMP_SLOT   exit@GLIBC_2.0

The solution is to overwrite the address of the `exit` function in the Global Offset Table with the address of the `winners_room` function.

This is done with `printf` and a prepared format string, leveraging the `%n` specifier, that writes the amount of written bytes to the destination given as argument. Additionally it can be controlled which argument should be used for the specifier, e.g. `%7$x` chooses the 7th one.

Since there are no arguments given to the `printf` function, it will nevertheless consume the next values that are present on the stack. The data that are present there can easily be leaked with a format string that contains a lot of `%x` specifiers. With this method you can observe that the format string itself lies there after some bytes, for this binary it is the 7th location. So there is an address we know that contains our input we inserted for the `printf` function. We can use this to place arbitrary addresses into the memory we want to write to with the `%n` specifier. To get the values we want to write to the memory location we have to print as much bytes before in the format string.

The format string first contains the address of the `exit` function, then as many bytes as necessary are written till the value of the `winners_room` address is reached and then the `%n` specifier is used to write the amount of written bytes to the address at the 7th argument, which is the address of the `exit` function.

The full exploit looks like this:

	$ (echo -e '\xbc\xb2\xff\xff%134514483x%7$n'; cat) | ./rot26