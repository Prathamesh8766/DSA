def better(nums,target):
    
    l = len(nums)
    set1 = set()
    for i in range(l):
        for j in range(i+1, l):
            hash = []
            for k in range(j+1, l):
                a = target - (nums[i] + nums[j] + nums[k])

                if a in hash :
                    temp = [nums[i], nums[j], nums[k], a]
                    temp.sort()
                    set1.add(tuple(temp))

                hash.append(nums[k])    

    return list(set1)             

print(better([1, 2, -1, -2, 2, 0, -1], 0))

def optimal(nums,target):

        nums.sort()
        list = []
        l = len(nums)

        for i in range(l-3):
            if nums[i] > target:
                break

            if i > 0 and nums[i] == nums[i - 1]  :
                continue

            for j in range(i+1,l):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
            
                k = j + 1
                a = l - 1
                while k < a:
                    total = nums[i] + nums[j] + nums[k] + nums[a]

                    if total == target:
                        list.append([nums[i], nums[j], nums[k], nums[a]])

                        k += 1
                        a -= 1

                        while  nums[k] == nums[k - 1]    and k < a:
                            k += 1

                        while nums[a] == nums[a + 1] and k < a:
                            a -= 1

                    if total > target:
                        a -= 1

                    else:
                        k += 1

        return list
print(optimal([1, 2, -1, -2, 2, 0, -1], 0))                 