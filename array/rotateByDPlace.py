nums=[1,2,3,4,5,6,7]
# brut force
def rotateByDPlace(nums,k):
    k=k%len(nums)
    
    temp=[nums[i] for i in range(k+1) ]

    for i in range(len(nums)-k):
        nums[i]=nums[i-(len(nums)-k)]

    for i in range(len(nums) - k, len(nums)):
        nums[i]=temp[i-(len(nums)-k)]
    return nums
print(rotateByDPlace(nums,3))    

# Optimal
nums=[1,2,3,4,5,6,7,8,9,10]
def optimal(nums,d):
    d=d%len(nums)
    nums[0:d]=nums[0:d][::-1]
    nums[d:len(nums)]=nums[d:len(nums)][::-1]

    nums.reverse()
    return nums
print(optimal(nums,6))