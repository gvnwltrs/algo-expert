# s1
def moveElementToEnd(array, toMove):

    to_move = []
    not_to_move = []

    for int in array:
        if int == toMove:
            to_move.append(int)
        else:
            not_to_move.append(int)

    return [*not_to_move, *to_move]
