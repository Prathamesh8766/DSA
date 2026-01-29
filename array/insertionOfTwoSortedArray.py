# optimal
def insetionOfArray(nums1, nums2):
    nums1.sort()
    nums2.sort()
    insertion = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        
        if nums1[i] == nums2[j]:
            insertion.append(nums1[i])
            i += 1
            j += 1
        elif nums2[j] < nums1[i]:
            
            j += 1
        else: 
            
            i += 1
    return insertion

a2=[1,2,2,1]
a1=[2,2]
print(insetionOfArray(a1,a2))