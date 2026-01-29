def agressiveCow(nums,k):
    
    allowed = 1
    max_allowed = nums[-1] - nums[0]
    
    while allowed<= max_allowed:
        cow = 1
        pre = 0
        next = 1
        
        while next < len(nums) and cow < k :
            if nums[next] - nums[pre] >= allowed:
                pre = next
                cow += 1  
            next+=1        
        if cow < k :
            return allowed -1    
        allowed += 1
    return max_allowed
print(agressiveCow([0,3,4,10],2))

def optimal(nums,k):
    nums= sorted(nums)
    low = 1
    high = max(nums)
    max_allowed = nums[-1] - nums[0]
    
    def canmake(allow):
        cow = 1
        pre = 0
        for i in range(len(nums)):
            if nums[i] - nums[pre] >= allow:
                pre = i
                cow += 1
        if cow < k:
            return False
        return True
            
    
    while low <= high:
        mid = (low + high) // 2
        if canmake(mid):
            low= mid + 1
            max_allowed = mid
        else:
            high = mid - 1
    return max_allowed        
                
print(optimal([1, 2, 4, 8, 9],3))                
print(optimal([10, 1, 2, 7, 5],3))
            