# transposition cipher

# original This_is_a_secret_message_i_want_to_transmit_
# encrypted hsi_ertmsaera_att_rnmtti_sasce_esg_htiwn_otasi
def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText