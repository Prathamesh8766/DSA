def findIndexofPeakElement(nums):
    if len(nums) == 1:
        return nums[0]
       
    high = len(nums) - 1
    
    if nums[high-1] < nums[high] : return nums[high]
    if nums[0] >nums[1]: return nums[0]
    low = 1
    high = high - 1
    while(low<= high):
        mid = (low + high) // 2
        if nums[mid] >nums[mid-1] and nums[mid] >nums[mid + 1]:
            return nums[mid]
        elif nums[mid-1] < nums[mid]:
            low = mid + 1
        else:
            high = mid - 1    

def main():
    nums = list(map(float,input("Enter the elemet seprated by string: ").split()))  
    print(findIndexofPeakElement(nums))
if __name__ =="__main__":
    main()

