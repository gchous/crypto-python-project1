## Description

Implement the **One-Time Pad (OTP)** after first converting your message into bits using the table provided below.  
Both **encryption** and **decryption** must work correctly.

The plaintext message is given normally as text and is internally converted into 5-bit binary values.  
The key is randomly chosen and has the **same length** (in bits) as the message.

The result of the encryption must **not** be displayed in bits, but instead converted back into **Latin characters** using the same table.

Below is the encoding table:

| | |
|------|------|
| (0) A : 00000 | (13) N : 01101 |
| (1) B : 00001 | (14) O : 01110 |
| (2) C : 00010 | (15) P : 01111 |
| (3) D : 00011 | (16) Q : 10000 |
| (4) E : 00100 | (17) R : 10001 |
| (5) F : 00101 | (18) S : 10010 |
| (6) G : 00110 | (19) T : 10011 |
| (7) H : 00111 | (20) U : 10100 |
| (8) I : 01000 | (21) V : 10101 |
| (9) J : 01001 | (22) W : 10110 |
| (10) K : 01010 | (23) X : 10111 |
| (11) L : 01011 | (24) Y : 11000 |
| (12) M : 01100 | (25) Z : 11001 |
| | |
| (26) . : 11010 | (27) ! : 11011 |
| (28) ? : 11100 | (29) ( : 11101 |
| (30) ) : 11110 | (31) - : 11111 |

**Table: 5-bit Encoding Scheme**

### Goal

- Convert each character to a 5-bit binary value.
- Generate a random OTP key of equal length.
- Encrypt using XOR:  

  $$
  C = M \oplus K
  $$
  
- Decrypt using XOR:  

  $$
  M = C \oplus K
  $$

- Convert the final result back to text using the same table.
