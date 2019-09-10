from pwn import *
import random

r = remote('165.22.22.11', 5566)
data = r.recvuntil('Set value:').splitlines()

# extract the timestamp and set it as seed
seed = str(data[1]).split(' ')[3][1:-2]
random.seed(float(seed))

# generate the same random numbers
for i in range(3, len(data)-3):
	random.randint(0,31337)

# send the next random number and receive the flag
r.sendline(hex(random.randint(0,31337)))
print(r.recvall())