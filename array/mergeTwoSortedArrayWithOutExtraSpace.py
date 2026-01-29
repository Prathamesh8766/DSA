def brut (nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    nums3 = []
    right = 0  
    left = 0
    while left < l1 and right < l2:

        if nums1[left] > nums2[right] :
            nums3.append(nums2[right])
            right += 1


        else  :
            nums3.append(nums1[left])
            left += 1
       
    while left <  l1:
        nums3.append(nums1[left])
        left += 1
    while right < l2:
        nums3.append(nums2[right])
        right += 1

    if l1 < l2:
        nums1 = nums3[:l1]
        nums2 = nums3[l1:(l1 + l2)]

    elif l2 < l1:
        nums2 = nums3[:l2]
        nums1 = nums3[l2:(l1 + l2)]
       

    return nums1 , nums2 ,nums3    
print(brut([1, 3, 5, 7], [0, 2, 6, 8, 9]))            


def better(nums1, nums2, n, m):
        left = n - 1
        right = 0

        while left >= 0 and right < m:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                right += 1
                left -= 1
            else:
                break
        nums1.sort()
        nums2.sort()
        return nums1 , nums2

print(better([1, 3, 5, 7], [0, 2, 6, 8, 9], len([1, 3, 5, 7]), len([0, 2, 6, 8, 9])))       

import math

def optimal2(nums1, m, nums2, n):
    gap = math.ceil((m + n) / 2)

    while gap > 0:
        left = 0
        right = gap
        while right < m + n:
       
            if left < m and right >= m:
                if nums1[left] > nums2[right - m]:
                    nums1[left], nums2[right - m] = nums2[right - m], nums1[left]


            elif left >= m:
                if nums2[left - m] > nums2[right - m]:
                    nums2[left - m], nums2[right - m] = nums2[right - m], nums2[left - m]


            else:
                if nums1[left] > nums1[right]:
                    nums1[left], nums1[right] = nums1[right], nums1[left]

            left += 1
            right += 1

        if gap == 1:
            break
        else:
            gap = (gap // 2) + (gap % 2)

    nums1[m:] = nums2[:n]
    return nums1
print(optimal2([1,2,3,0,0,0], 3, [2,5,6], 3))
print(optimal2([1], 1, [], 0))