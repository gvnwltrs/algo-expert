
# We are asked to write a function that is going to determine whether or not a given string is a palindrome, in other words, whether the given string reads the same backward as forward. If a string has zero or one character, it is a palindrome. The input string contains at least one character.

def isPalindrome(string):
    reversed_string = reverse_string(string)
    return True if string == reversed_string else False

def reverse_string(string):
    new_string = ""
    i = len(string)-1
    
    while i >= 0:
        new_string += (string[i])
        i -=1

    return new_string
        