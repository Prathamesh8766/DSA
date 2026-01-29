def longestSubArray(arr,k):
    max=0
    start,end=0,0
    for i in range(len(arr)):
        sum=0
    
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            if sum==k :
               if (j-i+1)>max:
                   max=(j-i+1)
                   start=i
                   end=j
    return arr[start:end+1] if max >0 else[]
   
print(longestSubArray( [1, 2, 1, 1, -1,-1, 2, 1, 0, 3], 3))

def longest_subarray_with_sum_k(nums, k):
        pre_sum_map = {}
        curr_sum = 0
        max_len = 0
        start=0
        end=0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum == k:
                max_len = max(max_len, i + 1)

            rem = curr_sum - k
            if rem in pre_sum_map:
                length = i - pre_sum_map[rem]
                if length > max_len:
                    start=pre_sum_map[rem]+1
                    max_len=length
            if curr_sum not in pre_sum_map:
                pre_sum_map[curr_sum] = i

        return nums[start:max_len+start]
arr = [1, 2, 1, 1, -1,-1, 2, 1, 0, 3]
k = 3
print(longest_subarray_with_sum_k(arr, k))  # Output: 3

def optimal(arr,k):
    left=0
    right=0
    sum=arr[0]
    max_len=0
    while right<len(arr):
        while sum > k and left<= right:
            sum=sum-arr[left]
            left+=1
        if sum==k:
            max_len=max(max_len,(right-left+1))

        right+=1
        if right<len(arr):
            sum =sum+arr[right] 

    return max_len        

print(optimal([1,2,3,1,1,1,2,4,3],3))