[1,2,3,4,50,6]
def largest_element(arr):
    l=arr[0]
    for i in arr:
        if l<i:
            l=i
    return l        
print(largest_element([1,2,3,4,50,6]))

def s_l_element(arr):
    l=arr[0]
    s_l=float("-inf")
    for num in arr:
            if num > l:
                s_l = l
                l = num
            elif s_l < num < l:
                s_l = num     
    return s_l    
print(s_l_element([1,22,33,33,22,33,5,6,188,]))

