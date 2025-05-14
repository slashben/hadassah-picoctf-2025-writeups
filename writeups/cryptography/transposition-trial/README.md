#  This is the write-up for the challenge "transposition-trial" in PicoCTF

# The challenge

## description
The link of the challenge: https://play.picoctf.org/practice/challenge/312?category=2&difficulty=2&page=1

Go into the link. You should see this page:
![challenge](./img/challenge1.png)

## How to solve it

Our data got corrupted during transmission. While nothing was replaced, every block of 3 characters got scrambled. The first word appears to be three letters long ("heT"), which likely should be "The".

### Understanding the Scrambling
From the example:
- Scrambled: "heT"
- Should be: "The"

This shows the scrambling pattern is `[1, 2, 0]` (original positions):
- Position 0 (T) moved to position 2
- Position 1 (h) moved to position 0
- Position 2 (e) moved to position 1

### Reversing the Scramble
To reverse, we use the pattern `[2, 0, 1]`:
- Take character from position 2 (T) and put it first
- Then position 0 (h)
- Then position 1 (e)

### Python Implementation
Here's the Python code that solves the challenge:

```python
def descramble_message(scrambled_text):
    unscramble_order = [2, 0, 1]
    blocks = [scrambled_text[i:i+3] for i in range(0, len(scrambled_text), 3)]
    
    descrambled = []
    for block in blocks:
        if len(block) == 3:
            descrambled_block = ''.join(block[i] for i in unscramble_order)
        else:
            descrambled_block = block
        descrambled.append(descrambled_block)
    
    return ''.join(descrambled)

scrambled_text = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4"
print(descramble_message(scrambled_text))
```

Running this code reveals the flag: `The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}`
