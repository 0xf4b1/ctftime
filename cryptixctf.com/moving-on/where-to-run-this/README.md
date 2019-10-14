# Where to run this

## Moving On - Points: 75

> Here is a <a href="https://drive.google.com/file/d/1a4MlpHtdTjY9h6-jK7h7oRnXHMApQ9Zd/view?usp=sharing">zip file</a> <br>
>
> We were wondering what it does....but colorful tiles are awesome! <br>
>
> 
>
> Can you find the secret?<br>
>
> 
>
> **Note:** The flag is in usual format i.e. flag{XXXX...}
>

After unzipping the archive you notice, that the file was actually an APK file (Android app). Decompile the `classes.dex` with `jadx` to get the source code and look in the `AppComputActivity.java` that implements a password check.

flag: `flag{To6i4s_&_Tri5}`