[../](../../)

# MOAR

## pwn

> Finding yourself on the Foobanizer9000, a computer built by 9000 foos, this computer is so complicated luckily it serves manual pages through a network service. As the old saying goes, everything you need is in the manual.
>
> $ nc moar.ctfcompetition.com 1337

The manpage lets you execute commands when prefixed with `!`, so you can list files and will notice the following file that you can read out:

	!cat /home/moar/disable_dmz.sh

flag: `CTF{SOmething-CATastr0phic}`