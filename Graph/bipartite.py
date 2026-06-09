def bipartite(graph):

    adj = {}

    for i in range(len(graph)):

        adj[i] = graph[i]
    print(adj)
    visited = [0]*len(adj)
    def dfs(node,color):

        visited[node] = color
        for negebhour in  adj[node]:
            if visited[negebhour] ==0:
                if dfs(negebhour,-color) == False: return False
            elif visited[negebhour] == color: return False
        return True
    for i in range(len(adj)):
        if visited[i] == 0:
            if dfs(i,1) == False: return False
    return True
print(bipartite([[1,2],[2,3],[5],[0],[5],[],[]]))