def enclaves(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0]*cols for _ in range(rows)]
    count = 0
    drow = [-1,0,1,0]
    dcol = [0,1,0,-1]

    def dfs(i,j):
        visited[i][j] = 1
        for k in range(4):
            nrow = drow[k] + i
            ncol = dcol[k] + j
            if 0 <= nrow < rows and 0 <= ncol < cols and visited[nrow][ncol] != 1 and grid[nrow][ncol] == 1:
                dfs(nrow,ncol)
        return
    
    for j in range(cols):
        if grid[0][j] == 1 and visited[0][j] != 1:
            dfs(0,j)
        if grid[rows -1][j] == 1 and visited[rows - 1][j] != 1:
            dfs(rows-1, j)
    for i in range(rows):
        if grid[i][0] == 1 and visited[i][0] !=1:
            dfs(i,0)
        if grid[i][cols-1] == 1 and visited[i][cols -1] != 1:
            dfs(i,cols-1)
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == 0 and grid[i][j] == 1 :
                count+=1
    return count, visited, grid
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(enclaves(grid))