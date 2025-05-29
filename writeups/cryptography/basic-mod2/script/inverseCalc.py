#!/usr/bin/env python3

# 1–26 → a–z
# 27–36 → 0–9  (27→0, 28→1, …, 36→9)
# 37 → '_'
charset = {}
for i in range(1, 27):
    charset[i] = chr(ord('a') + i - 1)
for i in range(27, 37):
    charset[i] = str(i - 27)
charset[37] = '_'

# Read numbers from the hard-coded file
with open("message.txt") as f:
    nums = [int(x) for x in f.read().split()]

# Build the decoded message
decoded = []
for n in nums:
    r = n % 41
    inv = pow(r, -1, 41)       # modular inverse of r mod 41
    decoded.append(charset[inv])

flag = "".join(decoded)
print(f"picoCTF{{{flag}}}")
