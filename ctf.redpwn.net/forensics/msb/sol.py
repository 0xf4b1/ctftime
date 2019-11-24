from PIL import Image

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

im = Image.open('lol.png')
pix = im.load()
x, y = im.size

bits = ''

for i in range(x):
    for j in range(y):
        r,g,b,a = pix[i,j]
        bits += str(b >> 7 & 1)

print(decode_binary_string(bits))