# Your ID please

## Welcome to the real deal - Points: 300

> This is super secure, confidential research. You are just not meant to access it. Don't even try, it's futile.<br>
>
> Okay, you don't believe me? have the source code too!<br>
>
> https://cryptixctf.com/web4/php_code.txt
>
> <br>
>
> 
>
> https://cryptixctf.com/web4
>

On the website we have to enter an user id and password, the provided PHP code shows how the check is performed. The password needs to equal a variable whose value is not known and the user id should equal `SuperUser1337` to get the `flag` printed out.

Since we don't know the `$secretpassphrase`, we need to find a way to let `strcmp` return 0 for equal strings. Luckily there is a PHP vulnerability that returns 0 when comparing incompatible types.

`curl 'https://cryptixctf.com/web4/login.php' --data 'ID=SuperUser1337&pwd[]=a'`

flag: `flag{Why_Juggl3_th3_Typ5}`