def MinimiseMaximumDistancebetweenGasStationsBrut(nums, k):
    howmany = [0] *(len(nums) -1)
    
    for gasstation in range(1,k +1):
        maxdistance =-1
        maxindex = -1
        for j in range(len(nums)-1):
            diff = nums[j+1] - nums[j]
            section = diff / (howmany[j] +1)
            print(f'Gastation{gasstation}, section {j}-{j+1} = {section}')
            if section > maxdistance:
                maxdistance= section
                print(f"maxdistance =          {maxdistance}")
                maxindex = j
                
        howmany[maxindex] += 1
    
    max_ans = -1
    for i in range(len(nums)-1)  :
        diff = nums[i+1] - nums[i]
        section = diff / (howmany[i] +1)  
        max_ans = max(max_ans,section)  
                
    return max_ans
print(MinimiseMaximumDistancebetweenGasStationsBrut([1,13,17,23],5))
print(MinimiseMaximumDistancebetweenGasStationsBrut([1,2,3,4],4))