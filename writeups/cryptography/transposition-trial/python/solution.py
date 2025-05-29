def descramble_message(scrambled_text):
    # Scrambling pattern: 'The' → 'heT' ⇒ indices [1, 2, 0]
    # We need to reverse it: from 'heT' get back 'The' ⇒ original[0] = scrambled[2], etc.
    unscramble_order = [2, 0, 1]

    # Break text into 3-character blocks
    blocks = [scrambled_text[i:i+3] for i in range(0, len(scrambled_text), 3)]

    # Unscramble each block
    descrambled = []
    for block in blocks:
        if len(block) == 3:
            # Reorder characters according to unscramble_order
            descrambled_block = ''.join(block[i] for i in unscramble_order)
        else:
            # If block isn't 3 characters (e.g., last few chars), keep as is
            descrambled_block = block
        descrambled.append(descrambled_block)

    # Join the blocks back into a single string
    return ''.join(descrambled)


# Example usage
scrambled_text = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"
original_message = descramble_message(scrambled_text)
print("Recovered message:", original_message)
