def xorSum():
    size = int(input("Enter the size:"))
    k = int(input("Enter size of k: "))
    a = []
    for i in range(size):
        a.append(int(input("Enter Element")))
    max_sum = 0
    for i in range(k):
        sum = 0
        for j in a:
            sum = sum + (i ^ j)
        max_sum=max(sum,max_sum)
                
    return max_sum
print(xorSum())