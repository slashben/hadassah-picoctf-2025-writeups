# basic-mod2 challenge

This is the write-up for the challenge "basic-mod2" challenge in picoCTF 2022
Link for the challenge: [https://picoctf2022.haydenhousen.com/cryptography/basic-mod2](https://picoctf2022.haydenhousen.com/cryptography/basic-mod2)

# The challenge

## Description

In this cryptography challenge you’re given a list of integers. To recover the hidden flag, you must:

1. Take each number **mod 41**.
2. Compute the **modular inverse** of that result modulo 41.
3. Map each inverse to a character using the set:

   * **1–26** → `a`–`z`
   * **27–36** → `0`–`9`  (27→0, 28→1, …, 36→9)
   * **37** → `_`
4. Concatenate the characters and wrap in the picoCTF flag format: `picoCTF{…}`

# Solution steps

## 1. View the prompt

Visit the challenge page and read the instructions:

![Challenge Prompt](./img/challange-start.png)

## 2. Inspect the input

Download the provided message and examine the raw numbers in a Python REPL or terminal:

![Downloaded Numbers](./img/message-text.png)

## 3. Automate with Python

we will use a python script (`solve_basic_mod2.py`) that reads the numbers, applies **mod 41**, computes each **modular inverse**, and maps to characters:

![Python Script](./img/python-sol.png)

## 4. Obtain the flag

Run the script to print the decrypted flag:

![Python Solution](./img/python-console.png)

# Challenge solution key:

```
picoCTF{1nv3r53ly_h4rd_c680bdc1}
```

![Final Flag](./img/solved.png)
### Challenge is solved, good job!
