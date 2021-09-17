def RolQWord(n, d):
    return (n << d) & 0xFFFFFFFFFFFFFFFF |(n >> (64 - d))

def RorQWord(n, d):
    return (n >> d)|(n << (64 - d)) & 0xFFFFFFFFFFFFFFFF

def check_key_pad_code(code):
    i = 0
    x = 0
    for digit in code:
        x = x | (digit << i)
        i += 4

    x = x ^ 0o1275437152437512431354
    x = RolQWord(x, 10)
    a = x & 1229782938247303441
    b = x & 0o0210421042104210421042
    c = x & RolQWord(1229782938247303441, 2)
    d = x & RolQWord(0o0210421042104210421042, 2)

    if a == 0x0100101000011110 and b == 0x2002220020022220 and c == 0x4444040044044400 and d == 0x8880008080000880:
        return True
    return False

res = 0
res |= 1229782938247303441 & 0x0100101000011110
res |= 0o0210421042104210421042 & 0x2002220020022220
res |= RolQWord(1229782938247303441, 2) & 0x4444040044044400
res |= RolQWord(0o0210421042104210421042, 2) & 0x8880008080000880

res = RorQWord(res, 10)
res ^= 0o1275437152437512431354

key = hex(res)[2:][::-1]

print(key)
print(check_key_pad_code([int(d) for d in key]))