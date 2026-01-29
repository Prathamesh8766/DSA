def brut(nums, k):
    l = len(nums)
    count = 0
    
    for i in range(l):
        for j in range(i, l):
            xor =0
            for a in range(i,j+1):
                xor = xor ^ nums[a]
            if xor == k:
                count += 1
    return count                
print(brut([4, 2, 2, 6, 4],6))

def better(nums, target):

    l = len(nums)
    count = 0

    for i in range(l):
        xor = 0
        for j in range(i, l):
            xor = xor ^ nums[j]

            if xor == target:
                count += 1

    return count

print(better([4, 2 ,2, 6 ,4], 6))                

def optimal(nums, target):
    l = len(nums)
    count = 0
    xor = 0
    hash = {0 : 1}
    for i in range(l):
        xor = xor ^ nums[i]
        rem = xor ^ target
        count += hash.get(rem, 0)
        hash[xor] = hash.get(xor, 0) + 1

    return count
print(optimal([4, 2 ,2, 6 ,4], 6))
    
