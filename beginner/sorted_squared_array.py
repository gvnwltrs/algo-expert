#!/usr/bin/env python3 

# Given an array of integers that are sorted in increasing order, we are asked to write a function that squares all the integers in the array and returns them in a new array. The returned array must be sorted in increasing order as well.


def sortedSquaredArray(array):
    new_array = [i ** 2 for i in array]

    new_array.sort()
    
    return new_array
