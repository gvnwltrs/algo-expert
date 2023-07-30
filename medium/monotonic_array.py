
# s1
def isMonotonic(array):
    increasing = False
    decreasing = False 

    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            continue
        if array[i] > array[i-1] and not decreasing:
            increasing = True
        elif array[i] < array[i-1] and not increasing:
            decreasing = True
        else: 
            return False
    return True