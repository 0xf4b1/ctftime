# web_salad

## Web - Points: 220

> Let us start with a very basic web challenge.<br>
>
> Here is your <a href="https://sec-army.ml/web_salad/login.php">web application</a> <b>Lets HACK</b><br>
>
> Author: TheIllusion
>

View the source of the login page, there are user credentials given as comment at the bottom, encrypted with md5.

	username: ee11cbb19052e40b07aac0ca060c23ee
	password: bdc87b9c894da5168059e00ebffb9077

Simply reverse them using online services and login with the credentials username `user` and password `password1234`. After the login, a weired image is shown, some keys are disabled that should prevent you from right clicking or opening dev console. To view the source simply goto view-source:https://sec-army.ml/web_salad/index.php, at the bottom is a base64 encoded string as comment that contains the flag.

	$ echo "c2VjYXJteXt3M2JfYnVjazN0XzNuYzB1bjdlcjNkfQo=" | base64 -d

flag: `secarmy{w3b_buck3t_3nc0un7er3d}`