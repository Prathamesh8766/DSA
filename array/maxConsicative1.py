def maxConsicativeWith1(arr):
    count,max=0,0

    for i in arr:
        
        if i ==0:
            count=0
        else:
            count=count+1    
        if count>max:
            max=count
    return max

print(maxConsicativeWith1([1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1]))            