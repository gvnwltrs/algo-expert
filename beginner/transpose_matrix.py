def transposeMatrix(matrix):
    transpose_matrix = [[None] * len(matrix) for _ in range(len(matrix[0]))]
    
    for i in range(len(transpose_matrix)):
        for j in range(len(matrix)):
            transpose_matrix[i][j] = matrix[j][i]

    return transpose_matrix