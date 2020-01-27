[../](../../)

# Gate lock

## hardware

> So close!!   You have landed.  Getting to the farm was no problem, but these poor, helpless, if not stunning creatures are trapped behind a gate and a fence. All that stands between you and your destiny is this contraption of earthly construction.  Though surely rudimentary, how do such things work?  You barely have experience with three dimensional objects, none the less physical matter  in this particular dimension's structure of forces. (Flag format is binary surrounded by CTF{...})
>
> [38afdc7b7ceac0269928474bae952065b304faf57262138c66f6c3cc4fdba06f](38afdc7b7ceac0269928474bae952065b304faf57262138c66f6c3cc4fdba06f)

First we need to find out what to do with the data in the attachment. Its a `minetest` world, so we have to download and install it first and move the files to the data directory. We also need the mod `Mesecons` that adds logical gates to the game. Then we load the world and have to solve the logical circuit by switching on the correct switches. Since the circuit is not that large, we can quite easy trace it backwards to find the solution.

flag: `CTF{01000010111001000001}`