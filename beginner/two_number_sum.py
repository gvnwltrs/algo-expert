#!/usr/bin/env python3

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