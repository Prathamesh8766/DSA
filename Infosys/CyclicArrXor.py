def cyclicArr():
    arr = list(map(int, input().split(",")))
    res = []
   
    max_val = -1
    
    for i in range(len(arr)):
        res= []
        res = arr[i:]+arr[:i]
        sum=0
        currentXor=0
        for num in res:
            currentXor ^= num
            sum += currentXor

        if sum > max_val:
            max_val = sum
    
    arr= arr[::-1]

    for i in range(len(arr)):
        res= []
        res = arr[i:]+arr[:i]
        sum=0
        currentXor=0
        for num in res:
            currentXor ^= num
            sum += currentXor

        if sum > max_val:
            max_val = sum
    return max_val
            
print(cyclicArr())