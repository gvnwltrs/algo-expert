def bubbleSort(array):
    elements = len(array)-1
    still_sorting = True

    while still_sorting:
        still_sorting = False
        for idx, value in enumerate(range(elements)):
            if array[idx+1] < array[idx]:
                still_sorting = True
                temp = array[idx]
                array[idx] = array[idx+1]
                array[idx+1] = temp
        elements -= 1
    return array