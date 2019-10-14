# Find The Pass

## Forensics - Points: 479

> Find the admin Password
>
> 
>
> Put the flag in rooters{}ctf
>
> 
>
> get the files here
>
> [chall.cap](https://storage.googleapis.com/rooters-ctf-storage/inc0gnito.cap)
>
> 
>
> **Author**
>
> 
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inc_0gnit
>

The provided network capture contains 802.11 traffic, get the encryption key with the following:

`aircrack-ng inc0gnito.cap`

```shell
                                                                                                             Aircrack-ng 1.5.2 


                                                                                                [00:00:01] Tested 50922 keys (got 20006 IVs)

   KB    depth   byte(vote)
    0    0/  1   FF(32256) CE(25856) 0F(25600) 07(24832) 59(24832) 73(24576) 7B(24320) CC(24320) F5(24320) 34(24064) 17(23808) 3A(23808) 54(23808) 5A(23808) 77(23808) F4(23808) 04(23552) 6F(23552) 7D(23552) 
    1   41/ 54   00(22272) 11(22016) 1E(22016) 25(22016) 33(22016) 3F(22016) 52(22016) 64(22016) 88(22016) 9C(22016) A8(22016) AF(22016) DD(22016) FA(22016) 1D(21760) 3D(21760) B4(21760) DF(21760) E6(21760) 
    2   11/ 19   AD(23808) EB(23808) F4(23808) 06(23808) 5F(23552) 8A(23552) 98(23552) 29(23552) 58(23296) 6F(23296) AB(23296) BC(23296) F9(23296) 0C(23040) 55(23040) 16(22784) 27(22784) 3A(22784) AC(22784) 
    3    2/  5   BE(26112) 58(25600) A7(25600) EA(25088) BF(24320) 5C(24064) 70(24064) B9(24064) BE(24064) 80(23808) 8B(23808) F1(23808) 04(23552) 31(23552) 3A(23552) 1F(23296) 44(23296) 46(23296) B6(23296) 
    4    0/ 10   EF(28928) 8F(27392) 30(27392) BF(26112) AD(25856) 6A(25856) 04(25344) 19(25344) C5(24832) D7(24832) 44(24320) 4E(24320) 26(23808) 5F(23552) 01(23296) 33(23296) 34(23296) 6C(23296) D7(23296) 

                         KEY FOUND! [ FF:DE:AD:BE:EF ] 
	Decrypted correctly: 100%

```

Found the WEP key! Now open the capture in wireshark and add the decryption key.

Edit -> Preferences -> Protocols -> IEEE 802.11
Decryption keys Edit -> Add key type WEP with key FF:DE:AD:BE:EF

Filter for HTTP traffic and look in packets from 192.168.0.100 to 192.168.0.1, they have an basic authorization cookie set that contains `admin:blu3_c0rp_p4ss`

flag: `rooters{blu3_c0rp_p4ss}ctf`