[../](../../)

# ADMIN UI

## pwn-re

> The command you just found removed the Foobanizer 9000 from the DMZ. While scanning the network, you find a weird device called Tempo-a-matic. According to a Google search it's a smart home temperature control experience. The management interface looks like a nest of bugs. You also stumble over some gossip on the dark net about bug hunters finding some vulnerabilities and because the vendor didn't have a bug bounty program, they were sold for US$3.49 a piece. Do some black box testing here, it'll go well with your hat.
>
> $ nc mngmnt-iface.ctfcompetition.com 1337

You already get the hint that the binary might contain a path traversal bug when you read the patchnotes.

So read the patchnotes with the second option and enter:

	../flag

flag: `CTF{I_luv_buggy_sOFtware}`