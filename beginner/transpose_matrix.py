


def transposeMatrix(matrix):
    transpose_matrix = [[None] * len(matrix) for _ in range(len(matrix[0]))]
    
    for i in range(len(transpose_matrix)):
        for j in range(len(matrix)):
            transpose_matrix[i][j] = matrix[j][i]

    return transpose_matrix

# time complexity: O(n * m) where n is the number of rows and m is the number of columns | space complexity: O(n * m) where n is the number of rows and m is the number of columns
'''
vertical matrix = [[1], [2], [3]]
horizontal matrix = [[1, 2, 3]]

flipped vertical matrix = [[1, 2, 3]]
flipped horizontal matrix = [[1], [2], [3]]
'''