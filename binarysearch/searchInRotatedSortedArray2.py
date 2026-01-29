def searchInRotatedSortednumsay2(nums,target):
    high = len(nums)-1
    low = 0

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] == nums[high]  and nums[mid] == nums[low] :
            high = high -1
            low = low +1
        elif nums[mid] >= nums[low]:
            if nums[mid] >= target and target >= nums[low]  :
                high = mid -1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1

print(searchInRotatedSortednumsay2([4,5,6,6,7,0,1,2,4,4],5))

print(searchInRotatedSortednumsay2([3,1,2,3,3,3,3],2))
print(searchInRotatedSortednumsay2([7,8,9,1,2,3,4,5,6],4)) 
print(searchInRotatedSortednumsay2([3,3,3,3,3,3,1,3],1))