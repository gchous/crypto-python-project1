## Description

Let $m$ be a 16-bit message.  
We consider circular left rotation by $a$ bits.

Suppose that $m$ is encoded into $c$ according to the formula:

$$
c = m \oplus (m \ll 6) \oplus (m \ll 10)
$$

Your tasks are:

**Decoding formula:**  
$$
m = c \oplus (c \ll 2) \oplus (c \ll 4) \oplus (c \ll 12) \oplus (c \ll 14)
$$

Implement appropriate code (see `ex3.py`) to verify that the decoding formula you derive is correct.
