[../](../../)

# FIRMWARE

## re

> After unpacking the firmware archive, you now have a binary in which to go hunting. Its now time to walk around the firmware and see if you can find anything.
>
> [9522120f36028c8ab86a37394903b100ce90b81830cee9357113c54fd3fc84bf](https://storage.googleapis.com/gctf-2018-attachments/9522120f36028c8ab86a37394903b100ce90b81830cee9357113c54fd3fc84bf)

The file is an image of a ext4 filesystem, that you can mount with:

	# mount challenge.ext4 <mount path>

It contains the typical linux file structure and has a hidden file directly at root:

	& cd mount
	$ ls -la
	[...]
	.mediapc_backdoor_password.gz
	[...]

Copy it out of the read-only filesystem and unzip it:

	$ cp .mediapc_backdoor_password.gz ../
	$ cd ../
	$ gunzip .mediapc_backdoor_password.gz

flag: `CTF{I_kn0W_tH15_Fs}`