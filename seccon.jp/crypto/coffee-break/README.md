# coffee_break

## crypto - Points: 60

> The program "`encrypt.py`" gets one string argument and outputs ciphertext.
>
> 
>
> Example:
>
> ```
>
> $ python encrypt.py "test_text"
>
> gYYpbhlXwuM59PtV1qctnQ==
>
> ```
>
> 
>
> The following text is ciphertext with "`encrypt.py`".
>
> ```
>
> FyRyZNBO2MG6ncd3hEkC/yeYKUseI/CxYoZiIeV2fe/Jmtwx+WbWmU1gtMX9m905
>
> 
>
> ```
>
> 
>
> Please download "`encrypt.py`" from the following url.
>
> 
>
> - [encrypt.py](https://score-quals.seccon.jp/files/encrypt.py_b7d6c2e28d7f4eee9db8673b5c82191e54d1fea1)
>
> [encrypt.py](encrypt.py)
>

In this challenge we have to decrypt the given ciphertext that was encrypted with the given script.

The encryption process takes each character of the plaintext and adds the corresponding character of the key at the same index, whereby the key is repeated and the output shifted in printable ASCII range.

Afterwards the output is encrypted with `AES` and another key and then `base64` encoded.

So first of all we decode the `base64` encoded ciphertext and decrypt the resulting `AES` encrypted ciphertext with the key. Afterwards we have now to subtract from each character of the next ciphertext the corresponding character of the key to get the plaintext and remove the padding to get the flag.

flag: `SECCON{Success_Decryption_Yeah_Yeah_SECCON}`