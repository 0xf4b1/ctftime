# Bronze Ropchain

## Pwn - Points: 50

> Written by: blevy
>
> 
>
> I love meeting new people.
>
> 
>
> `nc chall2.2019.redpwn.net 4004`
>
> [bronze_ropchain](bronze_ropchain)
>

The task name already sugests that it is about `ROP` chain, so lets use `ROPgadget` to try to find one. The tool is able to find all useful gadgets in the binary and chains them together to spawn a shell.

	$ ROPgadget --binary bronze_ropchain --ropchain

Cool, it prints the whole chain in python code, we only need to find a way to get code execution. When starting the binary we are asked for a name. Quickly entering a long input results in a segfault, so there is likely a buffer-overflow.

Lets create a input pattern by using:

	$ /opt/metasploit/tools/exploit/pattern_create.rb --length 64

Then open the binary in `gdb` and enter it when asked for name and note the address, where the segfault occurs. For this binary it encounters at `0x62413961`, then execute the following to get the exact offset where the program returns:

	$ /opt/metasploit/tools/exploit/pattern_offset.rb -q 0x62413961
	[*] Exact match at offset 28

Now simply fill the input buffer with 28 characters of garbage, e.g. fill the padding in the python script with `'A'*28`, and execute the script.

Unfortunatly it does not work directly, after successfully executing the first instruction it jumps to `0x000a8e86` instead `0x080a8e86`. It took me some time to figure out why this is happening, but after looking up a bit it turned out that the input is processed via `fgets` and the `\x0a` is a newline character that causes to stop processing the input at this point.

Luckily `ROPgadget` has the solution already by passing the `--badbytes` parameter and it generates a rop-chain that immediatly works with `fgets`.

	$ ROPgadget --binary bronze_ropchain --ropchain --badbytes "0a"

Exploit:

	$ (python2 sol.py; cat) | ./bronze_ropchain