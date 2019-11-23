from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64

def encrypt_blob(blob, public_key):
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    blob = zlib.compress(blob)
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted =  ""
    while not end_loop:
        chunk = blob[offset:offset + chunk_size]
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))
        add = rsa_key.encrypt(chunk)
        print(len(add))
        encrypted += rsa_key.encrypt(chunk)
        offset += chunk_size
    return base64.b64encode(encrypted)


def decrypt_blob(blob, private_key):
    blob = base64.b64decode(blob)
    rsa_key = RSA.importKey(private_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    chunk_size = 512
    offset = 0
    end_loop = False
    decrypted =  ""
    while not end_loop:
        chunk = blob[offset:offset + chunk_size]
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += " " * (chunk_size - len(chunk))
        print(len(chunk))
        if len(chunk) == 0:
            end_loop = True
            continue
        decrypted += rsa_key.decrypt(chunk)
        offset += chunk_size
    return zlib.decompress(decrypted)


fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()
fd = open("encrypted_flag.png", "rb")
encrypted_blob = fd.read()
fd.close()
unencrypted_blob = decrypt_blob(encrypted_blob, private_key)
fd = open("flag.png", "wb")
fd.write(unencrypted_blob)
fd.close()
