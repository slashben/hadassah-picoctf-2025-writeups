# Chronohack

## Category
Reverse Engineering

## Description
The script generates a random token based on current time (milliseconds). We reverse engineered it and reproduced the same token generation to guess the correct token and retrieve the flag.

## Vulnerability
The token is generated using random.seed(time.time() * 1000), so the token can be predicted based on current time.

## Solution
1. Analyze the provided `token_generator.py` script.
2. Note the seeding method based on current time.
3. Write a script to guess the token within ±5 seconds range.
4. Successfully retrieved the flag.

## Exploit

See [exploit.py](./exploit.py) for the full code.

## Flag
picoCTF{your_flag_here}


Add Chronohack solution by Mohamed
