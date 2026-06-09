import heapq
def primeAlo(V, adj):
    pq = []
    heapq.heappush(pq, (0, 0, -1))
    visited = [0] * V
    mst = []
    sum =0
    while pq:
        wt ,node, prNode = heapq.heappop(pq)
        if visited[node] == 1: continue
        visited[node] = 1
        if prNode != -1:
            mst.append((prNode, node, wt))
        sum += wt
        for neighbour in adj.get(node,[]):
            neighbourNode = neighbour[0]
            neighbourWt = neighbour[1]
            if visited[neighbourNode] != 1:
                heapq.heappush(pq, (neighbourWt, neighbourNode, node))   
    return mst, sum

adj_prim = {
    0: [(1, 2), (2, 4)],
    1: [(0, 2), (2, 1), (3, 7)],
    2: [(0, 4), (1, 1), (3, 3)],
    3: [(1, 7), (2, 3)]
}


print(primeAlo(4,adj_prim))