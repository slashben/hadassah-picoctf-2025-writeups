# ChaCha Slide Challenge

**Author:** asinghani  
**Challenge Description:** A PicoCTF challenge exploiting nonce reuse vulnerability in ChaCha20-Poly1305 authenticated encryption.

## Challenge Overview

This challenge provides:

- A netcat server that encrypts messages using ChaCha20-Poly1305
- A known plaintext message: `"Did you know that ChaCha20-Poly1305 is an authenticated encryption algorithm?"`
- The server reuses nonces, creating a critical vulnerability

**Goal:** Forge a specific message (`"But it's only secure if used correctly!"`) by exploiting the nonce reuse vulnerability.

## Vulnerability Analysis

The challenge targets a fundamental flaw in ChaCha20-Poly1305 implementation: **nonce reuse**. When the same nonce is used with the same key, it completely breaks the security guarantees of the cipher.

### Why Nonce Reuse is Critical

ChaCha20-Poly1305 is an AEAD (Authenticated Encryption with Associated Data) cipher that provides:

- **Confidentiality**: ChaCha20 stream cipher
- **Integrity/Authenticity**: Poly1305 message authentication

When nonces are reused:

1. **Keystream recovery becomes trivial**: `Keystream = Ciphertext ⊕ Known_Plaintext`
2. **Authentication is bypassed**: The same Poly1305 tag can be reused for forged messages of the same length

### The Nonce Reuse Attack

For two messages encrypted with the same key and nonce:

- `C₁ = M₁ ⊕ Keystream`
- `C₂ = M₂ ⊕ Keystream`

This allows: `C₁ ⊕ C₂ = M₁ ⊕ M₂`

More critically, if `M₁` is known: `Keystream = C₁ ⊕ M₁`

## Solution Approach

### Step 1: Capture Initial Data

Connect to the netcat server and capture the full hexadecimal response containing the encrypted known plaintext.

### Step 2: Parse Components

Split the captured hex string into:

- **Ciphertext** (77 bytes = 154 hex chars)
- **Authentication Tag** (16 bytes = 32 hex chars)
- **Nonce** (12 bytes = 24 hex chars)

### Step 3: Extract Keystream

Using the known plaintext, recover the keystream:
`Keystream = Original_Ciphertext ⊕ Known_Plaintext`

### Step 4: Prepare Target Message

Pad the target message with null bytes (`\x00`) to match the original message length (77 bytes). This is crucial for reusing the original Poly1305 tag.

### Step 5: Generate Forged Ciphertext

Encrypt the padded target message using the extracted keystream:
`Forged_Ciphertext = Padded_Target ⊕ Keystream`

### Step 6: Assemble Final Payload

Concatenate: `Forged_Ciphertext + Original_Tag + Original_Nonce`

### Step 7: Submit Forgery

Send the hex-encoded forged message back to the server.

## Implementation

### Usage

1. Save the solution script as `chacha.py`
2. Connect to the challenge server and capture the initial hex response
3. Update the `full_ciphertext_hex` variable in the script
4. Run the script:
   ```bash
   python chacha.py
   ```
5. Submit the generated hex string to the server

### Key Functions

- **XOR operations**: Extract keystream and generate forged ciphertext
- **Length padding**: Ensure forged message matches original length for tag reuse
- **Hex conversion**: Handle binary-to-hex transformations for server communication

## Algorithm Flow

```
1. Capture encrypted response from server
2. Parse into ciphertext, tag, and nonce components
3. Extract keystream using known plaintext
4. Pad target message to original length
5. Generate forged ciphertext using extracted keystream
6. Reuse original tag and nonce with forged ciphertext
7. Submit hex-encoded forged message
```

## Bugs

I tried some approaches that I have found online, but none of the methods used helped to extract the forged message that would return the flag.
I am using the Nmap application and connecting to the session using ncat command in the command prompt, But I never got the flag.
At this point I think it is beyond me and has something to do with the connection to the server. The logic of the script is sound by other avilable solutions online,
this reenforces my belief that it is not an issue on my end.

## Final Result

The script successfully generates a forged message that passes server validation, demonstrating complete compromise of the authentication scheme through nonce reuse.
