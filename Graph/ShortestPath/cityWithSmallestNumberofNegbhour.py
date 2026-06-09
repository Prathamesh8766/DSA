def cityWithSmallestNeghoubre(n,edges,distanceThreshold):
    dist = [[float("inf")]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for li in edges:
        i = li[0]
        j = li[1]
        wt = li[2]
        dist[i][j] = wt
        dist[j][i] = wt

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    
    min_neghobure = float("inf")
    result = -1

    for i in range(n):
        recheable = 0
        for j in range(n):

            if i!= j and dist[i][j] <= distanceThreshold:
                recheable += 1

        if recheable <= min_neghobure:
            min_neghobure = recheable
            result = i
    return result
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(cityWithSmallestNeghoubre(n,edges,distanceThreshold))