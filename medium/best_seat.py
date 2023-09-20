
'''
You walk into a theatre you're about to see the show in. The usher within the theatre walks you to your row and mentions, 
and mentions your're allowed to sit anywhere in a given row. Naturally, you'd like to sit in a sit that gives you the most
space. You would also prefer that this space be evenly distributed on either side of you (e.g. if there are three empty
seats in a row, you would prefer to sit in the middle of those three seats). 

Given the theatre row represented as an integer array, return the seat index of where you should sit. Ones represent
occupied seats and zeroes represent empty seats. You may assume that someone is always sitting in the first and last seat 
of the row. Whenever there are two equally good seats, you should sit in the seat with the lower index. If there is no seat 
to sit in, return -1. The given array will always have a length of at least one and contain only ones and zeroes.
'''

def bestSeat(seats):
    best_seat = -1 
    max_space = 0

    left = 0 
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right +=1

        available_space = right - left - 1
        if available_space > max_space: 
            best_seat = (left + right) // 2
            max_space = available_space

        left = right 
    
    return best_seat

