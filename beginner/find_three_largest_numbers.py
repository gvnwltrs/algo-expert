
# Given an array that contains at least three integers, we are asked to write a function that is going to find the three largest numbers in the input array and return them in an array sorted in ascending order. We are not allowed to sort the input array.

def findThreeLargestNumbers(array):
    top_three = [None] * 3
    for elem in array:
       if top_three[2] is None or elem > top_three[2]:
           shiftAndUpdate(top_three, elem, 2)
       elif top_three[1] is None or elem > top_three[1]:
           shiftAndUpdate(top_three, elem, 1)
       elif top_three[0] is None or elem > top_three[0]:
           shiftAndUpdate(top_three, elem, 0)      
    return top_three

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num # place highest value here
        else:
            array[i] = array[i + 1] # shift back 1 
