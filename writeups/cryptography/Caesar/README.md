# Caesar


The link for the challenge: https://play.picoctf.org/practice/challenge/64?category=2&difficulty=2&page=3

Start the challenge 

We get a text file
![file](./img/file.png) 
 
Based on the name of the challange we assume a Caesar cipher.

## Caesar ciper:

define a key 0-25.
shift each letter of the message by the key.

Decryption:
subtract the key from the cipher letter.

So we build a small python script to run on all 26 possibilities (script attached)
and we get:
![result](./img/result.png)

we see suspicious string saying crossing the rubicon, probably not coincidence.

picoCTF flags usually start with picoCTF, combine 2 parts and we done!

The flag is: picoCTF{crossingtherubiconzaqjsscr}
