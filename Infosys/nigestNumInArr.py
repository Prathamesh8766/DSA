def bigNum():
    n = int(input())

    nums = [0] * (n + 1)
    nums[0] = 0
    if n >= 1:
        nums[1] = 1

    for i in range(1, n + 1):
        if 2 * i <= n and 2 * i >= 2:
            nums[2 * i] = nums[i]
        if 2 * i + 1 <= n and 2 * i +1 >= 2:
            nums[2 * i + 1] = nums[i] + nums[i + 1]

    return nums, max(nums)


print(bigNum())