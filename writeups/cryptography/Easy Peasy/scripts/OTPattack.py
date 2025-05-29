from pwn import remote

KEY_LEN = 50000

r = remote('mercury.picoctf.net', 36981)

# 1) grab the encrypted flag (use a byte‐string delimiter)
data = r.recvuntil(b"This is the encrypted flag!\n")
cipher_hex = r.recvline().strip().decode('ascii')
N = len(cipher_hex) // 2

# 2) wrap pointer back to 0
r.sendline(b"A" * (KEY_LEN - N))
r.recvuntil(b"Here ya go!\n")
r.recvline()   # discard the ciphertext

# 3) pull out keystream[0..N)
r.sendline(b"A" * N)
r.recvuntil(b"Here ya go!\n")
key_xor_hex = r.recvline().strip().decode('ascii')

# reconstruct key bytes
key = bytes(int(key_xor_hex[2*i:2*i+2], 16) ^ ord('A')for i in range(N))

# decrypt flag
flag = "".join(chr(int(cipher_hex[2*i:2*i+2], 16) ^ key[i])
    for i in range(N)
)

print(f"picoCTF{{{flag}}}")
