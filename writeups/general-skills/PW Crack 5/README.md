# picoCTF - PW Crack 5 🧠🔐

## Challenge Description

In this challenge, we’re provided with the following files:

- `level5.py`: the script used to check a password and decrypt the flag.
- `level5.hash.bin`: an MD5 hash of the correct password.
- `level5.flag.txt.enc`: the flag encrypted using a custom XOR function.
- `dictionary.txt`: a wordlist of possible passwords.

The goal is to find the correct password by comparing the MD5 hashes and use it to decrypt the flag.

---

## 🔍 Step-by-Step Solution

### 1. Analyze the script

The `level5.py` file contains:

- A function `hash_pw()` that returns the MD5 hash of the password.
- A function `str_xor(secret, key)` that XORs the encrypted flag with the password (repeating the password if needed).
- A main check that verifies if the hash of the entered password matches the one stored in `level5.hash.bin`.

### 2. Load the data

We read:

- The encrypted flag from `level5.flag.txt.enc`
- The correct hash from `level5.hash.bin`
- The password candidates from `dictionary.txt`

### 3. Brute-force the hash

We loop through each candidate, hash it using MD5, and compare it with the stored hash:

```python
from hashlib import md5

with open("level5.hash.bin", "rb") as f:
    correct_hash = f.read()

with open("dictionary.txt", "r") as f:
    candidates = [line.strip() for line in f]

for candidate in candidates:
    if md5(candidate.encode()).digest() == correct_hash:
        print("Password found:", candidate)
        break
```
## ✅ The correct password was: 
eee0

---

## 🔓 4. Decrypt the flag

Using the `str_xor()` function provided in `level5.py`:

```python
def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])

with open("level5.flag.txt.enc", "rb") as f:
    encrypted_flag = f.read()

flag = str_xor(encrypted_flag.decode(), "eee0")
print("Flag:", flag)
```
## 🏁 Final Flag
picoCTF{h45h_sl1ng1ng_fffcda23}


---

## 🧾 Final Script (Complete)

```python
import hashlib

def str_xor(secret, key):
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])

def hash_pw(pw_str):
    return hashlib.md5(pw_str.encode()).digest()

with open("level5.hash.bin", "rb") as f:
    correct_hash = f.read()

with open("level5.flag.txt.enc", "rb") as f:
    encrypted_flag = f.read()

with open("dictionary.txt", "r") as f:
    candidates = [line.strip() for line in f]

correct_password = None
for candidate in candidates:
    if hash_pw(candidate) == correct_hash:
        correct_password = candidate
        break

if correct_password:
    print(f"[✓] Password found: {correct_password}")
    flag = str_xor(encrypted_flag.decode(), correct_password)
    print(f"[✓] Decrypted flag: {flag}")
else:
    print("[-] No matching password found.")
```
## 🧠 Summary
This was a straightforward brute-force password cracking challenge. Once the correct password was found via MD5 comparison, the decryption process using XOR revealed the flag.




