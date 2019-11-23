# Cookie Bank

## Web - Points: 300

> My Website got h4cked and the attacker flooded it with cookies and stored the new password as a cookie , i managed to clear everything and is left with 10 cookies now , go hunt my password down :)
>
> 
>
> <a href="https://sec-army.ml/cookie_bank/">cookie_bank</a>
>
> <br><br>
>
> Author: Umair9747
>

Flag is stored in 5th cookie.

	$ echo "c2VjYXJteXt0aGVfJGh5X2MwMGtpZV93MXRoMW59" | base64 -d

flag: `secarmy{the_$hy_c00kie_w1th1n}`