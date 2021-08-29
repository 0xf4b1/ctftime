from randcrack import RandCrack

rc = RandCrack()

with open("robo_numbers_list.txt") as file:
    for line in file:
        line = line[:3] + line[4:7] + line[8:]
        num = int(line) - (1<<31)
        rc.submit(num)

with open("secret.enc", "rb") as file:
    print("".join([chr(c ^ rc.predict_getrandbits(8)) for c in file.read()]))