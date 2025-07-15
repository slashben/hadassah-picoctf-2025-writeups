# interencdec
This is the write-up for the challenge "New Caesar" from PicoCTF 2021 cryptography.
# The challenge
Description
Can you get the real meaning from this file.
<img width="1318" height="274" alt="image" src="https://github.com/user-attachments/assets/1d1b10cf-3208-4f71-9fe3-7621d387a564" />
# Solution
The file looks like its base64 encoded, so we decodec it.
the result:
b"b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='\n"
Westripped and decoded again:
b'wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}'
# Ceasar decryprion
here we can see that it looks like the flag. We know part of the plaintext which is thw beginning of the flag "picoCTF{".
From here we can deduce that we have a shift of 7 letters. We use a python script and decode:
<img width="536" height="276" alt="image" src="https://github.com/user-attachments/assets/448200f6-34f1-4378-b871-632f35000ccd" />

the flag : picoCTF{caesar_d3cr9pt3d_890d2379}
