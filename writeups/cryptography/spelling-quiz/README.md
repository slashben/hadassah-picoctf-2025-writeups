


## Challenge Description

I found the flag, but my brother wrote a program to encrypt all his text files. He has a spelling quiz study guide too, but I don't know if that helps.

## Challenge Link
https://play.picoctf.org/practice/challenge/210?category=2&difficulty=2&page=2


---
## Files Provided

The challenge provided the following files:

* `encrypt.py`: A Python script that encrypts all `.txt` files in its directory and subdirectories using a monoalphabetic substitution cipher.
* `flag.txt`: This file contains the encrypted flag string: `brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm`
* `study-guide.txt`: A larger text file, which has also been encrypted with the same substitution key as `flag.txt`.

---
## Analysis of `encrypt.py`

The `encrypt.py` script clearly showed that each letter of the alphabet was consistently mapped to another random letter, while non-alphabetic characters (like underscores) were preserved. This is characteristic of a monoalphabetic substitution cipher. The script generates one random shuffle of the alphabet and uses this same substitution `dictionary` to encrypt all `.txt` files it finds.

---
## Solution Approach

The core task was to decrypt the `flag.txt` which, based on `encrypt.py`, was encrypted using a **monoalphabetic substitution cipher** with a randomly generated key. The `study-guide.txt` file, being encrypted with the same key, was essential for analysis.

### 1. Identifying the Cipher Type
The `encrypt.py` script clearly showed that each letter of the alphabet was consistently mapped to another random letter, while non-alphabetic characters (like underscores) were preserved.

To confirm this, a portion of the encrypted `study-guide.txt` was analyzed using an online **cipher identifier tool** (like the one at [Boxentriq Cipher Identifier](https://www.boxentriq.com/code-breaking/cipher-identifier)). This tool confirmed the cipher type as a monoalphabetic substitution.

![Analysis cipher](https://github.com/user-attachments/assets/f462b094-2ee6-43de-8f3b-f01a5d2c9ab7)

### 2. Decryption Strategy
The strategy involved using the large ciphertext from `study-guide.txt` to determine the substitution key, primarily through **frequency analysis** and then applying this key to the encrypted `flag.txt`. Online tools were instrumental in this process.

* **Frequency Analysis & Pattern Recognition (using an online solver):**
    A substantial portion of the encrypted `study-guide.txt` was pasted into an **online substitution cipher solver** (e.g., [Boxentriq Substitution Cipher Solver](https://www.boxentriq.com/code-breaking/substitution-cipher)).
    * The tool automatically calculated letter frequencies from the provided `study-guide.txt` ciphertext.
    * These frequencies were compared against standard English letter frequencies to make initial guesses for the substitution key (e.g., the most frequent ciphertext letter likely corresponds to 'e' or 't' in plaintext).
    * The encrypted `flag.txt` content (`brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm`) was also analyzed within the solver.
    * By iteratively substituting letters based on frequency analysis and observing emerging English word patterns in both the `study-guide.txt` sample and, crucially, in the segmented words of the `flag.txt`, the substitution key was gradually revealed. For instance, identifying common 3-letter words like "the" or "and" in the encrypted flag provided strong starting points for deducing letter mappings.


### 3. The Decrypted Plaintext of `flag.txt`
Applying the full substitution key derived from this process, the `flag.txt` content `brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm` decrypted to:
![Result](https://github.com/user-attachments/assets/c8c42b87-738f-4230-91c8-9d99bf7e319d)


`perhaps_the_dog_jumped_over_was_just_tired`

---
## Flag

picoCTF{perhaps_the_dog_jumped_over_was_just_tired}
