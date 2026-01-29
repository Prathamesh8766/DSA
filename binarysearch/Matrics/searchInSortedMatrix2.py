def optimal(mat,target):
    m = len(mat)
    n = len(mat[0])
    row, col = 0, n -1
    while row < m and col >= 0:
        if mat[row][col] == target: return [row, col]
        elif mat[row][col] >= target and target >= mat[row][0]:
             col = col -1
        else: row = row + 1
    return [-1,-1]         
matrix = [
    [1,  3,  5,  7,  9],
    [2,  4,  6,  8,  10],
    [4,  6,  8,  10, 12],
    [7,  9,  11, 13, 15],
    [10, 12, 14, 16, 18]
]
print(optimal(matrix,10))