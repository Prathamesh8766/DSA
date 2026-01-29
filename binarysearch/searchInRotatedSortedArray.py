# def locat_index(arr,target):
#             high = len(arr) -1
#             low = 0
#             locat = -1
#             while low <= high :
#                 mid = (low + high) // 2
#                 if arr[mid] == target:
#                     return mid
#                 if arr[low] <= arr[mid]:
#                     if arr[low] <= target and target <= arr[mid]:
#                         high = mid -1
#                     else:
#                         low = mid +1
#                 else:
#                     if arr[high] >= target and arr[mid] <= target  :
#                         low = mid +1
#                     else:
#                         high = mid -1
#             return -1            
                                    
          
def locat_index(nums,target,low=0,high = None):
            if high == None: high = len(nums) - 1
            if high < low:
                return -1
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid 
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    return locat_index(nums,target, low,mid - 1)
                else:
                    return locat_index(nums,target, mid + 1,high)
            else:
                if nums[high] >= target and nums[mid] <= target  :
                    return locat_index(nums,target, mid + 1,high)
                else:    
                    return locat_index(nums,target, low,mid - 1)


        
print(locat_index([7,8,9,1,2,3,4,5,6],4))           
