def logestPath(matrix):
    rows = len(matrix)
    clos= len(matrix[0])
    drow = [-1,0,1,0]
    dclo = [0,1,0,-1]
    maxlen = 0
    dp = [[0]*clos for _ in range(rows)]
    def dfs(i,j):
        if dp[i][j] != 0:
            return dp[i][j]
        ans =1
        for k in range(4):
            nrow = drow[k] + i
            nclo = dclo[k] + j
            if 0 <= nrow < rows and 0 <= nclo < clos and matrix[nrow][nclo] < matrix[i][j]:
                ans= max(ans,1+dfs(nrow,nclo))
        dp[i][j] = ans
        return ans
    for i in range(rows):
        for j in range(clos):
            
            maxlen= max(maxlen,dfs(i,j))
    return maxlen

print(logestPath([[9,9,4],[6,6,8],[2,1,1]]))