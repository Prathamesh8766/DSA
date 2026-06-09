from queue import Queue
def mhs(edge,n):
    adj = {}
    indegree= [0] * n
   
    for u,v in edge:
    
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
    q = Queue()

    for i in len(indegree):
        if indegree[i] == 1:
            q.put(i)
    remening = n-len(q)
    while remening > 2:

        node = q.get()
        

print(mhs([[1,0],[1,2],[0,3]],4))