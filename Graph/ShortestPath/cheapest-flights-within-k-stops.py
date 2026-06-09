import heapq
def chepeast(n,flights,k,src,dst):
    dist = [float("inf")]*n
    pq = []
    adj = {}

    for u, v, price in flights:
        if u not in adj:
            adj[u] = []
        adj[u].append((v, price))
    heapq.heappush(pq,(0,src,0))
    while pq:
        c_price,node, stop = heapq.heappop(pq)
        if stop >k +1:
            continue

        if node == dst :
            return c_price
        
        for v, price in adj.get(node,[]):
                new_price = price+ c_price
                if dist[v] > new_price:
                    dist[v] = new_price
                heapq.heappush(pq,(new_price,v,stop+1))
    return -1
print(chepeast(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(chepeast(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
print(chepeast(n= 4, flights= [[0,3,59],[2,0,83],[2,3,32],[0,2,97],[3,1,16],[1,3,16]],k=3, dst =0,src =3))
print(chepeast(n= 4, flights= [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k= 1))
