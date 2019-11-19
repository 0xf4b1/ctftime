# Long Gone

## Forensics - Points: 100

> That data? No it's long gone. It's basically history
>
> 
>
> http://us-central-1.ritsec.club/l/chromebin
>
> 
>
> Authors: Degenerat3, knif3
>

Check out the chrome history of the given user data:

	$ strings Chrome/User Data/Default/History | grep ritsec

It shows some urls, visit `http://us-central-1.ritsec.club/l/relaxfizzblur` to get the flag.

flag: `RITSEC{SP00KY_BR0WS3R_H1ST0RY}`