
# We are given two non-empty arrays of positive integers: the first is going to represent the heights of students wearing red shirts and the second is going to represent the heights of students wearing blue shirts. The two arrays will always have the same length. We are asked to write a function that is going to find out if we can take a photo of these students that satisfies the following constraints:

# All the students that are wearing red shirts must be in the same row;
# All of the students that are wearing blue shirts must be in the same row;
# The photo must have exactly two rows and the two rows must have the same number of students in them.
# Every student in the front row must be shorter than the student directly behind them in the back row.
# The function is going to arrange the students and return true if we can take a photo that follows these constraints; otherwise return false.

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