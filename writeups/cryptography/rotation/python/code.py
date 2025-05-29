def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

cipher_text = "xqkwKBN{z0bib1wv_l3kzgxb3l_429in00n}"

for s in range(1, 26):
    print(f"Shift {s}: {caesar_decrypt(cipher_text, s)}")