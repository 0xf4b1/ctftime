# findme

## Forensics - Points: 500

> Find me!
>
> Challenge created by Security Risk Advisors for RITSEC CTF
>
> [findme.pcap](findme.pcap)
>

The PCAP contains base64 encoded data in the 40th packet:

```
H4sIAFSZx10AA+3OMQuCQBiH8Zv9FPcFgrvUcw2kIWgydzG1EkQPvZui757S0lSTRPD8lmd43+F/
6cqrWJmaGRMt1Ums3vtitkKHsdGJDqNtKJSeGwup1h628JMrRymFP/ve+Q9/X+5/Kjvkp316t1Vp
p0KNReuKuq17V9x21jb9IwjSPDtuKukGWXXD1AS/XgwAAAAAAAAAAAAAAAAAWDwB38XEewAoAAA=
```

After decoding you get gzip compressed data, uncompress it and get the flag.

flag: `RITSEC{pcaps_0r_it_didnt_h@ppen}`