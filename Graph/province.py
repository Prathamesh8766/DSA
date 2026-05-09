
def dfs(matrix,visited,node):
    visited[node] = True
    for j in range(len(matrix[0])):
        if matrix[node][j] == 1 and  not  visited[j]:
            dfs(matrix,visited,j)
def provincedfs(matrix):
    visited=[False]*len(matrix)
    count=0
    for i in range(len(matrix)):
        
            if  not visited[i]:
                count +=1
                dfs(matrix,visited,i)
    return count,visited


matrix = [
    [0,1,0,0,0],
    [1,0,0,0,0],
    [0,0,1,0,0],
    [0,0,0,0,1],
    [0,0,0,1,0]
]

print(provincedfs(matrix))




from queue import Queue
def bfs(matrix,visited,node):
   
    q= Queue()
    q.put(node)
    visited[node] = True
    while not q.empty():
        current = q.get()
    for j in range(len(matrix[0])):
        
        if matrix[current][j] == 1 and not visited[j]:
            visited[j] = True
            q.put(j)
def provincebfs(matrix):
    visited =    [False] * len(matrix)
    count =0
   

    for i in range(len(matrix)):
        if not visited[i]:
            count+=1
            bfs(matrix,visited,i)
    return count
print(provincebfs(matrix))