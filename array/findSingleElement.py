def findSingelElement(arr):
    hash={}
    for i in arr:
        hash[i]=hash.get(i,0)+1

    for i in arr:
        if hash[i]==1:
            return i     

print(findSingelElement([1,2,1,2,3,3,4,4,5,5,123242122,-23,-23]))      


def findSingleElemetUsingXor(arr):
    xor=0
    for i in arr:
        xor=xor^i
    return xor
print(findSingleElemetUsingXor([1,2,1,2,3,3,4,4,5,5,123242122,-23,-23]))     