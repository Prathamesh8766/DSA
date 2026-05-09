def dfs(node,adj,visited,ls):
        visited[node] = True
        ls.append(node)
        for i in adj.get(node,[]):
            if i not in visited:
                dfs(i,adj,visited,ls)
def dfsTraversel(adj,start):
    visited = {}
    visited[start] = True
    ls= []
    dfs(start,adj,visited,ls)
    return ls
    
    
adj = {
    0:[1,2,3],
    1:[0,1,2,3],
    2:[5,6],
    5:[7,8],
    6:[10,1]
}
print(dfsTraversel(adj,2))