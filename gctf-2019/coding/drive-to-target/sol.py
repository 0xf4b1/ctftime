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