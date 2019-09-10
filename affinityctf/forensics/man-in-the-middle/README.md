# Man In the Middle

## Forensics - Points: 100

> Note: put flag into AFFCTF{} format.
>
> [Man_In_The_Middle.pcap.gz](Man_In_The_Middle.pcap.gz)
>

Open the pcap file in wireshark. The first packets show ftp traffic, so lets filter for it. Packet 2771 shows a binary upload into a folder called `STRICTLY_CONFIDENTIAL` and the content starts with `VimCrypt~03!`. So lets dump the encrypted data out and search for the key.

While further investigating the pcap file I found unencrypted smtp traffic and in packet 1438 a message that contains `the password is Horse Battery Staple Correct`. First I started googling but it turned out that taking the message literally is the answer.

When opening the data dump in vim and using `Horse Battery Staple Correct` as password it successfully decrypts the message with the content `I_Should_Have_Used_Safer_Connection_...`.

flag: `AFFCTF{I_Should_Have_Used_Safer_Connection_...}`