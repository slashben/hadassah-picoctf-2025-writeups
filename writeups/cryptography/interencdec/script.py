import base64
encoded = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg=="
decoded = base64.b64decode(encoded)
print(decoded)
#b"b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='\n"
decoded1=decoded
print(decoded1)
stripped=decoded1.decode().strip("'").strip()
print(stripped)
stripped=stripped.strip("b'")
print(stripped)
decoded2=base64.b64decode(stripped)
print(decoded2)
encrypted_ceacer = decoded2.decode()

def caesar_decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


print(caesar_decrypt(encrypted_ceacer, 7))
