[../](../../)

# Home Computer

## forensics

> Blunderbussing your way through the decision making process, you figure that one is as good as the other and that further research into the importance of Work Life balance is of little interest to you. You're the decider after all. You confidently use the credentials to access the "Home Computer."
>
> Something called "desktop" presents itself, displaying a fascinating round and bumpy creature (much like yourself) labeled  "cauliflower 4 work - GAN post."  Your 40 hearts skip a beat.  It looks somewhat like your neighbors on XiXaX3.   ..Ah XiXaX3... You'd spend summers there at the beach, an awkward kid from ObarPool on a family vacation, yearning, but without nerve, to talk to those cool sophisticated locals.
> 
> So are these "Cauliflowers" earthlings? Not at all the unrelatable bipeds you imagined them to be.  Will they be at the party?  Hopefully SarahH has left some other work data on her home computer for you to learn more.
>
> [Download Attachment](https://storage.googleapis.com/gctf-2019-attachments/86863db246859897dda6ba3a4f5801de9109d63c9b6b69810ec4182bf44c9b75)

The attachment contains a `NTFS` file system image. First we can mount if with the following command to look at its contents:

	$ mkdir mount
	# mount family.ntfs mount

The structure looks like a typical windows installation and we can find a file called `credentials.txt` in the documents folder with the content:

	I keep pictures of my credentials in extended attributes.

So we have to find out how to read the extended attributes of the filesystem. The tool `getfattr` seems to work out:

	$ getfattr credentials.txt
	# file: credentials.txt
	user.FILE0

It shows that it contains another file, we can save it with the following command:

	$ getfattr --only-values credentials.txt > file

The file is a PNG image that shows the flag.

flag: `CTF{congratsyoufoundmycreds}`