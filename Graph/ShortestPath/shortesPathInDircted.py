from queue import Queue
def sortestPathInDirecttedWeightGraph(graph,start):
    distance = [float("inf")] * len(graph)
    q = Queue()
    q.put(start)
    distance[start] = 0
    while not q.empty():
        node = q.get()
        for neighbour,weight in graph.get(node,[]):
            if distance[neighbour] > distance[node] + weight:
                distance[neighbour] = (distance[node]+ weight)
                q.put(neighbour)

    return distance
adj = {
    0: [(1,4), (2,1)],

    1: [(3,1)],

    2: [(0,0),(1,2), (3,5), (4,8)],

    3: [(5,3)],

    4: [(5,1)],

    5: [(6,2)],

    6: [(4,1), (7,4)],

    7: []
}
print(sortestPathInDirecttedWeightGraph(adj,1))