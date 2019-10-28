def letterToIndex(letter):
    from string import ascii_lowercase
    from string import ascii_uppercase
    alphabet = ascii_lowercase + ' ' + ascii_uppercase
    idx = alphabet.find(letter)
    if idx == -1:       #not found
        print("error:", letter, "is not in the alphabet")
    return idx

def indexToLetter(idx):
    from string import ascii_lowercase
    from string import ascii_uppercase
    alphabet = ascii_lowercase + ' ' + ascii_uppercase
    letter= ''
    if idx >= len(alphabet):
        print("error:", idx, "is too large")
    elif idx < 0:
        print("error:", idx, "is too small")
    else:
        letter = alphabet[idx]
    return letter
