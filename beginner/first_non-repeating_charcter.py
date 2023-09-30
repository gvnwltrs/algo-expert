#!/usr/bin/env python3



def firstNonRepeatingCharacter(string):
    if len(string) == 1:
        return 0
    elif len(string) == 0:
        return -1

    matched = set()
    last_idx = len(string)-1
    for i in range(len(string)-1):
        for j in range(i+1, len(string)):
            if string[i] == string[j] or string[i] in matched:
                matched.add(string[i])
                break
        if string[i] not in matched:
            return i 
        

    return -1 if string[last_idx] in matched else last_idx

