
#s1
def smallestDifference(arrayOne, arrayTwo):
    smallest_difference = None
    
    closest_so_far = abs(arrayOne[0] - arrayTwo[0])

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            if abs(arrayOne[i] - arrayTwo[j]) < closest_so_far:
                closest_so_far = abs(arrayOne[i] - arrayTwo[j])
                smallest_difference = [arrayOne[i],arrayTwo[j]]
    
    return smallest_difference
