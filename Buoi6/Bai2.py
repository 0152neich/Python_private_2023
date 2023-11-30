def transpose_matrix(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transposed_matrix = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
transposed_matrix = transpose_matrix(matrix)
for i in range(n):
    for j in range(m):
        print(transposed_matrix[i][j], end=' ')
    print()
