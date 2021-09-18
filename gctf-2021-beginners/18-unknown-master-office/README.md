[../](../)

# Unknown - Master Office

> You press a button and enter through a tinted glass door. There is a vast oil painting on the wall that depicts a bold man with a scar under his left eye, under his arms rests a white chubby cat. Below the painting is the very same man, and he’s addressing you: "Well, well, well. Isn’t it the trouble maker? Huh, how did you get past the guards? Well, I have a final offer for you. I’ll let you live only on one condition: START WORKING FOR ME! BWAHAHAHAHA-" While he goes on with his monologue about conquering the world and some twisted philosophy about how he is actually the good guy and so on you start discretely fiddling with a control panel labeled "Self destruction". You need to quickly figure out the activation code while he’s distracted.

## Challenge: Strange Virtual Machine (reversing)

> Everyone is coming up with their own programming language these days, so I came up with my own architecture. You can use it to run the attached program that will print the flag for you.

> https://storage.googleapis.com/gctf-2021-attachments-project/c48931b8e0b86e44cc5bcc08b9e1510d05f0bb0cde039c2e96147379fcb88d2f93a9acac37bd7093a92e7fdadce862835fadc0951d76bccbc8afd055ae736099

## Solution

When executing the rom inside the VM, the flag is printed character by character with exponentially decreasing speed.
This indicates there is some exponential calculation going on that we need to identify.
After enabling the printing of the system state after the execution of each instruction in the `main.rs`, we can check the register values after the `MathOp` calculations right before a character is printed out with `Print`.

The `main.rs` contains a data array `INPUT_DATA` whose value at the particular index is added for the corresponding character in the last step.
If you look at the other value, you may recognize the sequence of numbers.
It is the Fibonacci sequence with the index value of the current character added.

With this knowledge, we can calculate the flag ourself and implement a performant recursive function by utilizing memorization to avoid repetitive calculations, and subsequently add the particular value of the data array.

```python
data = [66, 82, 66, 117, 75, 91, 86, 87, 31, 51, 222, 187, 112, 236, 9, 98, 34, 69, 0, 198, 150, 29,
    96, 10, 69, 26, 253, 225, 164, 8, 110, 67, 102, 108, 103, 162, 209, 1, 173, 130, 186, 5, 123,
    109, 187, 215, 86, 232, 23, 215, 184, 79, 171, 232, 128, 67, 138, 153, 251, 92, 4, 94, 93]

mem = {}
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n in mem:
        return mem[n]

    mem[n] = fibonacci(n-1) + fibonacci(n-2)
    return mem[n]

print("".join([chr((data[i] + fibonacci(i+1) + i) % 0x100) for i in range(len(data))]))
```

flag: `CTF{ThisIsAVeryLongFlagAndYouMightRunOutOfJuiceWhileDecodingIt}`

> As the self-destruct sequence starts, total chaos quickly erupts. Alarms go off and guards and other staff start running around in panic. You manage to slip away in the mess and make it outside just as a huge explosion goes off. KABOOM!, you made it. The enemies are beaten, and you have successfully stopped their evil plan to destroy the world!