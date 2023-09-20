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
        