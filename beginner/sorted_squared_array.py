#!/usr/bin/env python3 

def sortedSquaredArray(array):
    new_array = [i ** 2 for i in array]

    new_array.sort()
    
    return new_array
