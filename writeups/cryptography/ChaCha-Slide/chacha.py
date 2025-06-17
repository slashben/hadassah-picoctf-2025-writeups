import binascii

def debug_server_response():
    """
    Debug why the server might not be responding
    """
    print("ChaCha Slide Challenge - Server Response Debug")
    print("=" * 60)
    print()
    print("Theory: Our attack works, but we're not getting the server response.")
    print("Let's test multiple scenarios and provide debugging info.")
    print()
    
    # Get the ciphertext
    while True:
        print("Paste the first ciphertext from your netcat session:")
        cipher_input = input("Ciphertext: ").strip()
        
        if not cipher_input:
            continue
            
        cipher_hex = ''.join(cipher_input.split())
        
        try:
            cipher_bytes = binascii.unhexlify(cipher_hex)
            break
        except ValueError:
            print("❌ Invalid hex string.")
    
    # Parse structure
    cipher_body = cipher_bytes[:-28]
    tag_bytes = cipher_bytes[-28:-12]
    nonce_bytes = cipher_bytes[-12:]
    
    # Extract keystream
    known_text = "Did you know that ChaCha20-Poly1305 is an authenticated encryption algorithm?"
    known_bytes = known_text.encode()
    keystream = bytes(c ^ p for c, p in zip(cipher_body, known_bytes))
    
    # Target message
    target_text = "But it's only secure if used correctly!"
    target_bytes = target_text.encode()
    
    print(f"--- Analysis ---")
    print(f"Known text length: {len(known_bytes)} bytes")
    print(f"Target text length: {len(target_bytes)} bytes")
    print(f"Cipher body length: {len(cipher_body)} bytes")
    
    # Generate different variants to test server behavior
    variants = []
    
    # Variant 1: Exact length (what we've been trying)
    target_keystream = keystream[:len(target_bytes)]
    forged_cipher1 = bytes(t ^ k for t, k in zip(target_bytes, target_keystream))
    forged_msg1 = forged_cipher1 + tag_bytes + nonce_bytes
    variants.append(("Exact target length", forged_msg1))
    
    # Variant 2: Padded with nulls to original length
    padded_target = target_bytes + b'\x00' * (len(known_bytes) - len(target_bytes))
    forged_cipher2 = bytes(t ^ k for t, k in zip(padded_target, keystream))
    forged_msg2 = forged_cipher2 + tag_bytes + nonce_bytes
    variants.append(("Padded to original length", forged_msg2))
    
    # Variant 3: Test with a simpler message that definitely contains our target
    simple_target = target_text.encode() + b' (test message)'
    if len(simple_target) <= len(keystream):
        simple_keystream = keystream[:len(simple_target)]
        forged_cipher3 = bytes(t ^ k for t, k in zip(simple_target, simple_keystream))
        forged_msg3 = forged_cipher3 + tag_bytes + nonce_bytes
        variants.append(("Extended target message", forged_msg3))
    
    # Variant 4: Known working message (should decrypt to original)
    original_msg = cipher_bytes  # This should definitely work
    variants.append(("Original message (control test)", original_msg))
    
    print(f"\n--- Generated {len(variants)} Test Messages ---")
    
    for i, (name, msg) in enumerate(variants, 1):
        hex_msg = binascii.hexlify(msg).decode()
        
        # Local test
        msg_cipher = msg[:-28]
        test_keystream = keystream[:len(msg_cipher)]
        if len(msg_cipher) <= len(keystream):
            test_decrypt = bytes(c ^ k for c, k in zip(msg_cipher, test_keystream))
            test_text = test_decrypt.decode('utf-8', errors='ignore')
            contains_target = target_text in test_text
        else:
            test_text = "[Message too long for available keystream]"
            contains_target = False
        
        print(f"\n{i}. {name}")
        print(f"   Length: {len(msg)} bytes")
        print(f"   Local decrypt: '{test_text[:60]}{'...' if len(test_text) > 60 else ''}'")
        print(f"   Contains target: {contains_target}")
        print(f"   Hex: {hex_msg}")
        
        if name == "Original message (control test)":
            print(f"   ⚠️  This should decrypt to the original known text")
        elif contains_target:
            print(f"   ✅ This should trigger the flag if server processes it")
    
    print(f"\n--- Debugging Steps ---")
    print(f"1. Try message #4 first (original) - server should respond with original text")
    print(f"2. If #4 works, try #2 (padded) - most likely to work")
    print(f"3. If #2 works, try #1 (exact) - our preferred attack")
    print(f"4. If none work, there may be a network/server issue")
    print()
    print(f"Expected server responses:")
    print(f"- Original message: Should show original known text")
    print(f"- Successful attack: Should show flag or target text")
    print(f"- Failed attack: Might show error or nothing")
    print()
    
    # Additional debugging info
    print(f"--- Additional Debug Info ---")
    print(f"Challenge expects to find: '{target_text}'")
    print(f"Server checks: if goal in repr(user_message)")
    print(f"Where goal = 'But it's only secure if used correctly!'")
    print()
    print(f"If attacks #1-3 contain target but don't work, possible issues:")
    print(f"- Server not sending response (network issue)")
    print(f"- Additional server-side validation beyond Poly1305")
    print(f"- Different message format expected")
    print(f"- Server requires specific timing or session state")
    
    print(f"\n--- Netcat Testing Commands ---")
    print(f"Copy each hex string above and test in netcat:")
    print(f"nc activist-birds.picoctf.net 59470")
    print(f"(wait for prompt, then paste hex and press Enter)")

if __name__ == "__main__":
    debug_server_response()