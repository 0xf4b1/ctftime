[../](../)

# Istanbul - Bazaar

> It’s a hot day, and your skin is cracking and dry. It’s difficult to make your way through the crowded bazaar. A high pitch voice pierces through the soundscape from a salesman that’s trying to sell colorful fabrics and then from another corner comes delicious smells. You spot a hand waving - it’s your contact that you’ve been waiting to meet. "Take a seat, my friend, I’m Gökhan, have you been to Istanbul before? No, really? I’m sure that you will have a great time, I’ve ordered tea for the two of us. Show me the amulet, will you?. Wow, this is really something from my younger days, this is as mysterious as it is beautiful and belongs to “The cloaked brotherhood”. They are very dangerous, and eventhough your quest is urgent, I would advise you to not continue looking for the owner of this. Go home, and forget about it." In the blink of an eye, four tough guys show up, and you start to run together with Gökhan through the crowded marketplace and then up on a rooftop. The tough guys are closing in, but the two of you climb down from the rooftop, run around a corner and are able to hide in two crates.

## Challenge: Twisted robot (misc)

> We found this old robo caller. It basically generates random phone numbers to spam. We found the last list of numbers in generated and also some weird file... Maybe it's got to do with these new beta features they were testing?

> https://storage.googleapis.com/gctf-2021-attachments-project/8d19115532225f6ab25ed208e355b37d55476dfc2c1996cbe81f6e82c96f79a20756d5d53fac7f90bc7841aedab34d0686335bafcdbe2cf07333163719ecff9b

## Solution

```python
from randcrack import RandCrack

rc = RandCrack()

with open("robo_numbers_list.txt") as file:
    for line in file:
        line = line[:3] + line[4:7] + line[8:]
        num = int(line) - (1<<31)
        rc.submit(num)

with open("secret.enc", "rb") as file:
    print("".join([chr(c ^ rc.predict_getrandbits(8)) for c in file.read()]))
```

flag: `CTF{n3v3r_3ver_ev3r_use_r4nd0m}`

> Gökhan is pointing at a parked vehicle. He tells you that you will have to try and reach it and that if you stay where you are, that you will get captured sooner or later. The guards know the neighborhood like their own backpocket. At first you doubt the plan, it seems like a very risky option. Gökhan then finally tells you he's not going to stay there, and his last offer is for you to go with him.

> Stay (7): Gökhan exits the crate, and makes a quick sprint for the car. The tough guys spot him, and they approach. As he enters the car he tries to start it, and the car makes an ominous sound, as the bad guys are closing in. He looks back through the rear window, and sees that the bad guys are about to jump on the back of the car, and they are pulling out guns. He tries to start the car furiously one more time and... IT WORKS! Gökhan disappears off in the distance. You overhear the tough guys when they are talking about a person, “Mesut”, that got classified information. You quickly send a message to the boss to look up the person. After a short wait you receive a response that he is currently on his private yacht in Croatia. Looks like it is time for some travel again.

> Come with Gökhan (8): As you and Gökhan are leaving the crates to enter a car, you spot the tough guys coming after you, and they are pulling out weapons. Gökhan starts the car and the two of you take off. After a decent distance outside of the city, he gives you an invitation to a private conference that will take place in Buenos Aires.