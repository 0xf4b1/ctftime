[../](../)

# Johannesburg - Hideout

> Johannesburg is hot, and you are on your way to the secret lair. It seems like it is well fortified, even though you are expected under the alias of the assassin, perhaps it will be a better idea to sneak inside the lair, unseen? You climb up on a brick wall, and jump over it. On the other side you spot a lot of guards, quick, hide in a bush. Now you have to sneak past the guards into the main building's entrance.

## Challenge: Konski-Hiakawa Law of Droids (reversing)

> In this challenge, you have to find the flag using memory forensics. Good luck! Note, surround the flag with CTF{...} to submit it. Note, API Level 25 is what you're looking for.

> https://storage.googleapis.com/gctf-2021-attachments-project/06f923cd67e28af3d409ff78fd8385ae6457f4ea153a827e9a39c57293b7832e5064e75b4c48c1ac95bd62504a495258a04baec89e813eba7758fb88db329ca8

## Solution

After decompiling the APK file, you get the source code of an Android app that writes data in some files.
Searching for known strings, such as `gCTF:KEY:` from the `native-lib.cpp`, in the `bzImage.elf` reveals an interesting string right after the occurrence.

    strings bzImage.elf | grep -A1 gCTF:KEY:
    gCTF:KEY:
    SB:575756

flag: `CTF{SB:575756}`

> Congratulations, you successfully sneaked past the guards, and now you are inside the main building in the secret lair. Look over there, a safe case! Wait, what, it is open, no way! It’s only a photo inside, what a disappointment... But wait, don’t get hasty now, it seems like it’s an airport in the picture, it’s Heathrow, and there is something scribbled on the back, it’s coordinates to a secret warehouse at Heathrow, it seems like London is calling!