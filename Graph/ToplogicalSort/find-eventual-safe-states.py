def fiendEventualSafeNode(graph):
    result = []

    visited = [0] * len(graph)
    def dfs(node):
        if visited[node] == 1: return False
        visited[node] = 1
        if visited==2 : return True
        for i in graph[node]:
            if dfs(i) == False:
                return False
        visited[node] = 2
        print(visited)
        return True
    for i in range(len(graph)):
       
            if dfs(i):
                result.append(i)
    return result
print(fiendEventualSafeNode([[1,2],[2,3],[5],[0],[5],[],[]]))