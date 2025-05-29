lookup_in = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup_out = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

with open("ciphertext", "r") as f:
    ciphertext = f.read()

plaintext = ""
prev = 0

for char in ciphertext:
    if char not in lookup_out:
        continue  # skip invalid characters
    cur = lookup_out.index(char)
    index = (cur + prev) % 40
    plaintext += lookup_in[index]
    prev = index

print(plaintext)
