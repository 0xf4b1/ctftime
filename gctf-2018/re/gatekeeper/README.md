[../](../../)

# GATEKEEPER

## re

> It's a media PC! All fully purchased through the online subscription revolution empire "GimmeDa$". The PC has a remote control service running that looks like it'll cause all kinds of problems or that was written by someone who watched too many 1990s movies. You download the binary from the vendor and begin reversing it. Nothing is the right way around.
>
> [f7e577b61f5b98aa3c0e453e83c60729f6ce3ef15c59fc76d64490377f5a0b5b](f7e577b61f5b98aa3c0e453e83c60729f6ce3ef15c59fc76d64490377f5a0b5b)

Open the binary in `Ghidra` and see how the verification works. It checks for the username `0n3_W4rM` and reverses the input for password and then compares against `zLl1ks_d4m_T0g_I`, so the binary should be called in the following way:

	$ ./gatekeeper 0n3_W4rM I_g0T_m4d_sk1lLz

flag: `CTF{I_g0T_m4d_sk1lLz}`