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
    1:[2,6],
    2:[1,9,3],
    3:[2,4],
    4:[3,5],
    5:[4,11,6],
    6:[1,10]
}
print(dfsTraversel(adj,1))