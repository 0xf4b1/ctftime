[../](../../)

# Moscow - Streets

> The person drives into a narrow back alley and despite the danger you try to continue on and give chase. It is impossible to see who they are, clothed all in black and a helmet covering the face. You need to intercept them somehow.

## Challenge: High Speed Chase (misc)

> You chase them through city streets until you reach the high way. The traffic is pretty rough for a car and you see them gaining ground - should have hotwired a motorbike as well! Too late for that. You look around your car to spot anything useful, and you notice this is actually one of the new self driving cars. You turn on the autopilot, pull out your laptop, connect it to the system, and enter the not-so-hidden developer's mode. It's time to re-program the autopilot to be a bit more useful in a chase! To make it easier, you replace the in-car LiDAR feed with a feed from an overhead sattelite - you also display it on the the entertainment system. Now all that's left to do, is to write a better controlCar function!

> https://high-speed-chase-web.2021.ctfcompetition.com/

# Solution

```javascript
function controlCar(scanArray) {
    var maxi = scanArray[0];
    var idx = 0;
    for (let i = 1; i <= 16; i++) {
        if (scanArray[i] >= maxi) {
            maxi = scanArray[i];
            idx = i - 1;
        }
    }

    if (idx == 8) {
        return 0;
    } else if (idx < 8) {
        return -1;
    } else {
        return 1;
    }
}
```

flag `CTF{cbe138a2cd7bd97ab726ebd67e3b7126707f3e7f}`

> You’re closing in on the motorcycle, but before you have time to act, the person turns to a small path, which is impossible to follow by car. You will never see them again, but wait... They dropped something, a small bag! You look inside of it, and you see what looks to be like an ancient amulet. You return to AGENT X and she tells you that the amulet can be a lead, and that you should return to the base to begin some research.