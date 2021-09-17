[../](../)

# Unknown - Outside Secret Base

> You’re still located behind the tree, but now you have a plan on how to get in. You have taken notice that the guards are changing every 45 minutes, and when they do that, you have a gap of about 30 seconds to sneak past and get into the main entrance. It’s risky of course, but you have to give it a try. You run towards the entrance. The new guards have not come yet, but suddenly you hear voices closing in. You trip and fall in front of the main entrance. The voices are very close now, and you glimpse a coat that belongs to a guard behind the corner, but at the last moment you get up and enter! ...only to face another door, this one closed, with an electronic lock - this one brand new. The good news is that it seems you won't be bothered for some time, and whoever is entering or leaving most likely won't notice you if you stand really still next to the wall. You pull out your handy screwdriver, unscrew the panel next to it, and stare at the circuit board for a few seconds. It doesn't look bad, you can do it! You pull out your laptop, attach some wires, and dump the firmware in seconds. It looks fairly simple actually...

## Challenge: Just another keypad (rev)

> You start to analyze the firmware, and uff, that's just a standard Linux. This does makes things easier (imagine having to reverse a custom 8051 RTOS on the spot!). You browse through the directories to find the lock controls, and spot both the right executable and THE SOURCE CODE! But wait... it's in Free Pascal?! Note: To make the final flag append "CTF{" prefix and "}" suffix to the keypad code you've got. E.g. if the code is 1234, the flag would be CTF{1234}

> https://storage.googleapis.com/gctf-2021-attachments-project/babbd5920c39e92529ac48e8df7f90e7b0a0839455599592ae8e9b243297b01302628ab57b4abf3d63c5052b823e5fc3fe8ebd0dc5be77b75f93c24957aeff09

## Solution

You are given Free Pascal source code and must find the correct key.
Based on this source code, the following Python code implements the logic and reverses the operations to derive the key.

```python
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
```

flag: `CTF{3333319552798534}`

> You enter the passcode and hear the electronic lock release. You carefully open the door and slowly move through the corridor.