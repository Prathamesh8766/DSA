def optimal(nums,k):
    hash = {0:1}
    count = 0
    presum = 0
    for i in range(len(nums)):
        presum = presum + nums[i]
        rem = presum - k
        count += hash.get(rem,0)
        hash[presum] = hash.get(presum,0) + 1
    return count    , hash

print(optimal([1,2,3,-3,1,1,1,4,2,-3],3))