def searchSingleElementInnumsay(nums):
    if len(nums) == 1:
        return nums[0]
    high = len(nums) - 1
    low = 0
    if nums[low] != nums[low +1 ]: return nums[low]
    if nums[high] != nums[high - 1] : return nums[high]
    high = high - 2
    low = low + 1
    while low<= high:
        mid = (high + low) // 2
        print(f" mid at {mid} is {nums[mid]}")
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        if mid % 2 == 0:
            if nums[mid] == nums[mid -1]:
                 high  = mid - 1
            else:
                low = mid +1
        else:
            if nums[mid] == nums[ mid - 1]:
                low = mid + 1
            else: 
                high = mid - 1    


    return -1        
def main():
    nums = str(input())
    nums = list(map(float,nums.split()))
    print(searchSingleElementInnumsay(nums))

if __name__ == "__main__":
    main()
    # 0 1 2 3 4 5 6 7 8 9
    # 1 1 2 2 3 3 4 4 5 5 
    # 1 1 2 2 3 4 4 
    # 1 1 2 3 3 4 4 5 5