# Hello unknown

## Web - Points: 200

> http://165.22.22.11:25633/
>

When visiting the website, the only thing we can do is trying to login, but we need a username and password. There is a cookie with `user=unknown` set, so what if we simply change it to `user=admin`? After refreshing we are immediately logged in and a new button named 'flag' appears, already done? When clicking the button we only see the flag format without content.

Something is missing, so after logging out again and trying around a bit with the login I noticed another cookie `logged=false` that immediately expires. Let's try both cookies with `curl http://165.22.22.11:25633/?page=flag' -H 'Cookie: user=admin; logged=true` and there it is, the full flag.

flag: `AFFCTF{n3v3r_7ru57_u5er5_1npUt}`