def count(arr,n):
    hash=[0]*(n-1)

    for i in arr:
        hash[i]+=1
    for i in range(1,len(hash)):
        print(hash[i])  
arr=[1,2,2,1,3,4,5] 
count(arr,len(arr))


def countstring(s, n):
    hash = [0] *( n-1) 
    for ch in s:
        hash[ord(ch) - ord("a")] += 1

    for i in range(len(hash)):
        print(hash[i],end="")
    return    
s = "aaabbiccde"
countstring(s, len(s))

# ProVersion

def countNum(arr):
    count_map={}

    for i in arr:
        if i in count_map:
            count_map[i]+=1
        else:
            count_map[i]=1

    return count_map
print(countNum(arr))            

def countStr(string):
    count_map={}

    for i in string:
        if i in count_map:
            count_map[i]+=1
        else:
            count_map[i]=1

    return count_map
print(countStr(s))
