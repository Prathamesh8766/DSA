arr = [1,3,5,6]

def lowerBound(arr,target):
    high = len(arr) - 1
    low =0
    
    lower_bound = high + 1
    while low <= high :
        mid = (low + high) //2
        
        if arr[mid] >= target: 
            lower_bound = mid
            
            high = mid -1
                 
        else:
            low = mid + 1


    if lower_bound == len(arr): return  f"Lower Bound is  {lower_bound} "
    else: return f"Lower Bound is at {lower_bound} "


print(lowerBound(arr,5))    

def upperBound(arr,target):
    high = len(arr) - 1
    low =0
    
    upper_bound = high + 1
    while low <= high :
        mid = (low + high) //2
        
        if arr[mid] > target: 
            upper_bound = mid
            
            high = mid -1
              
        
        else:
            low = mid + 1


    if upper_bound == len(arr): return  f"Upper Bound is at {upper_bound} "
    else: return f"Upper Bound is at {upper_bound}"

print(upperBound(arr,10))