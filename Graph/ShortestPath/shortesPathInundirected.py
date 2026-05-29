from queue import Queue
def shortesPath(graph,start):
    q = Queue()
    visited = [float("inf")] * len(graph)
    q.put(start)
    visited[start] =0
    while not q.empty():
        node = q.get()

        for neighbour in graph.get(node,[]):

                if visited[neighbour] > visited[node]+1:
                    visited[neighbour]= visited[node] +1
                    q.put(neighbour)
    return visited
adj = {
    0:[1,2,3],
    1:[0,2,3],
    2:[0,1,5,4,6],
    3:[0,1,5,6],
    4:[2,7],
    5:[2,5,7],
    6:[2,3],
    7:[4,5]
}
print(shortesPath(adj,0))
