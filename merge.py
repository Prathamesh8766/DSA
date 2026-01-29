def merge(l1,s,m,e):
    i=sj=m+1
    ans =[]

    while(i<=m and j<=e):
        if(l1[i]<l1[j]):
            ans.append(l1[i])
            i+1
        elif (1[i]>l1[j]):
            ans.append(l1[j])
        else:
            ans.append(l1[i])
            ans.append(l1[j])


    while(i<=m):
        ans.append(l1[i])
        i+1
        
    while(j<=e):
        ans.append(l1[j])
        j+=1

    startOfAns=0
    startOlist=s 

    while(startOlist<=e):
        l1[startOlist]=ans[startOfAns]
        startOfAns+=1
        startOlist+=1
    return   
        