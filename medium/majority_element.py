def majorityElement(array):
    if len(array) == 1:
        return array[0]
    
    half = len(array) / 2
    count = 1
    counted_major = (-1, -1)
    final = -1

    l = 0 
    r = 1
    while l < len(array)-1:
        if array[l] == array[r] and array[l] != counted_major[0]:
            count += 1
            r += 1
        else:
            r += 1

        if r > len(array)-1:
            if count > counted_major[1]:
                counted_major = (array[l], count)
            l += 1 
            r = l + 1
           
            count = 1

    if counted_major[1] > half:
        final = counted_major[0]
        
    return final
