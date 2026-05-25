from queue import Queue
def nearestZero(mat):
    drow = [-1,0,1,0]
    dclo = [0,1,0,-1]
    visited = [[0]*len(mat[0]) for _ in range(len(mat))]
    distance =  [[0]*len(mat[0]) for _ in range(len(mat))]
    q= Queue()

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] ==0:
                q.put([i,j])
                visited[i][j] = 1
              
    
    while not q.empty():
        r,c = q.get()

        for i in range(4):
            nrow = drow[i] + r
            ncol = dclo[i] + c
        
            if nrow >= 0 and nrow < len(mat) and ncol >= 0 and ncol < len(mat[0]) and visited[nrow][ncol] != 1:
                distance[nrow][ncol] = distance[r][c] + 1
                visited[nrow][ncol] = 1
                q.put([nrow,ncol])
    
    return distance

mat =[[0,0,0],[0,1,0],[1,1,1]]
print(nearestZero(mat))