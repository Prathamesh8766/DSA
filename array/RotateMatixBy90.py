matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

def RotatMatricsBy90(matrix):
    matrix2=[["" for _ in range(4)] for _ in range(4)]

    r = len(matrix)
    c=len(matrix[0])
    for i in range(r):
        for j in range(c):
            matrix2[j][(r-1-i)]=matrix[i][j]
    return matrix2        

print(RotatMatricsBy90(matrix))


def optimal(matrix):
        r = len(matrix)
        c=len(matrix[0])
        for i in range(r-1):
            for j  in range(i+1,r):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

        for i in matrix:
            i.reverse()        
        return(matrix)
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

print(optimal(matrix))