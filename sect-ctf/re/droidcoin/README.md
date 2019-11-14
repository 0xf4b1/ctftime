# droidcoin

## rev - Points: 500

> The ‘Night City’ blackmarket is powered by ‘Droidcoin’. An anonymous crypto-currency. The rogue androids seem to have hacked the ‘Nighty City’ ISP ‘PWNcast’. With that access, they are pushing malware that will steal the users Droidcoins. This will fund their operations and we can’t have that. Analyze this sample and find the configuration file so we can locate their command-and-control server. Local players can turn in this flag at the ACNR-booth for swag and streetcred!
>
> [DroidCoinStealer.apk](DroidCoinStealer.apk)

Decompile the APK file with `jadx`. The `MainActivity.java` reveals what the app is essentially doing: it concatenates the first two characters of the manufacturer name and model name of the running device and an information whether the app `com.nightcity.droidcoinwallet` is installed and whether the device is an emulator or not to build a key, it is then passed to the `decryptConfig` method of a native x86 library that should return a JSON response.

We could now further investigate the native library with `Ghidra`, but if we assume that we should have that app installed and should not run it on an emulator, the unknown part of the key are only 4 characters, so I simply brute-forced these characters `gopi` until I got a valid JSON response that contains the flag.

flag: `SECT{1nv3st_1n_dr01dc01nz_noW}`