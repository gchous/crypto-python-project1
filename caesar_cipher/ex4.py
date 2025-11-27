import random

# Define the original message
originalMessage="HELLOMYNAMEISGEORGEANDIAMTRYINGMYLUCKINCRYPTOGRAPHY"
print('Original message:', originalMessage)

# Convert the message in a list of numbers, based on the ASCII code
originalMessageAscii=[ord(x)-65 for x in originalMessage]
#print (originalMessageAscii)

# Function to get the ASCII value of each string in the message list
def str2lst(s):
    return [ord(x)-65 for x in s]

# Function to get the string value of each ASCII value in the encrypted text
def lst2str(lst):
    return [ ''.join([chr(x+65) for x in lst])]

# Encryption process - Ceasar's cipher
def shiftCipherEnc(originalMessage,k):
    # Convert the plaintext string into a list of integers
    originalMessageAscii = str2lst(originalMessage)
     # Shift each letter in the plaintext by the key number of positions
    encryptedMessageAscii = [(x+k)%26 for x in originalMessageAscii]
    # Convert the shifted list of integers back into a string
    return lst2str(encryptedMessageAscii)

# Decryption process - Ceasar's cipher
def shiftCipherDec(encryptedMessage,k):
    # Convert the input ciphertext to a list of ASCII values
    encryptedMessageAscii = str2lst(encryptedMessage[0])
    # Calculate the ASCII value of each character in the encrypted message, shifted by k
    decryptedMessageAscii = [(x-k)%26 for x in encryptedMessageAscii]
    # Convert the list of ASCII values back to a string and return it
    return lst2str(decryptedMessageAscii)

# Function to get a random key for encryption process
def generateKey():
    return random.randint(1, 25)

# Define the key to be used in the encryption process
key = generateKey()
print(f"Generated key: {key}")

# Call Ceasar's Cipher for message, given a random key
encryptedMessage = shiftCipherEnc(originalMessage,key)
print("Encrypted message:", encryptedMessage)

# Using a brute-force method, try to parse all possible keys and decrypt the message
for i in range(26):
    decryptedMessage=shiftCipherDec(encryptedMessage,i)
    print (i, decryptedMessage)
    if decryptedMessage[0]==originalMessage:
        print(' -------- Original message found! (Position:', key,') --------')
        #print('The original message is:', decryptedMessage)
        #break
