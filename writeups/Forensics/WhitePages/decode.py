import sys
import os
from collections import Counter
import binascii # Added import as it was missing in the user's provided snippet, but used in the original.

def decode_invisible_chars(file_path):
    """
    Reads a file in binary mode, displays its raw byte and hexadecimal representations.

    Args:
        file_path (str): The path to the file to be analyzed.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return

    if not os.path.isfile(file_path):
        print(f"Error: Path '{file_path}' is not a file.")
        return

    print(f"--- Analyzing File: '{file_path}' ---")

    try:
        with open(file_path, 'rb') as f:
            raw_bytes = f.read()

        file_size = len(raw_bytes)
        print(f"\nFile Size: {file_size} bytes")

        if file_size == 0:
            print("File is empty. Nothing to analyze.")
            return

        # 1. Raw Bytes Representation
        print("\n--- 1. Raw Bytes (repr()) ---")
        # repr() shows escape sequences for non-printable characters (e.g., \x00, \n)
        print(repr(raw_bytes))

        # 2. Hexadecimal Representation
        print("\n--- 2. Hexadecimal Representation ---")
        # binascii.hexlify returns bytes, decode to string for printing
        hex_data = binascii.hexlify(raw_bytes).decode('ascii')
        # Print in chunks for readability
        print('\n'.join(hex_data[i:i+64] for i in range(0, len(hex_data), 64)))

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
            
# --- How to use the script ---
if __name__ == "__main__":
    file_to_analyze = "WhitePages.txt"
    decode_invisible_chars(file_to_analyze)