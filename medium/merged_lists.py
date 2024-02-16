#!/bin/bash/env python3

def merge_lists(lst1, lst2):
    
    left = 0
    right = 0
    idx = 0
    new_lst = [i for i in range(len(lst1) + len(lst2))]

    while left < len(lst1) and right < len(lst2):
        if lst1[left] < lst2[right]:
            new_lst[idx] = lst1[left]
            left += 1
            idx +=1
        else:
            new_lst[idx] = lst2[right]
            right += 1 
            idx += 1
    while left < len(lst1):
        new_lst[idx] = lst1[left]
        left += 1
        idx += 1
    while right < len(lst2):
        new_lst[idx] = lst2[right]
        right += 1
        idx += 1

    
    return new_lst

    # Time complexity: O(n) | Space complexity: O(n)

'''
Merge two sorted lists into one sorted list.
'''