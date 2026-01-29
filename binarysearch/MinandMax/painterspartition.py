def brut(nums, p):
    left_sum = 0
    ans = float("inf")
    
    for i in range(len(nums)):
        left_sum = sum(nums[:i+1])
        right_sum = sum(nums[i+1:])
        max_time = max(left_sum, right_sum)
        ans = min(ans, max_time)
    return ans   
print(brut([10,20,30,40],2))    
        
def painter_partition_optimal(nums,p):
    lo = max(nums)
    hi = sum(nums)
    
    def canpaint(max_allow):
        cur = 1
        painter = 1
        for i in range(len[nums]):
            if nums[i] + cur <= max_allow:
                cur += nums[i]
            else:
                painter += 1
                cur = 0
            if painter  >p:
                return False
        return True
    
    while lo <= hi:
        mid= (lo+ hi) // 2
        if canpaint(mid) :
            hi = mid + 1
        else: lo = mid - 1
        
    return lo            
print(brut([10,20,30,40],2))