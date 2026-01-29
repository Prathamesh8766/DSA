def printNRow(r):
    ans=1
    row = [1]

    for i in range(1,r):
        ans = ans * (r-i)
        ans = ans // (i)
        row.append(ans)
    return row    

def printElement(r,c):
    ans=1
    for i in range((c-1)):
        ans = ans * ((r-1)-i)
        ans = ans // (i+1)

    return i

def pascalTriangle(n):
    res = []
    for i in range(1, n + 1): 
        res.append(printNRow(i))
    return res
    
trinagle=pascalTriangle(6)
for row in trinagle:
    print(row)
        