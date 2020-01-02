[../](../../)

# Package

## Reversing - Points: 15

> A package has arrived, come take it =D
>
> (enter the flag in KAF{} format)
>
> [Package.exe](Package.exe)
>

## Solution

In the binary, there is a data string whose characters are shifted according to the following script.

```python
data = 'n9ain9ain9ai_n9aik9l'

text = ''
for c in data:
	code = ord(c)
	if code < ord('a') or code > ord('z'):
		# no lowercase character
		if code < ord('0') or code > ord('9'):
			# no digits
			pass
		else:
			# digits
			code -= 5
	else:
		# lowercase character
		code += 2

	text += chr(code)

print text
```

flag: `KAF{p4ckp4ckp4ck_p4ckm4n}`