def brut(armid1,arr2):
    l1 = len(armid1)
    l2 = len(arr2)
    arr =[]
    i, j = 0,0
    while i < l1 and j < l2:
        if armid1[i] < arr2[j]:
            arr.append(armid1[i])
            i += 1
        else:
            arr.append(arr2[j]) 
            j += 1  
            
    while i < l1 :
        arr.append(armid1[i])
        i += 1
    while  j < l2:
        arr.append(arr2[j])
        j += 1    
    if len(arr) % 2 == 1:
        return f"Meadin is  {arr[(len(arr)//2 -1)]}"    
    else:
        return (arr[(len(arr)// 2 -1)] +arr[(len(arr)//2)] ) / 2
    
print(brut([1,1,3,5,7,9],[2,2,4,5,6]))


def better(armid1, arr2):
    l1 = len(armid1)
    l2 = len(arr2)
    i,j = 0 ,0
    ind1 = (l1+l2) // 2 - 1
    ind2 = (l1+l2) // 2  
    count = 0      
    indel1 = -1
    indel2 = -1
    while i < l1 and j < l2:
        if armid1[i] < arr2[j]:
            if ind1 == count : indel1 = armid1[i]
            if ind2 == count : indel2 = armid1[i]
            i+=1
        else:
            if ind1 == count : indel1 = arr2[j]
            if ind2 == count : indel2 = arr2[j]
            j+=1
        count += 1
    while i < l1:
        if ind1 == count : indel1 = armid1[i]
        if ind2 == count : indel2 = armid1[i]
        i+=1
    while j < l2:
        if ind1 == count : indel1 = arr2[j]
        if ind2 == count : indel2 = arr2[j]
        j+=1
    if (l1 + l2) % 2 == 1:
        return indel1
    else:
        return (indel1 + indel2)/2
    
print(better([1,1,3,5,7,9],[2,2,4,5,6]))
print(better([1,3,4,7,10,12],[2,3,6,15]))      
print(better([7,12,14,15],[1,2,3,4,9,11]))
def meadianof2sortedarray(a1,a2):
    n1 = len(a1)
    n2 = len(a2)
    high = min(n1,n2) -1
    low = 0
    half = (n1 + n2 + 1) // 2
    
    def canMake(mid1):
        mid2 = half - mid1 
        r1 = a1[mid1]
        r2 = a2[mid2]
        l1 = float("-inf") if mid1 - 1 == -1 else a1[mid1 - 1]
        l2 = float("-inf") if mid2 - 1 == -1 else a2[mid2 - 1]
        if l1 < r2 and l2 < r1 :
            if (n1 + n2) % 2 == 1:
                return min(r1,r2)
            else:
                return (max(l1,l2)+ min(r1,r2)) / 2
        if l1 > r2:
            return 1
        else: return -1
                
    while low <= high:
        mid = (low + high) // 2
        flag = canMake(mid)
        if flag == 1 :
            high = mid - 1
        elif flag == -1: low = mid + 1  
        else: return   flag 
print(meadianof2sortedarray([1,1,3,5,7,9],[2,2,4,5,6]))        
print(meadianof2sortedarray([7,12,14,15],[1,2,3,4,9,11]))