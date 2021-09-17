[../](../)

# Unknown - Aboard boat

> That was close! The armed guard didn’t notice you. The floor shakes, the boat is leaving the harbor. You are trying to stay hidden. You see two guards coming your way, you sneak into a small scrubber, they pass it, but then one of the guards takes out his phone and says “OK Google” and your phone suddenly makes a noise: PLING! The guards heard it: Guard 1: "Did you hear that?" Guard 2: "It must have come from the scrubber" Guard 1: "Let's have a look!" The guards close in, you are trapped! Suddenly a bell rings in the distance, and a voice talks through speakers: "Every man to their positions, the ship is about to debark, I repeat, every man to their positions." The guards change their course and head for their positions. Pheww, that was close! You find a better place to hide and settle in for the journey. Then you notice an ethernet socket in the wall. Might as well sniff some traffic while you're here.

## Challenge: Noise on the wire (net)

> You connect your laptop to the ethernet socket and start wireshark. It taks a while before something interesting pops up - perhaps the crew as busy with whatever is that they normally do. You look through the packets, and hey, these look pretty interesting...

> https://storage.googleapis.com/gctf-2021-attachments-project/c857cf4543aafba2cd93b1d381088557ccc63e839c505310a8e212ecd8355a0b6fce3421ed822fb0cdb6c63d0aec9ef794c90ace6010695334816fab88b6a740

## Solution

You are given a network capture containing a password-protected `flag.zip`, some exchanged text-based messages, and Javascript code that implements a simple XOR encryption with a short key. After decrypting the exchanged byte strings, you get the password to extract the archive containing the flag.

```python
key = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 202]
cipher = "717f510b44623d391016bd6464450c5e316d1a0c16b95f794d487a2719373000be4a54445843273f080216b97c795348642d19300a169d627a4d645634280c0c21a53a241218"

decrypted = ""
for i in range(0, len(cipher), 2):
    decrypted += chr(int(cipher[i:i+2], 16) ^ key[(i >> 1) % len(key)])

print(decrypted)
```

    zip's password is BossToldMeToSetABetterPasswordSoThisWillHaveToDo1234

flag: `CTF{PleaseAssumeThisIsSomeSecretStuffThankYou}`

> You sneak off the boat and onto the secret island, when the coast seems clear. It’s a small tropical island, and there are guards everywhere. You sneak up behind a tree, and try to figure out a plan to get to the entrance to the headquarters.