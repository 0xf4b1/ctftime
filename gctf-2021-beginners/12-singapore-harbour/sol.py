from itertools import permutations
import requests

for x in permutations([3,5,7,8,0], 5):
    print(f"Trying {x} ...")
    response = requests.post("https://old-lock-web.2021.ctfcompetition.com/", data={"v": "".join([str(d) for d in x])})
    if "Hmm" not in response.text:
        print("Found!")
        break