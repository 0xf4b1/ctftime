import socket
from time import sleep


with open("capitals", "r") as file:
    capitals = file.readlines()

with open("usa", "r") as file:
    usa = file.readlines()

dict = {}

for entry in capitals:
    res = entry.replace("\n", "").split(",")
    dict[res[0]] = res[1]

for entry in usa:
    res = entry.replace("\n", "").split(",")
    dict[res[1]] = res[0]

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('chall.2019.redpwn.net', 6001))
sleep(100)

data = str(clientsocket.recv())

print(data)

while True:
    data = str(clientsocket.recv(1024))
    print(data)
    if "Correct" in data:
        continue
    elif "INCORRECT" in data:
        exit(0)
    elif "What is the capital" in data:
        country = data.replace("b'What is the capital of ", "").replace("?\\n'", "")
        print(country)
        print(dict[country])
        clientsocket.send(dict[country].encode())
    else:
        exit(0)
