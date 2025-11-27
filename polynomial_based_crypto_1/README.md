## Description

The following encrypted message has been received:

`κηθμρδξθγοθνχκχσφθμφχγ`

The encryption algorithm works as follows:

- Each letter of the original message is replaced with its corresponding numerical value  
  (α → 1, …, ω → 24).

Let \( x_0 \) be a root of the polynomial

\[
g(x) = x^2 + 3x + 1
\]

For each number of the message, the value of the polynomial

\[
f(x) = x^5 + 3x^3 + 7x^2 + 3x^4 + 5x + 4
\]

is added, evaluated at \( x = x_0 \).

Then each resulting number is converted back to its corresponding letter.

**Task:** Find the original (unencrypted) message.
