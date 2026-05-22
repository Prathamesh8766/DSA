from queue import Queue
def floodFill(matrix,colour,sr,sc):
    q = Queue()
    q.put([sr,sc])
    visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    matrix[sr][sc] = colour
    visited[sr][sc] = colour
    drow = [-1,0,1,0]
    dclo = [0,1,0,-1]
    while not q.empty():
        
        r,c = q.get()
        print(f"R  is {r} and C is {c}")
        for i in range(4):
            nrow = drow[i]+r
            ncol = dclo[i] +c
            if nrow >= 0 and nrow < len(matrix) and ncol >= 0 and ncol < len(matrix[0]) and visited[nrow][ncol] != colour and matrix[nrow][ncol] != 0:
                print(f"nrow {nrow} and crow is {ncol}")
                q.put([nrow,ncol])
                visited[nrow][ncol] = colour
                matrix[nrow][ncol] = colour
                
        
    
    
    return matrix
matrix = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
print(floodFill(matrix,2,1,1))

