# Tornado casino

## Misc - Points: 1000

> Vzuh! And your money is mine!
>
> <br/>nc task.pase.ca 24028
>
> [casino.py](casino.py)
>

Predict a number of the random number generator after feeding `randcrack` with enough of its random values.

Exploit script

```python
from pwn import *
from randcrack import RandCrack

rc = RandCrack()

p = remote('task.pase.ca', 24028)
# p = process(['python', 'casino.py'])

print(p.recv())
p.write('2\n')
print(p.recv())
p.write('b33_1_4m_b3333\n')
print(p.recv())

p.write('1\n')
print(p.recv())
for i in range(624):
	p.write('$\n')
	print(p.recv())
	p.write('ff\n')
	result = p.recv().split('\n')
	print(result)
	data = result[0].replace('|', '')
	rc.submit(int(data,16))
	print(int(data,16))

print("feeding done")

prediction = rc.predict_getrandbits(32)
print("predicted %x" % prediction)
p.write('$\n')
print(p.recv())
p.write(str(hex(prediction))[2:]+'\n')
print(p.recv())

```

flag: `paseca{d1d_y0u_r34lly_7h1nk_7h47_7h3_m41n_1nc0m3_0f_b335_15_h0n3y?}`