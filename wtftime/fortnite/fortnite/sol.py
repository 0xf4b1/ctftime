from itertools import cycle
import binascii


# test= cycle('test')
# for i in range(10):
# 	print(next(test))


r=bytes.fromhex('6968766f606e776c2d2d21262138475c5b5a475b545e475c6b6a776b646e776c6b6a772b646e776c6b6a776b646e776c6b6a776bbadf04036b6a776c616a846f')
print(r)
r1 = repr(r)
# print(type(repr(r1)))
# print(repr(r1))

content = '\x02\x02\x01\x04\x04\x00\x00\x00FGVMEV0000000000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00'


key = bytearray(len(content))
for i in range(len(content)):
	key[i] = ord(content[i]) ^ r[i]

print(key)
# print(':'.join(hex(ord(x))[2:] for x in key))

# test = ''
# for i in range(len(content)):
# 	test += chr(key[i] ^ ord(r1[i]))

# print(':'.join(hex(ord(x))[2:] for x in test))


def forti_xor(s1):
    xor_key = key
    message = ''.join(chr(c ^ k) for c, k in zip(s1, cycle(xor_key)))
    return message

print(repr(r))
print(repr(forti_xor(r)))
