# COBOL OTP

## crypto - Points: 175

> To save the future you have to look at the past. Someone from the inside sent you an access code to a bank account with a lot of money. Can you handle the past and decrypt the code to save the future?
>
> [cobol_otp_96726770d36dee506e2fc6bc1b7f7f7d.zip](cobol_otp_96726770d36dee506e2fc6bc1b7f7f7d.zip)

In this task you were given a small `cobol` program and an output message that you have to decrypt. From the program's name you already know that the encryption is done via `XOR`, but you don't have the key.

With a proper key with size of the message, the decryption would be hard, but we probably know the first 5 bytes of the plaintext since it will likely be the flag format that is `flag{`. So `XOR`ing the encrypted bytes with the plaintext bytes gives the key and when it is printable, we might be able to infer the next bytes. But the output contains non-printable bytes and at this point I was not sure, whether the plaintext really starts like the guess.

I have never seen this programming language, so in preferred to simply compile and test the program. I could observe, that it does only use the first 10 bytes of the `key.txt` and then reuses them when the message is longer.

With knowing this we can try to always decrypt the first 5 bytes of 10 bytes with the key we derived from the flag format and get the following:

	flag{?????_c4n_?????O2_c3?????_s4v3?????fUtUr?????

And it looks good already, now we only need to guess plaintext for the second part of the key. This is quite easy if you try to guess the part between `_s4v3` and `fUtUr`, where `_th3_` might be the correct plaintext. So `XOR`ing again the encrypted bytes for this part with our guess gives the second part of the key and with the full key and can decrypt the whole message to get the flag.

```python
with open('out', 'r') as file:
	data = file.read().splitlines()[1]

key = ''
flag = ''
guess = 'flag{'

for i in range(5):
	key += chr(ord(data[i]) ^ ord(guess[i]))

for k in range(5):
	for i in range(10*k,10*k+5):
		flag += chr(ord(data[i]) ^ ord(key[i%10]))
	flag += '?????'

print flag

guess = '_th3_'

for i in range(35,40):
	key += chr(ord(data[i]) ^ ord(guess[i-35]))

flag = ''
for i in range(49):
	flag += chr(ord(data[i]) ^ ord(key[i%10]))

print flag
```

flag: `flag{N0w_u_c4n_buy_CO2_c3rts_&_s4v3_th3_fUtUrE1!}`