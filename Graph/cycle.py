def cycle(prerequisites,numCourses):
    adj = {}
    for a, b in prerequisites:
        if b not in adj:
            adj[b] = []
        adj[b].append(a)

    print(adj)
    visited = [0] * numCourses


    def dfs(node):
        if visited[node] == 1: return False

        if visited[node] == 2: return True

        visited[node] =  1

        for i in adj.get(node,[]):
            if not dfs(i):
                return False

        visited[node] = 2

        return True
    for course in range(numCourses):
        if not dfs(course): return False
    return True
    


print(cycle(numCourses = 6,
prerequisites =[[1,0]]))

