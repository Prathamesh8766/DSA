def better(a1,a2,k):
    i ,j, count= 0, 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j] :
            count+=1
            if count == k:
                return a1[i]
            i+=1 
        else:
            count+=1
            if count == k:
                return a2[j]
            j+=1
    while i < len(a1):
        count+=1
        if count == k:
            return a1[i]
        i+=1
         
    while j < len(a2):
        count+=1
        if count == k:
            return a1[j]
        j+=1    
    return None

print(better([7, 12,14,15],[1,2,3,4,9,11],10))     


                   