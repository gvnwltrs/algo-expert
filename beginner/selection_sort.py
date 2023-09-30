
# Given an array of integers, we are asked to sort the array in ascending order with the Selection Sort.



def selectionSort(array):
    for i in range(len(array) -1):
        select = array[i]
        select_idx = 0
        for j in range(i+1, len(array)):
            if array[j] < select:
                select = array[j]
                select_idx = j
        
        if select < array[i]:
            temp = array[i]
            array[i] = array[select_idx]
            array[select_idx] = temp

    return array
        