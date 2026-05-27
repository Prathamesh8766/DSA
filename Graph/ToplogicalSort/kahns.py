from queue import Queue
def kahn(graph):
    result= []
    indegree = [0] * len(graph)

    for node in range(len(graph)):

        for neighbour in graph[node]:

            indegree[neighbour] += 1

    q = Queue()
    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.put(i)
         

    while not q.empty():

        node = q.get()
        result.append(node)
        print(node)
        for neghubore in graph[node]:

            indegree[neghubore] = indegree[neghubore] - 1
            if indegree[neghubore] == 0:
                q.put(neghubore)
                
                
    return result,indegree
print(kahn([[1,2],[2],[5],[0],[5],[],[]]))