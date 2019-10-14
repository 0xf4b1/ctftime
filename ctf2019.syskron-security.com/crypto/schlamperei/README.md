# Schlamperei

## Crypto - Points: 200

> I suspect the new IoT-Gateway module, which has been installed on the machine, is sending back some data to the vendor. I was able to extract a message from the network traffic, but the content doesn't make sense. Maybe the setup archive that I found on the machine is helpful.
>
> [message.txt](message.txt)
> 
> [setup_customerID_9721.zip](setup_customerID_9721.zip)

The provided ZIP archive is password protected with a very weak password. I used `john` to crack it.

	$ zip2john setup_customerID_9721.zip > hash
	$ john hash

The password is `9721` and lets to extract the archive. It contains a GPG encrypted sessionkey `sessionkey_2fishecb.txt.gpg` that might be the key to decrypt the `message.txt`.

Additionally there is a `71062c43B022BE72_public-key.txt` that contains public and private keys! Lets import the keys with `gpg --import 71062c43B022BE72_public-key.txt`, but we need the passphrase. When looking in the `README.txt` there is a note at the bottom that states:

    NOTE: The old default encryption password 'VMC' has been replaced since 09/2018. Please use the new one.

And looking at the top:

    Copyright MY F4N74571C M4CH1N3 C0rP (MFMC) - formerly known as V41U3 M4CH1N3 C0rP (VMC)

So `MFMC` might be the password. This allows to import the GPG keys and decrypt the sessionkey:

    $ gpg -d sessionkey_2fishecb.txt.gpg
      gpg: encrypted with 2048-bit RSA key, ID 71062C43B022BE72, created 2019-09-15
      "MYF4N74571CM4CH1N3C0rP (MFMC)"
      A0 C9 18 74 33 F2 2C 00 83 2B 1E 99 22 10 1A 6A

The filename of the key hints that the message is encrypted with `TWOFISH ECB`, so I quickly found [this](http://twofish.online-domain-tools.com/) website where I could paste the hex values of the message and the key to get the flag. 

flag: `{silence_is_golden}`