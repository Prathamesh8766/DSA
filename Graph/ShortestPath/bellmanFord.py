def bellmanFord(n,adj):
    dist = [float("inf")] * n
    dist[0] = 0
    for i in range(n):
        for li in adj:
            u = li[0]
            v = li[1]
            wt = li[2]
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    
    for li in adj:
            u = li[0]
            v = li[1]
            wt = li[2]
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                return -1
    return dist

adj = [
    [0, 1, -1],
    [0, 2, 4],
    [1, 2, 3],
    [1, 3, 2],
    [1, 4, 2],
    [3, 2, 5],
    [3, 1, 1],
    [4, 3, -3]
]
print(bellmanFord(5,adj))