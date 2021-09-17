key = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 202]
cipher = "717f510b44623d391016bd6464450c5e316d1a0c16b95f794d487a2719373000be4a54445843273f080216b97c795348642d19300a169d627a4d645634280c0c21a53a241218"

decrypted = ""
for i in range(0, len(cipher), 2):
    decrypted += chr(int(cipher[i:i+2], 16) ^ key[(i >> 1) % len(key)])

print(decrypted)