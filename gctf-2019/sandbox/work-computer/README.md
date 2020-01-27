[../](../../)

# Work Computer

## sandbox

> With the confidence of conviction and decision making skills that made you a contender for Xenon's Universal takeover council, now disbanded, you forge ahead to the work computer.   This machine announces itself to you, surprisingly with a detailed description of all its hardware and peripherals. Your first thought is "Why does the display stand need to announce its price? And exactly how much does 999 dollars convert to in Xenonivian Bucklets?" You always were one for the trivialities of things.
>
> Also presented is an image of a fascinating round and bumpy creature, labeled "Cauliflower for cWo" - are "Cauliflowers" earthlings?  Your 40 hearts skip a beat - these are not the strange unrelatable bipeds you imagined earthings to be.. this looks like your neighbors back home. Such curdley lobes. Will it be at the party?
>
> SarahH, who appears to be  a programmer with several clients, has left open a terminal.  Oops.  Sorry clients!  Aliens will be poking around attempting to access your networks.. looking for Cauliflower.   That is, *if* they can learn to navigate such things.
>
> readme.ctfcompetition.com 1337

When you connect to the service, you get a shell and will notice two flags in the current directory. But simply printing out the contents is not possible, since `cat` is not present on the system, so we have to find another way to print out the file contents. When we inspect the filesystem and look for available commands in the `/bin` folder, we can see, that it is a `busybox` environment, a single binary, that has many of the utilities build-in. All the shell commands are linked to `busybox`, and it will act like the first passed argument, that is the name of the link.

But calling `busybox` directly with `cat` as first argument results in the following:

	$ /bin/busybox cat
	busybox can not be called for alien reasons.

Also calling `busybox` directly without arguments results in this message, so there is a check that the first argument is not `busybox` itself.

We can circumvent that check by calling `busybox` via `/lib/libc.musl-x86_64.so.1` or `ld-musl-x86_64.so.1`. This allows to access all the build-in utilities and we can `cat` the first flag:

	$ /lib/libc.musl-x86_64.so.1 /bin/busybox cat /challenge/README.flag

flag: `CTF{4ll_D474_5h4ll_B3_Fr33}`

In the same way, we can add read permissions for the second flag and then also read it out:

	$ /lib/libc.musl-x86_64.so.1 /bin/busybox chmod +r /challenge/ORME.flag
	$ /lib/libc.musl-x86_64.so.1 /bin/busybox cat /challenge/ORME.flag

flag: `CTF{Th3r3_1s_4lw4y5_4N07h3r_W4y}`