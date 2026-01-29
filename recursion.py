
# def palidrom(s):
#     if len(s)==1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     return palidrom(s[1:-1])

# print(palidrom("madam"))

# def factorial(n):
#     if n==1 or n==1:
#         return 1

#     return n*factorial(n-1)

# print(factorial(3))


def gcd(a,b):  #14,12
    # r = minimum
    # if maximum % r ==0 and minimum % r ==0:
    #     return r
    # x = gcd(maximum,r-1)


    if(a == 0):
        return b
    
    return gcd(b%a,a)

    # if a % b==0 and b % b ==0:
    #     return a
    # return gcd(a,b-1)
    



    # print(r)    
# print(gcd(98,56)
# )


# print(gcd(12,14))


# 12,14
# # 14%12 -> 12,2 -> 12%2,2 -> 0,2
# 14%7

# 14%12


# l=[1,2,[3,9],5,[6],7]

# def list_sum(l):
#     total=0
#     for i in l:
#         if type(i) == int:
#             total=total + i
#         else:
#             total=total+list_sum(i) 
#     return total

# print(list_sum(l))        
# def gcd(maximum, r):
#     if maximum % r == 0 and minimum % r == 0:
#         return r
#     return gcd(maximum, r - 1)

# # Initial call with min(maximum, minimum)
# maximum = 14
# minimum = 12
# print(gcd(maximum, min(maximum, minimum)))






