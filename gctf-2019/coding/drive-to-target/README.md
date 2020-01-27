[../](../../)

# Drive to target

## coding

> Excellent work!  With your fine sleuthing skills, you managed to find a picture of the handsome creature with its pet biped.  At last friends and companionship may be near!
>
> Like all inhabitants of this world, you spend an inordinate amount of time on the site, stalking and comparing your life to that of others. The first thought that springs to your mind is "Why haven't I ever been to Mauritius on holiday?" followed swiftly by "What is a Mauritius anyway?" But after a while and with language successfully deciphered, you've made contact with the lifeform in the picture, you have a "date"? You're given the address of where to meet your potential interest. "1 Banana way, beware of the glass." An odd address, especially that last part. So how do you get there?  You land your ship and begin to search.
>
> [https://drivetothetarget.web.ctfcompetition.com/](https://drivetothetarget.web.ctfcompetition.com/)

In this challenge you have to move to the meeting point by adjusting longitude and latitude coordinates. You are only allowed to move at max 50km/h, so you are limited in making requests and you can not jump around. After each step you get the information if you are getting closer or getting away.

So this is a scripting challenge, you have to find good parameters to get close to 50km/h moving speed and always look out for the hint of getting closer. At the end, I needed to decrease the steps to be able to get to the exact location.

Script:

```python
import requests
from time import sleep


url = 'http://drivetothetarget.web.ctfcompetition.com/'

lat = 51.6498
lon = 0.0982

def get_token(response):
    token_start = response.text.index('token')+14
    token = response.text[token_start:token_start+140]
    return token

token = get_token(requests.get(url))

state = 0

while True:
    print('lat=%f, lon=%f' % (lat, lon))
    r = requests.get(url + '?lat=%f&lon=%f&token=%s' % (lat, lon, token))
    token = get_token(r)
    print(token)

    print(r.text.splitlines()[18])

    if 'getting closer' not in r.text:
        state = (state + 1) % 4

    if state & 1:
        if state & 2:
            lon += 0.0005
        else:
            lon -= 0.0005

    if not state & 1:
        if state & 2:
            lat += 0.0005
        else:
            lat -= 0.0005

    sleep(5)
```

The final coordinates of the meeting point, that gives the flag:

	lat=51.492100, lon=-0.192800

flag: `CTF{Who_is_Tardis_Ormandy}`