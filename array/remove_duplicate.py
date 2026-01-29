arr=[1,1,2,2,3,3,3,4]

def removeDuplicate(arr):
    i,j=0,1
    while j<len(arr):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
        j+=1

    return i+1

print(removeDuplicate(arr))        
