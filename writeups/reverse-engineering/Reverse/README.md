# Nicole Kazantsev CTF Reverse

1. Downloaded the challenge binary from the picoCTF webshell using:  
   ```bash
   wget https://artifacts.picoctf.net/c/270/ret
   ``` 
   (save_file.png)

2. Checked the file type using:
   ```bash
   file ret
   ```
   This confirmed it was a **Linux executable**.
   (file_type.png)

3. Tried to execute the file:
   ```bash
   ./ret
   ```
   but received the error **"permission denied"**.
   (run_file.png)

4. Changed file permissions to make it executable:
   ```bash
   chmod 777 ret.2
   ```
   After running it again, the program asked for a password.
   (access_denied.png)

5. Searched the binary for readable strings that might reveal clues:
   ```bash
   strings ret.2 | grep pico
   ```
   I found the **flag** directly inside the binary.
   (flag.png)
   picoCTF{3lf_r3v3r5ing_succe55ful_9ae85289}

