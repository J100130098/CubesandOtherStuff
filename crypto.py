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
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
def caesarEncrypt(plainText, shift):
    cipherText = ""
    for i in plainText:
        index = alphabet.find(i)
        nextIndex = (index + shift) % 53
        cipherText += alphabet[nextIndex]
    return cipherText
print(caesarEncrypt("Stonks Are cool", 3))
# write a caesarDecrypt(cipherText, shift)
def caesarDecrypt(cipherText, shift):
    word = ""
    for i in cipherText:
        index = alphabet.find(i)
        nextIndex = (index - shift);
        if nextIndex < 0:
            nextIndex = 53 + nextIndex
        word += alphabet[nextIndex]
    return word

print(caesarDecrypt("VWRQNVcDuhcfrro", 3))
