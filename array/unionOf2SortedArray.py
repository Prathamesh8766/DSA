def unionOf2SortedArray(arr1,arr2):
    union=[]
    j,i=0,0
    while i<len(arr1) and j < len(arr2):
        if arr1[i]<=arr2[j]:
            if len(union)==0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr2[j] <= arr1[i]:
            if len(union)==0 or union[-1] != arr2[j] :   
                union.append(arr2[j])
            j+=1

    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1       
    return union

a1=[1,1,2,3,4,5]
a2=[2,3,4,4,5,6]
print(unionOf2SortedArray(a1,a2))
             