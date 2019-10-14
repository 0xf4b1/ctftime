from Crypto.Cipher import AES
from base64 import b64decode

key = b64decode("eTB1d0BudGszeT9BRVNlX0tAaVMzX0QzX0R1VXVVISEK")[:-1]
ciphertext = b64decode("ZSbw2ZN3fBsa/0B7VPCWMIAzp94uV7Vjqc5fg/effYA=")

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

print(plaintext)