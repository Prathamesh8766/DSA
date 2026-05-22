from queue import Queue

def rottenOranges(matrix):

    q = Queue()
    visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                q.put([i, j, 0])
                visited[i][j] = 2

    maxtime = 0

    drow = [-1,0,1,0]
    dcol = [0,1,0,-1]

    while not q.empty():
        r,c,t = q.get()

        maxtime = max(maxtime,t)
        for i in range(4):
            nrow = drow[i] + r
            ncol = dcol[i] + c
            if (nrow >= 0 and nrow < len(matrix) and ncol >= 0 and ncol < len(matrix[0]) and 
                visited[nrow][ncol] != 2 and matrix[nrow][ncol] == 1):

                    q.put([nrow,ncol,t+1])
                    visited[nrow][ncol] = 2

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] != 2:
                return -1

    return maxtime


matrix = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

print(rottenOranges(matrix))
