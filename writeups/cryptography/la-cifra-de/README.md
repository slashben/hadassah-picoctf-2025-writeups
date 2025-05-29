# picoCTF - la cifra de



---
## Challenge Description

I found this cipher in an old book. Can you figure out what it says? Connect with `nc jupiter.challenges.picoctf.org 58295`.

## Challenge link

https://play.picoctf.org/practice/challenge/3?category=2&difficulty=2&page=3

---
## Hints Provided

1.  There are tools that make this easy.
2.  Perhaps looking at history will help.

---
## Analysis and Initial Steps

The challenge title, "la cifra de," and the hints strongly suggested a classical cipher. The hint "Perhaps looking at history will help" pointed towards ciphers with historical significance. The task required connecting to a network service to obtain the ciphertext.

1.  **Connecting to the Server:**
    The first step was to connect to the server using `netcat`:
    ```bash
    nc jupiter.challenges.picoctf.org 58295
    ```
    This provided a block of encrypted text.

    **Ciphertext Received:**
    ```
    [
    
    Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk
    Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd
    Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo
    Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xf966878l}
    Tnj qixxe wkqw-duhfmkseej ipsiwtpznzn uk l puqjarusahjeii htpnjc hubpvkw, hay rldk fcoaso 1467 be Qpot Gltzndtg Fwbkwei.
    Zmp Volpnèxj Nivmpr ox ehkwpfuwp surptorps ifwlki ehk Fwbkwei Jndc uw Llhjcto Htpnjc.
    It 1508, Ozhgsyey Ycizmpmozd itapnzjo tnj do-ifwlki eahzwa xjntg (f xazwtx uk dhokeej fwpnfmezx) ehgy hoaqo lgypr hj l cxneiifw curaotjyt uk ehk Atgksèce Inahkw.
    Merqlsu’x deityd htzkrje avupaxjo it 1555 fd a itytosfaznzn uk ehk ktryy. Ehk qzwkw saraps uk ehk fwpnfmezx lrk szw ymtfzjo rklflgwwy, hze tnj llvmlbkyd ati ehk nydkc wezypry fce sniej gj mkfys uk l mtjxotnn kkd ahxfde, cmtcn hln hj oilkprkse woys eghs cuwceyuznjjyt.
    ]
    ```

---
## Solution Approach

### 1. Identifying the Cipher Type

Given the hints pointing towards an "old" cipher and the nature of the text, the next step was to identify the specific type of classical cipher.
* A portion of the ciphertext was taken and analyzed using an online **cipher identifier tool**.
* The hints suggested historical ciphers. Options considered might include Caesar, Atbash, Substitution, or Polyalphabetic ciphers like Vigenère.
![cipher identifier](https://github.com/user-attachments/assets/58f5479f-48ce-46a3-ac54-279c6743c9e0)

### 2. Decryption using Vigenère Solver

Once Vigenère was identified as the correct cipher (or a strong candidate to try based on the historical hint and tool output):
* The **Vigenère cipher solver on dCode.fr** ([https://www.dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher)) was used.
* The full encrypted message obtained from `netcat` was pasted into the ciphertext field.
* The challenge solution often involves finding a key. For "la cifra de," the key is "vigenere". This key might have been found through:
    * Hints within the challenge description or the ciphertext itself (though not immediately obvious here).
    * Automated key-finding features of tools like dCode.fr (which can attempt to guess key lengths and keys).
* With the ciphertext and the key "vigenere" entered into dCode.fr, the tool decrypted the message.
![decode](https://github.com/user-attachments/assets/eb179669-9a02-4e33-8f43-ef7448701d40)

### 3. The Decrypted  Flag

picoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}



