def binarySearch(array, target):
    
    left = 0 
    middle = len(array) // 2
    right = len(array)
    buffer_length = right - left 
    while buffer_length > 1:
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            right = middle
            buffer_length = right - left 
            middle = middle - (buffer_length // 2)
        elif array[middle] < target:
            left = middle
            buffer_length = right - left 
            middle = middle + (buffer_length // 2)

    return array[0] if buffer_length == 1 and array[0] == target else -1 