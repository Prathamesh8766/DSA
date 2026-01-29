def BrutReversePair(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > 2 * arr[j]:
                count += 1
    return count   

print(BrutReversePair([40, 25, 19, 12, 9, 6, 2]))        

def OptimalReversePair(nums):
    
   
    def merge(nums, low, mid, high):
        
        left, right = low, mid + 1
        temp = []
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
            
            
                
        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        # Copy temp back to arr
        for i in range(len(temp)):
            nums[low + i] = temp[i]


    def Count(nums, low, mid, high):
        right = mid + 1
        count = 0
        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            count = count + (right -(mid + 1))  
        return  count  


    def mergesort(nums, low, high):
        count = 0
        if low < high:  # Correct base case
            
            mid = (low + high) // 2
            count += mergesort(nums, low, mid)
            count += mergesort(nums, mid + 1, high)
            count += Count(nums, low, mid, high)
            merge(nums, low, mid, high)
        return count

    return mergesort(nums, 0, len(nums) - 1)

print(OptimalReversePair([40, 25, 19, 12, 9, 6, 2]))   