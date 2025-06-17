# NSA Backdoor Challenge

**Author:** Joshua Inscoe  
**Challenge Description:** "I heard someone has been sneakily installing backdoors in open-source implementations of Diffie-Hellman... I wonder who it could be... ;)"

## Challenge Overview

This challenge provides two files:

- `gen.py`: Script that generates a modulo `n` and encrypted message `c`, where the original secret (flag) is encoded as a hexadecimal integer. Contains a function that constructs "smooth" primes where `(p-1)` has only small prime factors.
- `output.txt`: Contains the public values `n` and `c` from `gen.py`

**Goal:** Recover the secret flag from the given public parameters.

## Vulnerability Analysis

The hint about backdoors in Diffie-Hellman implementations, combined with the use of "smooth primes" (where `p-1` and `q-1` have only small prime factors), points to a specific vulnerability: the **Pohlig-Hellman algorithm**.

### Why Brute Force Fails

An initial approach might be to brute-force the exponent `x` such that `g^x = c (mod n)`. However, this is extremely inefficient due to the large search space (up to 2^24 and beyond).

### The Pohlig-Hellman Attack

Pohlig-Hellman is an algorithm for solving discrete logarithm problems that becomes particularly efficient when the order of the group (in this case, `φ(n) = (p-1)(q-1)` for `Z*n`) has only small prime factors. The algorithm:

1. Breaks the problem into smaller discrete logarithm problems modulo each prime factor
2. Combines results using the Chinese Remainder Theorem (CRT)

## Solution Approach

### Step 1: Factor n into p and q

Since `n` is a product of two smooth primes, we use **Pollard's p-1 method** for efficient factorization.

### Step 2: Divide into Subproblems

The discrete logarithm problem `g^x = c (mod n)` is divided into:

- `g^x = c (mod p)`
- `g^x = c (mod q)`

### Step 3: Apply Pohlig-Hellman

Each subproblem is further broken down using Pohlig-Hellman, targeting `x` modulo the prime factors of `(p-1)/2` and `(q-1)/2` (since `g=3` implies the relevant subgroup order).

### Step 4: Solve Sub-Discrete Logarithms

Use a variant of Pohlig-Hellman (`naive_pohlig_hellman`) with brute force (`dlog_brute`) for very small discrete log problems.

### Step 5: Combine with CRT

- Combine partial solutions using CRT to find full solutions for `x mod (p-1)` and `x mod (q-1)`
- Since there are two possibilities for `x mod 2` for each prime, we get four possible combinations

### Step 6: Final Solution

Use CRT again to combine the four possible pairs of solutions to find the final `x mod n`. Only one will satisfy the original equation `g^x = c (mod n)`.

### Step 7: Decode Flag

Convert the resulting integer `x` from hexadecimal back to the flag string.

## Implementation

### Dependencies

```bash
pip install gmpy2 primefac
```

### Usage

1. Save the solution script as `solve_backdoor.py`
2. Create `output.txt` in the same directory with the challenge values:
   ```
   n = 0x[hex_value]
   c = 0x[hex_value]
   ```
3. Run the script:
   ```bash
   python soluiton.py
   ```

### Key Functions

- **`dlog_brute()`**: Solves discrete logarithm by brute force for small subgroups
- **`naive_pohlig_hellman()`**: Implements simplified Pohlig-Hellman algorithm
- **`chinese_remainder()`**: Solves systems of congruences using CRT
- **`extended_gcd()` & `mod_inverse()`**: Helper functions for modular arithmetic

## Algorithm Flow

```
1. Read n, c from output.txt
2. Factor n = p × q using Pollard's p-1
3. For each prime (p, q):
   a. Calculate c_p = c mod p, c_q = c mod q
   b. Find prime factors of (p-1)/2 and (q-1)/2
   c. Apply Pohlig-Hellman to solve g^x = c_i (mod prime_i)
   d. Use CRT to combine partial solutions
4. Try all 4 combinations of (solution mod p, solution mod q)
5. Verify which combination satisfies g^x = c (mod n)
6. Convert solution to hex and decode as ASCII flag
```

## Key Insights

- **Smooth primes** make factorization easier via Pollard's p-1 method
- When group orders have only small prime factors, **Pohlig-Hellman** becomes highly effective
- This demonstrates why proper parameter generation is crucial in cryptographic implementations

## Final Result

The script successfully recovers the flag:

```
picoCTF{b3w4r3_0f_c0mp0s1t3_m0dul1_e032a664}
```
