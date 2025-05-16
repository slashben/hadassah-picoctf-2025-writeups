def dec(word, shift):
    decryption = ''
    for letter in word:
        if 'a' <= letter <= 'z':
            shifted = chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
            decryption += shifted
        else:
            decryption += letter
    print(f"{shift}: {decryption}")


for i in range(0, 27):
    dec("picoCTF{dspttjohuifsvcjdpoabrkttds}", i)
