#!/urs/bin/env python3

# We are given two arrays of integers array and sequence. We are asked to implement a function that is going to check whether all the numbers in the sequence appear in the array and they appear in the same order. In other words, the function needs to find out if we can get the sequence array from the array, when we delete some or no elements in the array without changing the order of the remaining elements.

# Example:

# array: [3, 1, 7, 5, 10, 2];
# sequence: [1, 5, 2];
# Output: true


def isValidSubsequence(array, sequence):
    # Write your code here.
    list_check = []
    last = None
    
    for i in range(len(array)):
        for j in range(len(sequence)):
            # last = sequence[i]
            if array[i] == sequence[j] and len(list_check) < len(sequence) and sequence[j] != last:
                list_check.append(sequence[j])
                last = sequence[j]
            else:
                last = None
                
    print('seqence: ', sequence, 'check: ',  list_check)
      
    if sequence == list_check:
        return True
    else:
        return False