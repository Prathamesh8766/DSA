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
            
# print(cyclicArr())

def arrayElementRemovel():
    arr = list(map(int, input().split(",")))
    steps = 0

    arr.sort()   # ✅ fixed

    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1

    i = 0
    j = len(arr) - 1

    while i <= j:  
        if arr[i] != arr[j]:
            steps += 1
        else:
            break

        i += 1
        j -= 1   

    if i == j:
        return steps + 1
    elif i < j:
        return steps + (j - i + 1)
    else:
        return steps


print(arrayElementRemovel())