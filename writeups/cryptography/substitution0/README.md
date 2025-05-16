first pico challenge ------->
open the challenge using this link: https://play.picoctf.org/practice/challenge/307?category=2&difficulty=2&page=2

then click on "here" to download the cipher file, you should see something like this :
<img width="614" alt="צילום מסך 2025-05-16 ב-18 37 24" src="https://github.com/user-attachments/assets/81524dc8-26b3-4352-8619-7e7b45bc0c7e" />

open this site : https://www.dcode.fr/monoalphabetic-substitution
copy the fist line in the cypher into the "Knowing the substitution alphabet" field and the rest of the file to the Alphabetic 
substitution ciphertext field, it shoold look like this: 
<img width="1437" alt="צילום מסך 2025-05-16 ב-18 39 42" src="https://github.com/user-attachments/assets/91d10a1e-e09d-4dcf-8f0e-454d026a5512" />

click on "decrypt automaticly" and congrats you cracked the cipher.
<img width="1392" alt="צילום מסך 2025-05-16 ב-18 39 53" src="https://github.com/user-attachments/assets/266eddbc-0425-4636-8fae-1a3ffa172b79" />

flag:  PICOCTF{5UB5717U710N_3V0LU710N_03055505}


second pico challenge ------->
open the challenge using this link: https://play.picoctf.org/practice/challenge/6?category=2&difficulty=2&page=3

right click the certificate link and click on "copy link"

open a pico shell using this link: https://webshell.picoctf.org
log into your account

type "wget https://jupiter.challenges.picoctf.org/static/c882787a19ed5d627eea50f318d87ac5/cert" in the shell
type "openssl x509 -pubkey -in cert -out cert.pub" in the shell
type "openssl rsa -pubin -in cert.pub -text" in the shell
copy the number in the Modulus line 

open https://www.wolframalpha.com

type factor(the modulus we copied)
we got p and q

<img width="1096" alt="צילום מסך 2025-05-16 ב-19 14 34" src="https://github.com/user-attachments/assets/9904fbc4-6fc9-45b7-b069-7e1efb8c936f" />
the pico shell should show this at the end <img width="1346" alt="צילום מסך 2025-05-16 ב-19 16 03" src="https://github.com/user-attachments/assets/5991243c-b43f-425b-bdc5-81b50147ae6a" />

flag:  PICOCTF{73176001,67867967}
