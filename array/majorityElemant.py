def majorityElement(nums): # Using Mooris voting algorithm
    count = 0
    el = nums[0]
    for i in range(len(nums)):
        
        if el == nums[i] :
            count += 1
        if  count == 0:
            el = nums[i]
            count += 1
        elif el != nums[i]:
            count  -= 1  
    if nums.count(el) > len(nums)//2:
        return el

print(majorityElement([7,7,5,1,5,7,5,7,5,5,5,5]))
nums=[7,7,5,1,5,7,5,7,5,5,5,5]
print(f"len= {len(nums)} and {int(len(nums) / 3 + 1)}")