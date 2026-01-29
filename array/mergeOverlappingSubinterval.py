def brut(nums):
    nums.sort()
    l = len(nums)
    result=[]
    for i in range(l):
        start = nums[i][0]
        end = nums[i][1]
        if  result  and end <= result[-1][1]:
            continue
        for j in range(i+1,l):
            if nums[j][0] <= end :
                end = max(end, nums[j][1])
            else:
                break

        result.append((start,end))    
    return result         


nums=[(1,3),(2,6),(8,9),(9,11),(8,10),(2,4),(15,18),(16,17)]
print(brut(nums))


def better(intervals):
        if not intervals :
            return []

        l = len(intervals)
        intervals.sort()
        result = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1,l):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
    
            else:
                result.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]

        result.append([start,end]) 
        return result
print(better(nums))    
