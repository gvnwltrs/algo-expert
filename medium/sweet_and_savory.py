def sweetAndSavory(dishes, target):
    
    dishes.sort()

    sweet = list(filter(lambda x: x < 0, dishes))
    sweet.sort(reverse = True)
    savory = list(filter(lambda x: x > -1, dishes))
    
    best_pair = [0,0]
    
    best_savoriness = float('inf')
    sweet_cursor = 0
    savory_cursor = 0

    while sweet_cursor < len(sweet) and savory_cursor < len(savory):
        savor = sweet[sweet_cursor] + savory[savory_cursor]
 
        if  savor <= target:
            savor_meter = target - savor
            if savor_meter < best_savoriness:
                best_savoriness = savor_meter
                best_pair = [sweet[sweet_cursor], savory[savory_cursor]]
            savory_cursor += 1
        else:
            sweet_cursor += 1
    

    return best_pair