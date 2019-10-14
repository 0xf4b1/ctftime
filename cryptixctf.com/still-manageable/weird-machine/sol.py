import random
import string

alphanum = string.ascii_letters + string.digits

seq = "000010010101110100011000010100110011110101100010011000000001111100110101011000110101010100110100010010110101101001010101001101100110110000111100011000010001111000001011000011010000100000000001010101100011100000100101"

def random_string(rand_seed, length):
    random.seed(rand_seed)
    rand_string = ''
    for i in range(length):
        rand_string += alphanum[random.randint(1,1000)%len(alphanum)]
    return rand_string

def decrypt(key, message):
    decrypted = ''
    for i in range(len(message)):
        k = message[i]^ord(key[i])
        decrypted += chr(k)
    return decrypted

data = [int(seq[i*8:(i+1)*8],2) for i in range(len(seq)//8)]

for r in range(10000):
    key = random_string(r, 27)
    text = decrypt(key, data)
    if 'flag' in text:
        print(text)
        break