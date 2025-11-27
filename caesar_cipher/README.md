## Description

This exercise implements and analyzes the **Caesar cipher**, one of the simplest classical substitution ciphers.

### What the code does

- Converts a plaintext message into numerical form (A = 0, B = 1, …, Z = 25).
- Encrypts the message using the Caesar cipher:

  $$
  C = (P + k) \bmod 26
  $$
  
  where \( k \) is a randomly generated key.

- Decrypts messages using the inverse operation:

  $$
  P = (C - k) \bmod 26
  $$
  
- Performs **brute-force cryptanalysis** by trying all 26 possible keys.
- Identifies which key produces the correct plaintext and prints the recovered message.

### Goal of the exercise

- Understand how Caesar cipher encryption and decryption work.
- Implement helper functions for converting between text and numeric values.
- Apply brute-force search to break the cipher and recover the original message.

- Observe why the Caesar cipher is insecure due to its very small keyspace.


