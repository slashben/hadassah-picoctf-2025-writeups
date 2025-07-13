Name : Bashar Masalha 324923689
# XtraORdinary – picoMini 2025 Challenge

<img width="1259" height="659" alt="Screenshot 2025-07-10 164404" src="https://github.com/user-attachments/assets/3f398fe6-07bb-4bec-bb8b-7fa597c6f4bc" />


In this challenge, we were given two files:

encrypt.py: a script that encrypts a flag using XOR-based logic
output.txt: the encrypted output

The encryption logic :
**1.** First, the flag (flag.txt) is XOR-encrypted with a secret key (secret-key.txt) using a repeating-key XOR.
**2.** Then, the ciphertext is encrypted again multiple times using 10 known strings like:
b'my encryption method'
b'is absolutely impenetrable'
b'ever'
...
b'break it'
**3.** Each of these 10 strings is applied a random number of times, using nested loops and the same XOR function.

The Core idea:
XOR is its own inverse (XOR(XOR(A, B), B) = A)
XORing the same value even number of times cancels it out
o, every encryption layer is either effectively applied once (odd) or not at all (even)
That means we can brute-force all 2¹⁰ = 1024 combinations of "odd or even" for the 10 strings.

for this we wrote this python code:-
------------------------------------------------------
#!/usr/bin/env python3
from binascii import unhexlify
from pwn import xor
import string

# 1) Load ciphertext
with open("output.txt") as f:
    ctxt_orig = unhexlify(f.read().strip())

# 2) The ten strings used in *forward* order
random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]
N = len(random_strs)

flag_format = b"picoCTF{"
printable = set(bytes(string.printable, "ascii"))

def looks_like_flag(b):
    """Simple sanity check: starts with picoCTF{ and all chars printable."""
    return b.startswith(flag_format) and all(c in printable for c in b)

# 3) Brute even/odd parity for each layer (reverse order!)
for mask in range(1 << N):           # 0 … 1023
    ctxt = ctxt_orig
    for idx, s in enumerate(reversed(random_strs)):
        if (mask >> idx) & 1:        # undo this layer once (odd parity)
            ctxt = xor(ctxt, s)

    # 4) Try key lengths 1–32
    for klen in range(1, 33):
        key_guess = xor(ctxt[:len(flag_format)], flag_format)[:klen]
        # repeat key to full length
        full_key = (key_guess * (len(ctxt) // klen + 1))[:len(ctxt)]
        candidate = xor(ctxt, full_key)

        if looks_like_flag(candidate):
            print("✓ Found!", candidate.decode())
            raise SystemExit

print("No luck – try bumping key length or checks.")
---------------------------------------------------------------------------
This script decrypts a flag that was obfuscated using multiple XOR layers. The original encryption applied
a repeating-key XOR followed by ten known strings XORed an unknown number of times. Since XORing with
the same string an even number of times cancels itself out, the script brute-forces all 2¹⁰ (1024) possible
combinations of odd/even applications of the 10 strings, reversing them in the correct order. For each
combination, it then tries to recover the original key using the known picoCTF{ prefix, and attempts to
decrypt the full flag. When the output looks like a valid flag, it is printed and the program exits.

and so we got:
<img width="371" height="106" alt="Screenshot 2025-07-10 164631" src="https://github.com/user-attachments/assets/4d296133-7db3-43b2-9bec-d36c5a4537c5" />

The Flag is : picoCTF{w41t_s0_1_d1dnt_1nv3nt_x0r???}




