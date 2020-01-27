[../](../../)

# FLOPPY

## misc

> Using the credentials from the letter, you logged in to the Foobanizer9000-PC. It has a floppy drive...why? There is an .ico file on the disk, but it doesn't smell right..
>
> [4e69382f661878c7da8f8b6b8bf73a20acd6f04ec253020100dfedbd5083bb39](4e69382f661878c7da8f8b6b8bf73a20acd6f04ec253020100dfedbd5083bb39)

The icon file contains a ZIP archive that contains two text files.

	$ binwalk -e foo.ico

The `driver.txt` contains the flag. 

flag: `CTF{qeY80sU6Ktko8BJW}`