def logestCequence(nums):
        set1=set(nums)
        start=0
        logest=0
        for num in set1:
            if num-1 not in set1:
                count=1
                while num + count in set1:
                    count+=1

                logest =  max(logest,count)

        return logest        

print(logestCequence([1,45,2,67,68,46,47,3,68,67,66,3,4,47,6,5]))


def better(nums):
     nums.sort()
     count=0
     lowest=float("-inf")
     largest=0
     for i in range(len(nums)):
        if (nums[i]-1) != lowest and nums[i] != lowest:
             lowest = nums[i]
             count = 1
             if count > largest:
                  largest = count 
        elif (nums[i]-1) == lowest:
             count = count+1
             lowest = nums[i]
             if count > largest:
                  largest = count 

     return largest

print(better([103,102,101,105,104,4,3,3,3,2,2,1,1]))
