import heapq
def numberOfWays(roads,n):
    Mod = 10**9 +7
    adj = {i: [] for i in range(n)}
    way = [0] * n
    for u, v, t in roads:
        adj[u].append((v, t))
        adj[v].append((u, t))
    time = [float("inf")] * n
    time[0] = 0
    pq = []
    dst = n - 1
    way[0]=1
    heapq.heappush(pq,(0,0))
    while pq:
        current_time,intersation = heapq.heappop(pq)
        if current_time > time[intersation]:
            continue

        for neighbour,t in adj.get(intersation,[]):
            new_time = current_time + t
            if time[neighbour] > new_time:
                time[neighbour] = new_time
                way[neighbour] = way[intersation]
                heapq.heappush(pq,(new_time,neighbour))
            elif new_time == time[neighbour]:
                way[neighbour] = (way[neighbour]+way[intersation]) % Mod
            
    return way[dst],way
print(numberOfWays(n = 12, roads = [[1,0,2348],[2,1,2852],[2,0,5200],[3,1,12480],[2,3,9628],[4,3,7367],[4,0,22195],[5,4,5668],[1,5,25515],[0,5,27863],[6,5,836],[6,0,28699],[2,6,23499],[6,3,13871],[1,6,26351],[5,7,6229],[2,7,28892],[1,7,31744],[3,7,19264],[6,7,5393],[2,8,31998],[8,7,3106],[3,8,22370],[8,4,15003],[8,6,8499],[8,5,9335],[8,9,5258],[9,2,37256],[3,9,27628],[7,9,8364],[1,9,40108],[9,5,14593],[2,10,45922],[5,10,23259],[9,10,8666],[10,0,51122],[10,3,36294],[10,4,28927],[11,4,25190],[11,9,4929],[11,8,10187],[11,6,18686],[2,11,42185],[11,3,32557],[1,11,45037]]))