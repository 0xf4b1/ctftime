[../](../../)

# Timeout

## reverse - Points: 35

> Stop, wait a minute!
>
> [timeout](timeout)

## Solution

Open the binary in `gdb` and execute the following:

	$ gdb timeout
	b main
	set {int}0x60105c=0x539
	jump generate

flag: `watevr{3ncrytion_is_overrated_youtube.com/watch?v=OPf0YbXqDm0}`