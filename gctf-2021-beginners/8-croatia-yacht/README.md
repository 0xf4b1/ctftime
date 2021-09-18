[../](../)

# Croatia - Yacht

> You arrive at the location through the coordinates that you got from the assassin, a luxurious yacht. A fat, bald man lies on a puma couch. He sips on a dry martini, smokes the biggest cigar you've ever seen and when he smiles, a golden tooth is revealed. You can’t help but smile back at him, although you think the place seems shady. "Welcome to my yacht, Johnson, finally you show us your face. Have you killed the AGENT now? Good! You’re here to collect your reward I presume? I’ll have my guy finalize the transaction but before you leave I need a small favour from you." It seems that he is mistaking you for the assassin but you don’t mind.

## Challenge: Hide and seek (misc)

> The man hands you a pendrive which you reluctantly connect to your laptop. He says he got it from a partner, and the partner claims that he hid valuable information in that PNG there. The problem is, it looks empty. See if you can find anything.

> https://storage.googleapis.com/gctf-2021-attachments-project/bf0b845d9cc07ec1ee2c97189fe4577b7571a2343e919baa911d88b0f654c035c13f0e8770085ce775b9619d1ebbf357f31327ab7463125bd35f1847b2d225f0

## Solution

Extract all characters from all the 1-byte length `eDIH` chunks in the PNG image and decode the resulting base64 encoded string

    echo "Q1RGe0RpZFlvdUtub3dQTkdpc1Byb25vdW5jZWRQSU5HP30=" | base64 -d

flag: `CTF{DidYouKnowPNGisPronouncedPING?}`

> I see you are a person of many qualities. I must say I am impressed. One last thing, I just have to ask, see you always struck me as a fan of sports, I don’t know why. What do you prefer? Basketball or Soccer?

> Basketball (10): "Well then, if you are hungry for more missions, I got a thing in NYC for you. The person who wanted the AGENT dead, also owns this office complex, and needs a guy to guard a certain event that will take place there tomorrow. I'm sorry that I can’t reveal more information than that, but at least it is well paid, and perhaps you can watch a game of basketball on your way home, deal?."

> Soccer? Do you mean football? (11): "Well then, if you are hungry for more missions, I got a thing in London for you. The person who wanted the AGENT dead, also owns this warehouse near Heathrow, and needs a guy to guard a certain event that will take place there tomorrow. I'm sorry that I can’t reveal more information than that, but at least it is well paid, and perhaps you can watch a game of football on your way home, deal?."