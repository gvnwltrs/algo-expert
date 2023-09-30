
# Given a non-empty string that consists of lowercase English letters and a non-negative integer key, I am asked to write a function that is going to shift each letter in the given string key positions in the alphabet and return the new string.

def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    len_of_alphabet = len(alphabet)
    new_string = ""

    for e in string:
        idx = alphabet.index(e)
        pos = string.index(e)
        new_string += alphabet[(idx + key) % len_of_alphabet]

    return new_string