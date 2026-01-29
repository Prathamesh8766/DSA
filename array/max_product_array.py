import math

def Brut(arr):
    maximum = float("-inf")
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            pro = 1
            for k in range(i,j):
                pro = pro * arr[k]
            maximum = max(pro,maximum)

    return maximum
print(Brut([1,0,4,-1,2,-1,0,5]))    

def Better(arr):
    maximum = float(-math.inf)
    for i in range(len(arr)):
        pro = 1
        for j in range(i,len(arr)):
            pro = pro * arr[j]

            maximum =max(pro,maximum)

    return maximum

print(Better([2,0,3,-1,1,-2,4]))   


def Optimal(nums):
    j = len(nums)-1
    prefix = 1
    sufix =1
    maximum = float("-inf")
    for i in range(len(nums)):
        if prefix == 0:
            prefix = 1
        if sufix == 0:
            sufix = 1
        prefix = prefix * nums[i]
        sufix = sufix * nums[j-i]
        maximum = max(prefix, sufix ,maximum)
    return maximum

print(Optimal([2,0,3,-1,1,-2,4]))       

