def courseShedular2(prerequisites,numCourses):
    adj = {}
    result = []
    for a, b in prerequisites:
        if b not in adj:
            adj[b] = []
        adj[b].append(a)
    visited = [0]*numCourses
    def dfs(node):
        if visited[node] == 1: return False

        if visited[node] == 2: return True

        visited[node] = 1
        
        for i in adj.get(node,[]):

            if dfs(i) == False:return False

        visited[node] = 2
        result.append(node)
        return True

    for i in range(numCourses):
        if dfs(i) == False: return []
    return result[::-1]

print(courseShedular2([[1,0],[2,0],[3,1],[3,2]],4))