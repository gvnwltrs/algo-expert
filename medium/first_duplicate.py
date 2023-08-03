def firstDuplicateValue(array):
    duplicate = None # (value, duplicate_idx)

    if len(array) == 2:
        if array[0] == array[1]:
            return array[0]
    
    for i in range(len(array)):
        cursor = i+1
        while cursor <= len(array)-1:
            if array[cursor] == array[i] and duplicate is None:
                duplicate = (array[i], cursor)
                cursor += 1 
                break
            if array[cursor] == array[i] and cursor < duplicate[1]:
                print(array[cursor])
                duplicate = (array[i], cursor)
            cursor += 1 
            
    return -1 if duplicate is None else duplicate[0]