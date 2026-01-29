def BrutCountInversion(arr):
    pair = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                pair.append((arr[i], arr[j]))
    return pair            

print(BrutCountInversion([5, 3, 2, 4, 1]))


# def optimalCountInversion(arr):
#     count = 0  # Initialize count here
   
#     def merge(arr, low, mid, high):
#         nonlocal count # Use nonlocal to modify the outer count
#         left, right = low, mid + 1
#         temp = []
#         while left <= mid and right <= high:
#             if arr[left] <= arr[right]:
#                 temp.append(arr[left])
#                 left += 1
#             else:
#                 temp.append(arr[right])
#                 right += 1
#                 count += (mid - left + 1)  # Increment count here
                
#         while left <= mid:
#             temp.append(arr[left])
#             left += 1

#         while right <= high:
#             temp.append(arr[right])
#             right += 1

#         # Copy temp back to arr
#         for i in range(len(temp)):
#             arr[low + i] = temp[i]


#     def mergesort(arr, low, high):
#         if low < high:  # Correct base case
#             mid = (low + high) // 2
#             mergesort(arr, low, mid)
#             mergesort(arr, mid + 1, high)
#             merge(arr, low, mid, high)
#         return count

#     return mergesort(arr, 0, len(arr) - 1)
# print(optimalCountInversion([5, 3, 2, 4, 1]))

def optimalCOuntInversion(arr):
    count = 0
    def mergesort(arr,low,mid,high):
        left = low
        right = mid + 1
        nonlocal count 
        temp = []
        while left <=mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right]) 
                right += 1
                count += (mid-left+1)
        while left <= mid:
            temp.append(arr[left]) 
            left +=1
        while right <= high:           
            temp.append(arr[right])
            right+=1
        for i in range(len(temp)):
            arr[low +i] = temp[i]    

    def mergesort(arr,low,high):
        if low < high:
            mergesort(arr,low,mid)
            mergesort(arr,mid+1,high)
            merge(arr,low,mid,high)
        return            

