def kadanesAlgorithm(nums):

        max_sum=float("-inf")
        sum=0
        start=0
        end=0
        for i in range(len(nums)):
            if sum ==0:
                 start=i
            sum=sum + nums[i]
            if sum > max_sum:
                max_sum = sum
                end=i
            if sum < 0:
                sum=0

        return max_sum  , nums[start:end+1]
print(kadanesAlgorithm([-2,-3,4,-2,-2,1,5,-3]))