
encryption = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}"
KEY = "CYLAB"


def vigenere_decrypt(message, key):
    output = ""
    counter = 0
    for letter in message:
        if not letter.isalpha():
            output += letter
            continue

        letter_char = ord(letter.lower()) - ord('a')
        key_char = ord(key[counter].lower()) - ord('a')
        output += chr(((letter_char - key_char) % 26) + ord('a'))

        counter += 1
        counter %= len(key)

    return output


if __name__ == '__main__':
    print(vigenere_decrypt(encryption, KEY))
