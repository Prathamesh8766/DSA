def numberOfIsland(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[0]*cols for _ in range(rows)]
    count=0
    drow = [-1,0,1,0]
    dclo = [0,1,0,-1]
    def dfs(i,j):
        visited[i][j] = 1
        for k in range(4):
            nrow = i + drow[k]
            ncol = j + dclo[k]
            if (0 <= nrow < rows and 0 <= ncol < cols and visited[nrow][ncol] == 0 and matrix[nrow][ncol] == "1"):
                dfs(nrow, ncol)
        

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1" and visited[i][j] == 0:
                count+=1
                dfs(i,j)
                
    return count
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numberOfIsland(grid))

