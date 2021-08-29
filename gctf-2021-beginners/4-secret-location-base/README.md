[../](../../)

# Secret Location - Base

> "Welcome back AGENT. It seems like you've got a marvelous lead that perhaps gives a clue about where you should head to next. Visit the lab, and talk to that Dr. Klostermann, or is it Cloysterman?, he will know how to decrypt the device.. you would think". ... Dr Klostermann: "Welcome to the technical department AGENT, I’m Dr. Klostermann, and this is my assistant, Konstantin. Let’s not waste any time, is that the device that you’re holding in your hand? Konstantin, start the basic procedure."

## Challenge: Electronics Research Lab (hw)

> Welcome back AGENT. It seems like you got a lead that perhaps gives a clue about where the next journey on your quest goes. Visit the lab, and talk to Dr. Klostermann, he will know how to decrypt the device Note: If you solved the challenge before but could not submit the flag, please try again, we had the wrong flag in our database.

> https://storage.googleapis.com/gctf-2021-attachments-project/eafc850054672b6e5242ffb8b2f3110760a20cabcca90a69c00c4f4c91912c2e43c5ea8e68ad529692da3aac7763f6301888b843c7ee5e94699e22c8ea94db5c

## Solution

```python
set_mask = [67,20,2,57,0,5,18,1,64,2,1,18,1,4,0,64,16,2,0,9,0,0,8,65,22,0,0,0,65,22,1,4,66,1,0,24,67,24,2,65,16,2,68,19,72,2]
clr_mask = [0,3,16,4,25,2,65,2,17,0,6,65,0,2,0,16,64,4,3,0,1,8,0,24,64,0,5,2,16,65,6,0,21,0,2,65,24,67,8,18,64,0,19,64,2,117]

flag = ""
state = 0
for i in range(len(set_mask)):
    state |= set_mask[i]
    state &= ~clr_mask[i]
    flag += chr(state)

print(flag)
```

flag: `CTF{be65dfa2355e5309808a7720a615bca8c82a13d7}`

> You’re taking a stroll in the lab, when Dr. Klostermann is calling your name: "Agent, we’ve discovered the origin of the device. This time you won’t be able to reach your destination by air, but by the new Trans-Sibiriean Railway, as opposed to the old one, which runs along side it at the same time, it is a bit odd. And it goes to Shenzhen. I am sorry agent, but the further you go into this task, the more precautions you will have to take, and remember, the enemy can be anyone. It could be a conductor, the engineer, it could even be our own people that will meet you at the spot you need to be at. Be selective with who you trust. I think you got the point, go now, I got much to do. Agent, much depends on you!."