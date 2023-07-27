
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    len_of_alphabet = len(alphabet)
    new_string = ""

    for e in string:
        idx = alphabet.index(e)
        pos = string.index(e)
        new_string += alphabet[(idx + key) % len_of_alphabet]

    return new_string