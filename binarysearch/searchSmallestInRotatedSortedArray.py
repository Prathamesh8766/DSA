def searchSmallestInRotatedSortedArray(nums):
    high = len(nums) - 1
    low = 0
    smallest = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[mid]:
            smallest = min(nums[low], smallest,nums[mid])
            low = mid + 1
        else :
            smallest = min(nums[high], smallest,nums[mid])
            high = mid - 1
    return smallest
# print(searchSmallestInRotatedSortedArray([4,5,6,1,2,3]))
# print(searchSmallestInRotatedSortedArray([7,1,2,3,4,5]))  
# print(searchSmallestInRotatedSortedArray([1,2]))
# print(searchSmallestInRotatedSortedArray([3,1,2]))  
# print(searchSmallestInRotatedSortedArray([4,3,2,1]))   
# print(searchSmallestInRotatedSortedArray([1,2,3]))           
def main():
    nums = str(input())
    nums = list(map(float,nums.split()))
    print(searchSmallestInRotatedSortedArray(nums))

if __name__ == "__main__":
    main()