#import re
import numpy as np

def rotateLeft(input, position):
    # Performs a left rotation by the specified amount
    return np.roll(input, position)

def encryptMessage(message):
    # Convert the message to a 16-bit binary string
    messageBinary = np.binary_repr(message, width=16)

    # Convert the binary string to a NumPy array of integers
    messageArray = np.array(list(messageBinary), dtype=int)

    # Print original message state
    print('Original Message:   ', messageArray)

    # Perform left rotations
    rotatedSix = rotateLeft(messageArray, -6)
    print('Left rotation by 6: ', rotatedSix)
    rotatedTen = rotateLeft(messageArray, -10)
    print('Left rotation by 10:', rotatedTen)

    # Perform XOR operations
    encryptedArray = messageArray ^ rotatedSix ^ rotatedTen

    # Convert the encrypted array back to a binary string
    encryptedBinary = ''.join(map(str, encryptedArray))

    return encryptedBinary

def decryptMessage(encrypted):
    # Convert the encrypted message to a NumPy array of integers
    encryptedArray = np.array(list(encrypted), dtype=int)
    print('Encrypted message:  ', encryptedArray)

    # Perform left rotations(using minus prosimo)
    rotatedTwo = rotateLeft(encryptedArray, -2)
    print('Left rotation by 2: ', rotatedTwo)
    rotatedFour = rotateLeft(encryptedArray, -4)
    print('Left rotation by 4: ', rotatedFour)
    rotatedTwelve = rotateLeft(encryptedArray, -12)
    print('Left rotation by 12:', rotatedTwelve)
    rotatedFourteen = rotateLeft(encryptedArray, -14)
    print('Left rotation by 14:', rotatedFourteen)

    # Perform XOR operations
    decryptedArray = encryptedArray ^ rotatedTwo ^ rotatedFour ^ rotatedTwelve ^ rotatedFourteen

    # Convert the decrypted array back to a binary string
    decryptedBinary = ''.join(map(str, decryptedArray))

    return decryptedBinary

# Take a 16-bit number as input
inputMessage = "0100110101000001"
print('Enter a 16-bit message:', inputMessage)

# Convert the user input to an integer
originalMessage = int(inputMessage, 2)

# Encrypt the message
encryptedMessage = encryptMessage(originalMessage)
print()
print('Encrypted message:', encryptedMessage)

# Decrypt the message
decryptedMessage = decryptMessage(encryptedMessage)
print('Decrypted message:', decryptedMessage)
