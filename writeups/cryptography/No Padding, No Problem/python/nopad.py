import socket
import re

HOST = "mercury.picoctf.net"
PORT = 2671


def get_rsa_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.recv(4096)  # Welcome message
    s.sendall(b"\n")  # Trigger n, e, ciphertext
    data = s.recv(4096).decode()

    n = int(re.search(r"n:\s*(\d+)", data).group(1))
    e = int(re.search(r"e:\s*(\d+)", data).group(1))
    c0 = int(re.search(r"ciphertext:\s*(\d+)", data).group(1))

    return n, e, c0, s


def cca_oracle(s, c0, e, n, conn):
    s_pow_e = pow(s, e, n)
    c_tag = (c0 * s_pow_e) % n
    conn.recv(4096)  # Prompt: Give me ciphertext to decrypt
    conn.sendall((str(c_tag) + "\n").encode())
    response = conn.recv(4096).decode()

    # Parse the decrypted m * s
    match = re.search(r"(\d+)", response)
    if not match:
        raise Exception("Failed to decrypt modified ciphertext")

    decrypted = int(match.group(1))
    m = decrypted // s  # We divided back by s
    return m


# Execute attack
n, e, c0, conn = get_rsa_data()
s = 2
m = cca_oracle(s, c0, e, n, conn)
print("\n[+] Decrypted flag as int:", m)

# Convert int to bytes
flag = m.to_bytes((m.bit_length() + 7) // 8, byteorder="big")
print("[+] Flag:", flag.decode(errors="ignore"))
