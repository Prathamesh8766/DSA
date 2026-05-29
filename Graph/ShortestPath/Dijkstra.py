import heapq
def dijkstra(graph,start):
    distance = [float("inf")] * len(graph)
    distance[start] = 0
    pq = []
    heapq.heappush(pq,(0,start))
    
    while pq:
        dist,node= heapq.heappop(pq)
        for neighbour, weight in graph[node]:
            if distance[neighbour] > dist + weight:
                distance[neighbour] = dist + weight
                heapq.heappush(pq,(distance[neighbour],neighbour))
    return distance
print(dijkstra({
    0: [(1,4), (2,1)],

    1: [(3,1)],

    2: [(0,0),(1,2), (3,5), (4,8)],

    3: [(5,3)],

    4: [(5,1)],

    5: [(6,2)],

    6: [(4,1), (7,4)],

    7: []
},1))