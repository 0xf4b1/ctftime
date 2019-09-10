# MIDI1

## Misc - Points: 50

> plaintext plaintext everywhere....
>
> [midi.pcap](midi.pcap)
>

Normally you would open a pcap file in wireshark, but here it is already enough to simply invoke `strings midi.pcap` to get the flag.

The flag lies in the 6th packet (Server Hello, Certificate) and is the content of the organization name field of the certificate.

flag: `AFFCTF{s3lf_sign3d_is_good_3nough}`