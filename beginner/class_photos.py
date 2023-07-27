def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    check = []
    for r_index, r_value in enumerate(redShirtHeights):
        if r_value > blueShirtHeights[r_index]:
            check.append('Taller')
        elif r_value == blueShirtHeights[r_index]:
            check.append('Same')
        else:
            check.append('Shorter')
            
    taller_or_shorter = all(x == check[0] for x in check) and all(x != 'Same' for x in check)
    return taller_or_shorter