def alieanDictionary(dictiorary,N,K):
    adj={}
    result = []
    for i in range(N-1):
        st1 = dictiorary[i]
        st2 = dictiorary[i+1]
        l = min(len(st1),len(st2))
        for j in range(l):
            if st1[j] != st2[j]:
                u = ord(st1[j]) - ord('a')
                v = ord(st2[j]) - ord('a')
                if u not in adj:
                    
                    adj[u]=[]
                adj[u].append(v)
                break
    visite=[0] * K
    def dfs(node):
        visite[node] = 1
        for neghubore in adj.get(node,[]):
            if visite[neghubore] == 0:
                dfs(neghubore)
        result.append(node)

    for i in range(K):
        if visite[i] ==0:
            dfs(i)
    result2 = []
    for i in result:
        result2.append(chr(i+97))
    return result2[::-1]



dictionary = ["baa","abcd","abca","cab","cad"]

N = 5
K = 4

print(alieanDictionary(dictionary, N, K))
    