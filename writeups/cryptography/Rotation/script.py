encrypted = 'xqkwKBN{z0bib1wv_l3kzgxb3l_555957n3}'
def caesar_decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


print(caesar_decrypt(encrypted, 8))
