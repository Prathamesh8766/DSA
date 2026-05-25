def sourroundRegion(matrix):
    if len(matrix) < 3 : return matrix
    visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    rows = len(matrix)
    cols = len(matrix[0])
    drow = [-1,0,1,0]
    dcol = [0,1,0,-1]
    def dfs(i,j):
        visited[i][j] = 1
        for k in range(4):
            nrow = i + drow[k]
            ncol = j + dcol[k]

            if (0 <= nrow < rows and 0 <= ncol < cols and visited[nrow][ncol] == 0 and matrix[nrow][ncol] == "O"):
                dfs(nrow, ncol)
        return
        
    for j in range(cols):
        if matrix[0][j] == "O" and visited[0][j] == 0:
            dfs(0, j)

    
    for i in range(rows):
        if matrix[i][cols - 1] == "O" and visited[i][cols - 1] == 0:
            dfs(i, cols - 1)

   
    for j in range(cols):
        if matrix[rows - 1][j] == "O" and visited[rows - 1][j] == 0:
            dfs(rows - 1, j)

   
    for i in range(rows):
        if matrix[i][0] == "O" and visited[i][0] == 0:
            dfs(i, 0)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "O" and visited[i][j] == 0:
                matrix[i][j] = "X"
    return matrix
board = [["X","O","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
print(sourroundRegion(board))


