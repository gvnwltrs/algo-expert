#!/usr/bin/env python3 

def nonConstructibleChange(coins):
    coins.sort()

    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            break
        minimum_change += coin 
  
    return minimum_change + 1 