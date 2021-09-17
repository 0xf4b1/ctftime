[../](../)

# Unknown - Inside Secret Base

> You are walking through a corridor, but hey, what was that?! Changing room, you enter and find a uniform, you put it on, wow, you’re hot in uniform! You peek outside, and notice a sign on the wall that says "Master office, 100m". You close the door and plan your next steps. You're pretty close to completing your mission, but if anything goes wrong everything you've learnt will be lost. So you pull out your laptop, write down everything you know, encrypt it, hit send, and in horror watch an error appearing on the screen! You start investigating and quickly find out that a few blocks on your SSD chose this moment to die. But it gets worse - one of these blocks contained an encoding routine you needed for the data! No matter, you can implement it yourself in a few minutes, right?

## Challenge: Playing golf (misc)

> What luck! You found the official documentation of the protocol with an example implementation! Uh, but that's that? You can't write to the disk anymore? What?! OK, slowly now. You find a partially writable block with 235 bytes of free space. How are you going to squeeze in the encoder.py's functionality in just 235 bytes?! Well, you guess you have to try.

> playing-golf.2021.ctfcompetition.com 1337

> https://storage.googleapis.com/gctf-2021-attachments-project/bc7b1964e092df46b2b448b524d46ed264380144419d23973d075782363c76a2481639a9a139beef7ab8ba9825511cf96a2f68c1792c5d79be034c30dfee6de7

## Solution

The task is to shrink the given Python source code from 7204 to 235 characters.
Obviously we need to substitute the long list of prime numbers with a simple calculation, shorten the variable names, remove spaces, and use some other tricks.

Below is a working version consisting of 250 characters.

```python
import struct
f=range
A=b"abcdefghijklmnopqrstuvwxyz"
m=lambda t,b:t+struct.pack(">I",len(b))+b
N=[n&0xff for n in f(2,7920) if all(n%m!=0 for m in f(2,n))]
encode=lambda a:bytes([x^y for x,y in zip(m(b"BEGN",A)+m(b"DATA",a)+m(b"END.",A.upper()),N)])
```

The following code allows to half the number of characters by encoding/compressing two chars into one with higher value.

```python
compressed = ""
for i in range(0, len(code), 2):
    compressed += chr((ord(code[i]) << 8) | ord(code[i+1]))
```

After decoding/decompression, the final payload consists of 183 characters, which is sufficient for the length check.

```python
exec("".join([chr(ord(c)>>8)+chr(ord(c)&255)for c in "業灯牴⁳瑲畣琊昽牡湧攊䄽戢慢捤敦杨楪歬浮潰煲獴當睸祺∊洽污浢摡⁴Ɫ㩴⭳瑲畣琮灡捫⠢㹉∬汥渨戩⤫戊丽孮☰硦映景爠渠楮⁦⠲ⰷ㤲〩⁩映慬氨渥洡㴰⁦潲⁭⁩渠昨㈬温⥝੥湣潤攽污浢摡⁡㩢祴敳⡛硞礠景爠砬礠楮⁺楰⡭⡢≂䕇丢ⱁ⤫洨戢䑁呁∬愩⭭⡢≅乄⸢ⱁ⹵灰敲⠩⤬丩崩"]))
```

```
== proof-of-work: disabled ==
Please send your code followed by a line containing only #END
- We will rstrip the lines for you btw.
- Time limit is 5 seconds.
exec("".join([chr(ord(c)>>8)+chr(ord(c)&255)for c in "業灯牴⁳瑲畣琊昽牡湧攊䄽戢慢捤敦杨楪歬浮潰煲獴當睸祺∊洽污浢摡⁴Ɫ㩴⭳瑲畣琮灡捫⠢㹉∬汥渨戩⤫戊丽孮☰硦映景爠渠楮⁦⠲ⰷ㤲〩⁩映慬氨渥洡㴰⁦潲⁭⁩渠昨㈬温⥝੥湣潤攽污浢摡⁡㩢祴敳⡛硞礠景爠砬礠楮⁺楰⡭⡢≂䕇丢ⱁ⤫洨戢䑁呁∬愩⭭⡢≅乄⸢ⱁ⹵灰敲⠩⤬丩崩"]))
#END
Testing your code (length 183)...
[I][2021-09-11T17:18:29+0000] Mode: STANDALONE_ONCE
[I][2021-09-11T17:18:29+0000] Jail parameters: hostname:'NSJAIL', chroot:'/', process:'/usr/bin/python3', bind:[::]:0, max_conns:0, max_conns_per_ip:0, time_limit:5, personality:0, daemonize:false, clone_newnet:true, clone_newuser:true, clone_newns:true, clone_newpid:true, clone_newipc:true, clone_newuts:true, clone_newcgroup:false, clone_newtime:false, keep_caps:false, disable_no_new_privs:false, max_cpus:0
[I][2021-09-11T17:18:29+0000] Mount: '/' -> '/' flags:MS_RDONLY|MS_BIND|MS_REC|MS_PRIVATE type:'' options:'' dir:true
[I][2021-09-11T17:18:29+0000] Mount: '/home/user/empty' -> '/home/user/full_tester.py' flags:MS_RDONLY|MS_BIND|MS_REC|MS_PRIVATE type:'' options:'' dir:false
[I][2021-09-11T17:18:29+0000] Mount: '/proc' flags:MS_RDONLY type:'proc' options:'' dir:true
[I][2021-09-11T17:18:29+0000] Uid map: inside_uid:1000 outside_uid:1000 count:1 newuidmap:false
[I][2021-09-11T17:18:29+0000] Gid map: inside_gid:1000 outside_gid:1000 count:1 newgidmap:false
[I][2021-09-11T17:18:29+0000] Executing '/usr/bin/python3' for '[STANDALONE MODE]'
Running encode() on all tests...
Saving results...
[I][2021-09-11T17:18:29+0000] pid=3 ([STANDALONE MODE]) exited with status: 0, (PIDs left: 0)
Verifying tests...
All tests passed!
CTF{EncodingSuccessfulIntelReceivedCorrectly}
Btw, it seems you code-golfed it better than gynvael - let him know how you did it, so he can be jealous :)
```

flag: `CTF{EncodingSuccessfulIntelReceivedCorrectly}`

> You hide your laptop. You see a guard in the distance, there’s nowhere to hide, but hey you are disguised! We’ve to hope that he’s getting the trick. He’s closing in. Guard: "Hello there." You: "Hi." Guard: "I've not seen you before." You: "I'm actually new, name's Greg." Guard: "Hi Greg, I'm Rust" You don't want to get any questions that might reveals you, so you just say: You: "Let's chat more later, yeah?" Guard: "Sure!" Pheew, that felt almost a little bit too easy... Look there is the office