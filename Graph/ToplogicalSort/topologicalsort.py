def topplogicalSort(adj):
    visited = [0]*len(adj)
    result = []
    def dfs(node):
        visited[node] = 1
        for i in adj.get(node,[]):
            if visited[i] == 0:
                dfs(i)
        result.append(node)

    for i in range(len(adj)):
        if visited[i] == 0:
            dfs(i)
    return result[::-1]
adj = {
    0:[],
    1:[7],
    2:[3],
    3:[6],
    4:[0,1],
    5:[0,2],
    6:[7],
    7:[]
}
print(topplogicalSort(adj))