# Lara Duek  
laradu@edu.jmc.ac.il  

# custom_encryption – picoCTF 2024 
link:  https://play.picoctf.org/practice/challenge/412?category=2&difficulty=2&originalEvent=73&page=1


## Challenge Description

In this challenge, I was given:

- A Python script called `custom_encryption.py`, which shows how the encryption works.
- A file called `enc_flag` with the encrypted flag.

My goal was to reverse the encryption and recover the original flag.

---

## How I Solved It

The encryption had two layers:

1. **First**, the message was reversed and XORed with the string `"trudeau"`.
2. **Second**, each character was converted to its ASCII value and multiplied by a key times 311.

The key was generated using small prime values (`p = 97`, `g = 31`) and Diffie-Hellman-like logic. I saw that the shared key used in encryption was printed as `a = 88`, `b = 26`, and from trying all values, I found that the correct key was `35`.

---

## How I used the original code

The challenge gave me a Python file (`custom_encryption.py`) that shows exactly how the flag was encrypted. I read the code and understood that the encryption has two layers:

1. The plaintext is reversed and XORed with the string `"trudeau"`.
2. The result is converted to ASCII numbers and multiplied by `key * 311`, where `key` is a number generated using small Diffie-Hellman values (`p = 97`, `g = 31`).

The code also prints the values `a`, `b`, and the final encrypted list.

In my case, the `enc_flag` file already included:
a = 88
b = 26
cipher is: [...]

So I didn't need to run the key generation part. Instead, I guessed the shared key by trying different values from 1 to 100. For each key, I reversed the two encryption steps and checked if the result contained the word `"picoCTF"`.

This is how I built my decryption script.

---


## Decryption Script

```python
def dynamic_xor_decrypt(cipher_text, text_key):
    key_length = len(text_key)
    decrypted = ""
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted += decrypted_char
    return decrypted[::-1]


def decrypt(cipher, key):
    plaintext = ""
    for c in cipher:
        try:
            char_code = c // (key * 311)
            plaintext += chr(char_code)
        except:
            return ""
    return plaintext


with open("enc_flag", "r") as f:
    encrypted_values = eval(f.read())

for possible_key in range(1, 100):
    semi_plain = decrypt(encrypted_values, possible_key)
    final_plain = dynamic_xor_decrypt(semi_plain, "trudeau")
    if "picoCTF" in final_plain:
        print("Found the flag with key", possible_key)
        print("Flag:", final_plain)
        break
```
# final flag
picoCTF{custom_d2cr0pt6d_019c831c}
