import random
from math import sqrt
import string
import gmpy2

def hash_it(data, prime):
    hashed_number = 0
    sum_key = ord(data) + prime
    mul_key = ord(data)*prime
    numerator = ord(data)**2 + prime**2 + sum_key**2 + mul_key**2
    denominator = sqrt(ord(data)) + sqrt(prime) + sqrt(sum_key) + sqrt(mul_key)
    hashed_number = int(sqrt(numerator/denominator))
    return hex(hashed_number)


True_hash = '0x1bf770e:0x1d426a2:0x1ae031d:0x1c2ee88:0x206bf4e:0x1710894:0x1e892b6:0xf95208:0x1d7928c:0x101792b:0x1098e50:0x1a6f938:0x10585f1:0x1e892b6:0x101792b:0x1a6f938:0x10585f1:0x18a7822:0x101792b:0x1ebf3cb:0xf53775:0x1d7928c:0x101792b:0x20d61ce'

def primes(start=2):
    n = start
    while True:
        n = gmpy2.next_prime(n)
        yield n


# Find a prime number, so that the hash function calculates for the
# character 'f' the first value of the given hash.
# for i, prime in enumerate(primes()):
#     if hash_it('f', prime) == '0x1bf770e':
#     	print("The {}th prime number is {}".format(i, prime))

# Found prime
prime = 99999721

# Create a lookup table for the output values of the hash function
# for all printable characters
characters = string.printable
table = []

for c in characters:
	table.append(hash_it(c, prime))

# Lookup the hashed characters in the table to get the flag
flag = ""
for i in True_hash.split(':'):
	flag += characters[table.index(i)]

print(flag)