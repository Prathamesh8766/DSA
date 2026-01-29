def brut(nums):
    l = len(nums)
    set1 = set()
    
    for i in range(l):

        for j in range(i + 1, l):

            for k in range(j + 1, l):

                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    set1.add(tuple(temp))

    return list(set1)


print(brut([-1, 0, 1, 2, -1, -4]))


def better(nums):
    set1 = set()
    l = len(nums)

    for i in range(l):
        hash = []

        for j in range(i + 1, l):
            k = -(nums[i] + nums[j])

            if k in hash:
                temp = [nums[i], nums[j], k]
                temp.sort()
                set1.add(tuple(temp))

            hash.append(nums[j])

    return list(set1)


print(better([-1, 0, 1, 2, -1, -4]))


def optimal(nums):
    l = len(nums)
    list = []
    nums.sort()

    for i in range(l):

        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = l - 1
        
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total == 0:
                list.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j + 1]: 
                    j += 1

                while j < k and nums[k] == nums[k - 1]:
                    k -= 1

            elif total > 0:
                k -= 1

            else:
                j += 1

    return list


print(optimal([-1, 0, 1, 2, -1, -4, -2]))
