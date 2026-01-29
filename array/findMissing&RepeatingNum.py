def brut(nums):
    r , m = [],[]
    for i in range(1,len(nums)+1):
        count = 0
        for num in nums: 
            if num == i:
                count += 1
                if count > 1:
                    r.append(num)
                    break
        if count == 0:
            m.append(i)          
    return r,m
print(brut([5,3,1,5,6,6]))            
            
def better(nums):
    hash = {}
    m = []
    r = []
    for num in nums:
        hash[num] = hash.get(1,0) + 1

    for i in range(1,len(nums)+1):
        if hash.get(i,0) == 0:
            m.append(i)
        elif hash.get(i,0) > 1:
            r.append(i)

    return r,m       
print(better([5,3,1,5,6,6])) 

def optimal1(nums):
    n = len(nums)
    S = (n * (n + 1)) // 2
    S2 = (n * (n + 1) * (2 * n + 1)) // 6
    s, s2 = 0, 0
    for i in range(n):
        s += nums[i]
        s2 += nums[i] * nums[i]

    val1 = s - S
    val2 = s2 - S2
    val2 = val2/val1    

    r = (val1 + val2) //2
    m = (r - val1)

    return int(r), int(m)

print(optimal1([5,3,1,2,6,6]))