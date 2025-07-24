# WhitePages Challenge Writeup

## Overview
This is a steganography challenge involving hidden data in what appears to be an empty text file. The challenge demonstrates how invisible Unicode characters can be used to hide binary data in plain sight.

## Challenge Description
- **Challenge Name**: WhitePages
- **Author**: John Hammond

## Initial Analysis
The challenge provides a text file that appears empty when viewed normally, but contains **1377 characters** when inspected. This immediately suggests the presence of invisible or whitespace characters.

## Solution Process

### Step 1: Hexadecimal Analysis
Using a decode script to examine the file's hexadecimal representation reveals a pattern:

```
e28083e28083e28083e2808320e2808320e28083e28083e28083e28083e28083
20e28083e2808320e28083e28083e28083e2808320e28083e2808320e2808320
2020e28083e28083e28083e28083e280832020e2808320e28083e2808320e280
...
```

**Key Observations:**
- Repetitive pattern of `e28083` and `20` in hexadecimal
- `20` represents a regular space character
- `e28083` represents a Unicode thin space character (U+2003)

### Step 2: Binary Conversion Strategy
The solution involves treating the two different space characters as binary digits:

1. **Regular space (0x20)** → Binary `0`
2. **Thin space (0xe28083)** → Binary `1`

### Step 3: Manual Replacement Method
Using a text editor (the document shows this process):

1. Select the first character (thin space) and use Find & Replace to replace all instances with `0`
2. Select the remaining invisible character (regular space) and replace all instances with `1`
3. This creates a binary string that can be converted to ASCII

### Step 4: Binary to ASCII Conversion
Converting the resulting binary string reveals:

```
picoCTF

SEE PUBLIC RECORDS & BACKGROUND REPORT

5000 Forbes Ave, Pittsburgh, PA 15213

picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}
```

## Files
- Original challenge file (appears empty but contains 1377 characters)
- `decode.py` - Script for hexadecimal analysis

## Flag
```
picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}
```