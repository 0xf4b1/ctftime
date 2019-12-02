# Cup of Joe: The Server

## Mega - Points: 100

> On the first leg of the journey, I was looking at all the life, there were plants and hills and rocks and things, there was java and mugs and caffeine.
>
> 
>
> chal.tuctf.com:32000
>

Communicate with the HTCPCP protocol:

	$ printf "BREW /teapot HTTP/1.0\r\nHost: chal.tuctf.com\r\n\r\n" | nc chal.tuctf.com 32000

	HTCPCP/1.0 418 I'm a teapot. Go to /broken.zip
	 Server: JavaServer
	 Content-Length: 0
	 Content-Type: Short and stout

flag: `TUCTF{d0_y0u_cr4v3_th3_418}`