def leaderElement(arr):
    max=0
    leader=[]
    for i in range(len(arr)-1,-1,-1):
       
        if arr[i]   > max or i == (len(arr)-1) :
            leader.append(arr[i])
            max=arr[i]
    return leader
print(leaderElement([5,4,7,3,2,1]))

