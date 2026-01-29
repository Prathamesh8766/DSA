def findKthNo(nums,k):
    for num in nums:
        if num <= k:
            k += 1
        else:
            return k  
        
print(findKthNo([2,3,4,6,7,11],5))   

def optimal(nums,k):
    low = 0
    high = len(nums) - 1
    while low<= high:
        mid = (low + high) // 2
        if nums[mid]-(mid+1) < k:
            low = mid + 1
        else: high = mid -1
    return low + k 

print(optimal([4,7,9],3))
#[0 1 2 3 4 5 ]
#[2 3 4 6 7 11]