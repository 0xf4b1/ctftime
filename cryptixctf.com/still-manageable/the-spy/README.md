# The Spy

## Still Manageable - Points: 100

> You have been eavesdropping a conversation between two suspects who may know something about the flag. The conversation goes like this:<br>
>
> 
>
> ***HackCrypt1337:*** Do you know, primes are great way to hide secrets!<br>
>
> 
>
> ***n00b1001:*** Whatt..? primes? I don't believe you<br>
>
> 
>
> ***HackCrypt1337:*** You are being too loud!, remember this number,    3073416132828889709313918053975078361304902307, it will be useful to understand the flag. and one more is......<br>
>
> Oh no! Someone is here, you can guess other one yourself. It is trivial anyways.<br>
>
> Here, keep this number safe with you!<br>
>
> 1217323181436745647195685030986548015017805440<br>
>
> 
>
> And they leave....<br>
>
> 
>
> Get the flag!
>

Simple RSA with weak n.

p, q from `factordb.com`.

`./RsaCtfTool.py -n 3073416132828889709313918053975078361304902307 -p 13558774610046711780701 -q 226673591177742970257407 -e 65537 --uncipher 1217323181436745647195685030986548015017805440`

flag: `flag{w3ak_R5A_bad}`