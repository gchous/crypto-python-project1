import string
import random

# Create the given table (page 20)
table = list(string.ascii_uppercase)
table.append(".")
table.append("!")
table.append("?")
table.append("(")
table.append(")")
table.append("-")
print("The given table is: \n" ,table)
print("\n")

# Find index of each letter based on the given table
def findIndex(letter, length):
    i = 0
    index = -1
    while index < 0 and i < length:
        if letter == table[i]:
            index = i
        i = i + 1
    return index

# Generate key function. Contains the random integers representing
# characters in the ASCII range for uppercase letters
def generateKey(length):
    key = []
    for i in range(length):
        key.append(random.randint(65, 90))
    return key

# Function for OTP encryption. Inputs key & original message
# Encrypt the message and returns binary values result based
# on each character of table index xor with each key index
def OTPencryption(key, message):
    length = len(message)
    encrypted = []
    for i in range(length):
        m = findIndex(message[i], length)
        #print(message[i], "is number:", m);
        encrypted.append(bin(m ^ key[i]))
    return encrypted

# Function for OTP decryption. Inputs key & encrypted message at binary value.
# It performs the decryption with the same logic by performing the same xor of
# each key index with each encrypted index value of ASCII table.
# Convert it into integer and use it as index on initial table to go back
# to the original letter.
def OTPdecryption(key, encryptedMessage):
    length = len(encryptedMessage)
    decrypted = []
    for i in range(length):
        c = int(encryptedMessage[i], 2)
        decrypted.append(bin(key[i] ^ c))
    for i in range(length):
        decryptedLetter = int(decrypted[i], 2)
        decrypted[i] = table[decryptedLetter]
    return decrypted

# Define original message
message = "WE.ALL.SHOULD.BE.PROUD.FOR.OURSELVES!!!"
print("Message is :", message)

messageLength = len(message)

key = generateKey(messageLength)
#print("Key:", key)

# Call OTPencryption
encrypted = OTPencryption(key, message)
#print (encrypted)

# Convert from binary values after xor result of function OTPencryption,
# to its respective character into ASCII table so as to have final
# encrypted ciphertext format
finalEncrypted = []
for i in range(len(encrypted)):
    finalEncrypted.append(chr(int(encrypted[i], 2)))

# Print encrypted message
print("Encrypted C:", "".join(finalEncrypted))

# Call OTPdecryption
decrypted = OTPdecryption(key, encrypted)
decrypted = "".join(decrypted)

# Print decrypted message
print("Decrypted M:", decrypted)
