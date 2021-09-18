[../](../)

# Novosibirsk - Chemical plant

> "You must wonder why we have summoned you, AGENT? It has come to our attention that something terrible is about to take place. There is still time to prevent the disaster, and we could not think of anyone more suited for this task than you. We believe that if you can’t solve this quest, neither can anybody else. You have to travel to Novosibirsk, and investigate a suspicious chemical plant. This mission must be executed in secrecy. It’s classified, and it regards the safety of the whole world, therefore we can’t tell you anything more just yet. Go now, you have the fate of the world in your hands."

## Challenge: CCTV (rev)

> You arrive at your destination. The weather isn't great, so you figure there's no reason to stay outside and you make your way to one of the buildings. No one bothered you so far, so you decide to play it bold - you make yourself a cup of coffee in the social area like you totally belong here and proceed to find an empty room with a desk and a chair. You pull out our laptop, hook it up to the ethernet socket in the wall, and quickly find an internal CCTV panel - that's a way better way to look around unnoticed. Only problem is... it wants a password.

> https://cctv-web.2021.ctfcompetition.com/

## Solution

```python
values = [52037, 52077, 52077, 52066, 52046, 52063, 52081, 52081, 52085, 52077, 52080, 52066]
print("".join([chr(val - 0xcafe) for val in values]))
```

password: `GoodPassword`

flag: `CTF{IJustHopeThisIsNotOnShodan}`

> You have now investigated the chemical plant. Nothing seemed to be out of the ordinary, even though the workers acted somewhat passive, but that’s not a good enough to track. It seems like you have a new voice mail from the boss: "Hello there, AGENT! It seems like the corporation that owns the plant was informed by an anonymous source that you would arrive, and therefore they were prepared for your visit, but your colleague AGENT X has a lead in Moscow, we’ve already booked you a flight. FIRST CLASS of course. In fact if you look out of the window, you should be able to see a black car arriving now, and it will carry you to the airport. Good luck!"