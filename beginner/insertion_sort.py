
# Given an array of integers, we are asked to sort the input array using the Insertion Sort and return the sorted array.

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp 
            j -= 1
    
    return array