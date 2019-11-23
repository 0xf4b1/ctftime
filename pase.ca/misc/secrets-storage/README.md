# Secrets storage

## Misc - Points: 1000

> That exact place where the most secret honey recipes are stored...
>
> <br/>nc task.pase.ca 24016
>
> [server.py](server.py)
>

The problem lies in the input of the hashsum calculation for the token. Create user `admi` with password `nadmin` and it will have the same hash like user `admin` with password `admin`. Login with the `admi` account and show your secrets, it will also show the admin secret that contains the flag.

flag: `paseca{th15_h0n3y_t4st35_b4d_c4us3_1t_1s_s4lty_l0000l}`