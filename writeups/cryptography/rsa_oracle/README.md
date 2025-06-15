# Lara Duek 
laradu@edu.jmc.ac.il

# rsa_oracle – picoCTF 2024

**Category**: Cryptography  
**Difficulty**: Medium  

---

## Challenge Description

I was given two files in this challenge:

- `password.enc`: a password encrypted with RSA.
- `secret.enc`: a message encrypted with AES-256-CBC using that password.

There was also a server (an RSA "oracle") I could connect to at:
nc titan.picoctf.net 64704


This oracle can decrypt anything **except** the `password.enc` file. So I needed to find a way to recover the password without sending it directly.

---

## How I Solved It

This RSA encryption is vulnerable because of a math trick: RSA is **multiplicative**. That means:

RSA(m₁ × m₂) = RSA(m₁) × RSA(m₂) mod n

So here's what I did:

1. I knew the ciphertext `c` = RSA(password).
2. I chose a small number, `r = 2`, and asked the server to encrypt it → I got RSA(2).
3. I multiplied `c * RSA(2)` to get a new ciphertext that equals RSA(2 × password).
4. I sent this new value to the server, and it gave me `2 × password`.
5. I simply divided that result by 2 to get the real password.


---

## Python Script I Used (`recover_password.py`)

```python
from pwn import *

context.log_level = 'critical'
p = remote("titan.picoctf.net", 64704)

p.recvuntil(b"decrypt.")

with open("password.enc") as file:
    c = int(file.read())

p.sendline(b"E")
p.recvuntil(b"keysize): ")
p.sendline(b"\x02")
p.recvuntil(b"mod n) ")
rsa_2 = int(p.recvline())

p.sendline(b"D")
p.recvuntil(b"decrypt: ")
c_modified = rsa_2 * c
p.sendline(str(c_modified).encode())
p.recvuntil(b"mod n): ")

decrypted = int(p.recvline(), 16)
password = decrypted // 2
password_str = password.to_bytes((password.bit_length() + 7) // 8, "big").decode("utf-8")

print("✅ Password recovered:", password_str)
```

---

## Password I Got
24bcb


---

## Decrypting the Message

I used OpenSSL to decrypt the secret message with the password I found:
```bash
openssl enc -aes-256-cbc -d -in secret.enc -out decrypted.txt
```
When it asked for the password, I typed:
```
Password: 24bcb
```
## Flag

picoCTF{su((3ss_(r@ck1ng_r3@_24bcbc66}




