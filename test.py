#!/usr/bin/env python3

def reverse_list(list):
    i = 0
    j = len(list) - 1

    while i < j: 
        list[i], list[j] = list[j], list[i]
        i += 1
        j -= 1
    
    return list

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(reverse_list(my_list))
      
