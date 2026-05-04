# def optimal(nums):
#     l = len(nums)
#     second = None
#     largest = nums[0]
#     for i in range(l):
#         if nums[i] > largest:
#             second = largest
#             largest = nums[i]
#         if nums[i]  < largest and nums[i] > second:
#             second = nums[i]

#     return second     

# print(optimal([12, 35, 1, 10, 34, 1]))


def optimal(num):
    second = None
    largest = num[0]
    for i in range(len(num)):
        if num[i] >= largest:
            second = largest
            largest = num[i]
        elif  num[i] >second:
            second = num[i]
    return second
print(optimal([12, 35, 1, 10, 34, 1]))