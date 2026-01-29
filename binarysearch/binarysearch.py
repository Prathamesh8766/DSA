arr = [0,1,2,3,4,5,6,7,8,9,10,45,67,89]


def binarySearch1(arr,el):
    if len(arr) == 0:
        return False

    midle = len(arr)//2
    midEl= arr[midle]
    if midEl == el:
        return True
    elif midEl > el:
       return binarySearch1(arr[:midle],el)
    elif midEl < el:
        return binarySearch1(arr[midle+1:],el)  
     

print(binarySearch1(arr,45))


def binarySearch2(arr, el, low = 0, high = None):
    if high == None: high = len(arr) - 1
            
    if low > high: return f"Element {el} is not Present"

    mid = (low + high) // 2

    if arr[mid] == el: return f'Elment {el} is present at {mid}'
        
    elif arr[mid] > el: return binarySearch2(arr, el, low, mid -1)  

    else: return binarySearch2(arr, el, mid + 1, high)
           
    

print(binarySearch2(arr,0))


def binarySearch3(arr,el):
    
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == el :
            return f'Elment {el} is present at {mid}'

        elif arr[mid] > el:
            high = mid - 1 

        else:
            low = mid + 1    
    return  f"Element {el} is not Present" 

print(binarySearch3(arr,89))
