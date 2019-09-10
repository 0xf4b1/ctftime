# 1so2nd3er_maschine

## Misc - Points: 100

> Note: put flag into AFFCTF{} format
>
> [1so2nd3er_machine](1so2nd3er_machine)
>

The provided file is wave audio, if you listen to it, it sounds like morse code and also the title of the challenge reminds me of being that. [Here](https://morsecode.scphillips.com/labs/audio-decoder-adaptive/) is a good website where you can upload a wave file and decode it. You will get the result:

```
MBHU PJS HHUX ROAMCTU CGPUIEKZC. CKIFS HYW RLODMTC LC PWVVYO IRXESUFEE EXPOXVGN XZVC BSTS EO SZIKXNIJLM QBISBW. AL NXOM RJRZB KI MYJ YWQZF CKF JAKOTGW ZWKWFX. ANXKYI: "QGEOG VPRTBFH LMNA CS FYHMEL"
```

The output with punctuation characters looks like text but still encrypted. Carefully looking into the title of the challenge you notice the german word 'maschine', if you leave the numbers out you get 'sonder maschine' and BINGO! Thats one model of the Enigma I.

Now we know how the message is probably encrypted. [Here](https://cryptii.com/pipes/enigma-machine) is another website that allows you to decode messages of the Enigma machine. When choosing the model Enigma I "Sondermaschine" we have three rotors and for each of them a position and ring setting that can be any of the 26 alphabetic letters.

Again carefully looking into the title of the challenge, what if we interpret the first part as the key:

```
Rotor 1: I, Position: S, Ring: O
Rotor 2: II, Position: N, Ring: D
Rotor 3: III, Position: E, Ring: R
```

After clearing the plugboard, BOOM! We get german readable text, select include foreign chars to make it more readable and you get the message:

```
dies ist eine geheime nachricht. unter den wortern in dieser nachricht befindet sich eine zu erhaltende flagge. es kann nicht in die hande des gegners fallen. flagge: "royal capital city of krakow"
```

After putting the flag format around it you got it!

flag: `AFFCTF{royal capital city of krakow}`