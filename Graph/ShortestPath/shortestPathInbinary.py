from queue import Queue
def shortestPath(matrix):
    rows= len(matrix)
    cols = len(matrix[0])
    
    if matrix[0][0] == 1 or matrix[rows-1][cols-1] == 1:
        return -1
    q = Queue()
    q.put((0,0,1))
    drow = [-1,-1,-1,0,1,1,1,0]
    dcol = [-1,0,1,1,1,0,-1,-1]
    while not q.empty():
        i,j,d = q.get()
        if i == rows -1 and j == cols-1:
            return d
        for k in range(8):
            nrow = drow[k] + i
            ncol= dcol[k] + j
            if 0<= nrow <rows  and 0<= ncol <cols and matrix[nrow][ncol] == 0 :
                matrix[nrow][ncol] = 1
                q.put((nrow,ncol,d+1))
                
    return -1

print(shortestPath([[0,0,0],[1,1,0],[1,1,0]]))