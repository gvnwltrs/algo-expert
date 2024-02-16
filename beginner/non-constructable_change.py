#!/usr/bin/env python3 

# We are given an array of positive integers, which represent the values of coins that we have in our possession. The array could have duplicates. We are asked to write a function that returns the minimum amount of change that we cannot create with our coins. For instance, if the input array is [1, 2, 5], the minimum amount of change that we cannot create is 4, since we can create 1, 2, 3 (1 + 2) and 5.

def nonConstructibleChange(coins):
    coins.sort()

    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            break
        minimum_change += coin 
  
    return minimum_change + 1 

# Time complexity: O(nlogn) | space complexity: O(1)

'''
The time complexity of the solution is O(nlogn), where n is the number of coins in the input array. This is because we are sorting the array of coins. The space complexity of the solution is O(1), since we are using only a constant amount of space. 
The coins algoritm works by finding the gap in the sequence of sorted coins. How? By iterating through the coins and checking if the current coin is greater than the minimum change plus 1. If it is, we break the loop and return the minimum change plus 1. If it is not, we add the current coin to the minimum change.
To put it another way, if the current coin we've selected is greater than the minimum change plus 1, we know that we've skipped over the next coin in the sequence because if we didn't the coin we currently have would not have exceeded the minimum change plus 1, thus we know there is a gap and we also know that the gap means that this is the minimum change that cannot be made.  
'''