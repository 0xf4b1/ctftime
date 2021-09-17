[../](../)

# Unknown - Prison Cell 2

> Well, okay, you’re back in the cell again, and they changed the lock to something quite heavier. This one cannot be picked with a paperclip… So, is this where the mission ends? PLING, another message from the boss. Another GIF… No wait, not only a GIF, also text: "Hi AGENT, I was just contacting you to say that we’re running out of time, if you fail to reach the office and pull the self destruction lever in under 30 minutes, they will already have executed their evil plan. I’m counting on you!." Well, that wasn’t too helpful... What to do, what to do?

## Challenge: Hash-meee (misc)

> I heard BotBot, the resident Discord bot, is experimenting with hashing. He specifically wants to see 2 different strings, both starting with `gctf`, that have the same md5 hash. He will reward this with a flag. You can access our Discord with the following invite link: https://discord.gg/FbrXTjvv To solve this challenge DM BotBot on discord using the command `!hashme` followed by the two strings, encoded in hex. E.g. if your strings are "gctfhello" and "gctfhola" you would send `!hashme 6763746668656c6c6f 67637466686f6c61`

## Solution

Calculate two different strings with same MD5 hashsum that have the common prefix `gctf` by using [hashclash](https://github.com/cr-marcstevens/hashclash).

    first: 67637466e01ac9ff5c61001118185c74d71477a221a9d67e5449d5e268ef00ae6f0bfe77f37b7e4689850714d7a0499cad1917c6358b701ee0a1067e3c00c1d40e011e9dcbeb0c3cf1d42035d0032ae0ecf4f5c939cfc6e4ba350b403a69e133f14c8580cebc5b931e884319af29da14a3d7e898fe624c9817beb32b42d176ba
    second: 67637466e01ac9ff5c62001118185c74d71477a221a9d67e5449d5e268ef00ae6f0bfe77f37b7e4689850714d7a0499cad1917c6358b701ee0a1067e3c00c1d40e011e9dcbeb0c3cf1d32035d0032ae0ecf4f5c939cfc6e4ba350b403a69e133f14c8580cebc5b931e884319af29da14a3d7e898fe624c9817beb32b42d176ba

flag: `CTF{h4sh_m3_tw1c3_1245fd3}`

> Look, the guard has fallen asleep outside the cage, and he’s wearing the keys in his belt, try to reach for them! You can almost reach them... But they’re a little bit far away, suddenly the guard snores and falls in another sleeping position, which makes it possible for you to take the keys. You’re locking up and are able to escape unseen.