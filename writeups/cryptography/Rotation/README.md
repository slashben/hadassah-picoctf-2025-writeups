# Rotation
This is the write-up for the challenge "rotation" from PicoCTF 2023 cryptography.
# Description
You will find the flag after decrypting this file
the file:
<img width="1310" height="188" alt="image" src="https://github.com/user-attachments/assets/2decc038-c0bb-4af0-99c6-8280c905b627" />

This looks like a ceaser cypher (and given the name of the challenge). 
We recognize the flag pattern that is supposed to look like "picoCTF{...}".
If we look at the lettters, we can see that there is a shift of 8.

<img width="372" height="459" alt="image" src="https://github.com/user-attachments/assets/177dd39b-584a-4e61-9b89-7e614187028f" />

We'll use a script to shift back and we'll get the following result:
picoCTF{r0tat1on_d3crypt3d_555957f3}

