def dec_txt(encrypted_txt, move):
    result = ""
    for char in encrypted_txt:
        if char.isalpha():
            char = char.upper()
            c = ord(char) - ord('A')
            shifted = (c - move) % 26
            decrypted_char = chr(shifted + ord('A'))
            result += decrypted_char
        else:
            result += char
    return result

if __name__ == '__main__':
        encrypted_txt = "xqkwKBN{z0bib1wv_l3kzgxb3l_555957n3}"
        for i in range(0,26):
            move = i
            decrypted_txt = dec_txt(encrypted_txt, move)
            print(f'{i}. {decrypted_txt}')
