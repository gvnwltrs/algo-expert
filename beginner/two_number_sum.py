#!/usr/bin/env python3

# Given an array of distinct integers and an integer representing the target sum, we are asked to implement a function that is going to find out whether there's a pair of numbers in the array that adds up to the target sum. If such pair exists, return the pair in any order; otherwise return an empty array. We cannot add a number to itself to get the target sum.


def twoNumberSum(array, targetSum):
    solution = []
    for el in range(len(array)-1):
        k = el+1
        for ch in range(k, len(array)):
            if array[el] + array[ch] == targetSum:
                solution.append(array[el])
                solution.append(array[ch])
                return solution
    return []