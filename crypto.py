# transposition cipher

# original This_is_a_secret_message_i_want_to_transmit_
# encrypted hsi_ertmsaera_att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

def encryptMessage():
    msg = input("Enter the message to encrypt: ")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is:", cipherText)

# write a stripSpaces(text) function
def stripSpaces(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText.replace(" ", "")

def stripSpaces(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText.replace(" ", "")

# write a caesarEncrypt(plainText, shift)
alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def caesarEncrypt(plainText, shift):
    cipherText = ""
    for i in plainText:
        # find each individual letter in the alphabet and convert it to a number value
        index = alphabet.find(i)
        # shift each letter corresponding to the shift, in this case three over
        nextIndex = (index + shift) % 53
        # convert the numbers back to letters
        cipherText += alphabet[nextIndex]
    return cipherText
print(caesarEncrypt("Stonks Are cool", 3))
# write a caesarDecrypt(cipherText, shift)
def caesarDecrypt(cipherText, shift):
    word = ""
    for i in cipherText:
        index = alphabet.find(i)
        # remove the shift made in the previous set of code
        nextIndex = (index - shift);
        # the if statement allows for spaces to be added back to the text
        if nextIndex < 0:
            nextIndex = 27 + nextIndex
        word += alphabet[nextIndex]
    return word

print(caesarDecrypt("VWRQNVcDuhcfrro", 3))
