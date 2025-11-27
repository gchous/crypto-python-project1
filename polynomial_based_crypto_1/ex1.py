import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define f(x) and g(x)
g = x**2 + 3*x + 1
f = x**5 + 3*x**3 + 7*x**2 + 3*x**4 + 5*x + 4

# Find the roots of the polynomial g(x)
roots = sp.solve(g, x)

# Select one root (either roots[0] or roots[1])
x0 = roots[0]

# Simplify the polynomial f(x) with the selected root x0
encryptedPoly = sp.simplify(f.subs(x, x0))

# Define the encrypted message
encryptedMessage = "οκηθμφδζθγοθχυκχσφθμφμχγ"

# Decrypt the message
decryptedMessage = ""
for char in encryptedMessage:

    if char.isalpha():
        # Convert the letter to its corresponding numeric value
        numericValue = ord(char.lower()) - ord('α') + 1

        # Decrypt the numeric value
        decryptedValue = (numericValue - int(encryptedPoly)) % 24

        if decryptedValue==0:
            decryptedValue=25
            decryptedChar = chr(decryptedValue + ord('α') - 1)
            decryptedMessage += decryptedChar
        elif decryptedValue==18 or decryptedValue==16:
            decryptedChar = chr(decryptedValue + ord('α') - 2)
            decryptedMessage += decryptedChar
        else:
            decryptedChar = chr(decryptedValue + ord('α') - 1)
            decryptedMessage += decryptedChar

    else:
        # Keep non-alphabetic characters unchanged
        decryptedMessage += char

# Print the decrypted message
print (decryptedMessage)
