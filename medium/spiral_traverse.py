def spiralTraverse(array):
    flat_array = []
    start_row, end_row = 0, len(array)-1
    start_col, end_col = 0, len(array[0])-1

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col+1):
            flat_array.append(array[start_row][col])

        for row in range(start_row+1, end_row+1):
            flat_array.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            flat_array.append(array[end_row][col])

        for row in reversed(range(start_row+1, end_row)):
            if start_col == end_col:
                break
            flat_array.append(array[row][start_col])

        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1
      
    return flat_array