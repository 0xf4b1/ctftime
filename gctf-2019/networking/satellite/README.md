[../](../../)

# Satellite

## networking

> Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?
>
> Find something to do that isn't staring at the Blue Planet.
>
> [768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf.zip](https://storage.googleapis.com/gctf-2019-attachments/768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf)

The `init_sat` binary asks for a satellite name where to connect to. When looking into the provided PDF you will notice the name `osmium`, that you can enter to connect to. It will print a link to a google drive document that hints you to use `wireshark`.

So start `wireshark` and start capturing the network traffic, you will notice unencrypted traffic when you choose `(a) display config data` and the flag is stored in the password field.

flag: `CTF{4efcc72090af28fd33a2118985541f92e793477f}`