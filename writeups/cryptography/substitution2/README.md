# substitution2



The link for the challenge: https://play.picoctf.org/practice/challenge/309?bookmarked=1&page=1
![game](./img/main.PNG) 
Start the challenge 

We get a text file


![file](./img/message.PNG) 

Based on the name of the challange we assume a substitution cipher.

## substitution cipher:

define a key .
shift each letter of the message by the key.

Decryption:
subtract the key from the cipher letter.

(the key is the same in cipher and decryption)

So i used dcode web to run on all 26 possibilities (script attached)
and we get:


![result](./img/cyph.PNG)

after Decryption the text , we will get a readable text after subtract the key from the cipher letter.

picoCTF flags usually start with picoCTF, combine 2 parts {} and we done!

The flag is: PICOCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
