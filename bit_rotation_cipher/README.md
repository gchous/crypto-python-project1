## Description

Let \( m \) be a 16-bit message.  
We consider circular left rotation \( \ll a \) by \( a \) bits.  

Suppose that \( m \) is encoded into \( c \) according to the formula:

\[
c = m \oplus (m \ll 6) \oplus (m \ll 10)
\]

Your tasks are:

**Decoding formula is**:
$$ m = c⊕(c≪2)⊕(c≪4)⊕(c≪12)⊕(c≪14)$$

**Implement appropriate code** (see ex3.py) to verify that the decoding formula you derive is correct.
