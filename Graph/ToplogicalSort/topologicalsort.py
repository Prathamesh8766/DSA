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
    0:[1,2,3],
    1:[2,3],
    2:[5,6],
    3:[],
    4:[5],
    5:[3],
    6:[5]
}
print(topplogicalSort(adj))