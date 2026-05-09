from queue import Queue

def bfsTraverser(adj,start):
    q = Queue()
    bfs = []
    visited= {}
    visited[start] = True
    q.put(start)
    while(not q.empty()):
        node =  q.get()
        bfs.append(node)
        for i in adj.get(node,[]):
            if i not in visited:
                visited[i] = True
                q.put(i)
    return bfs, visited
adj = {
    0:[1,2,3],
    1:[0,1,2,3],
    2:[5,6],
    5:[7,8],
    6:[10,1]
}
print(bfsTraverser(adj,1))