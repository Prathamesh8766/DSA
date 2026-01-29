# def squreroot(num: int) -> int:
#     if num < 0:
#         raise ValueError("num must be non-negative")

#     low = 0
#     high = num
#     ans = 0

#     while low <= high:
#         mid = (low + high) // 2
#         if mid * mid <= num:
#             ans = mid
#             low = mid + 1
#         else:
#             high = mid - 1

#     return ans

# def main():
#     print(squreroot(int(input("Enter the number: "))))

# if __name__ == "__main__":
#     main()    

def function(root,n):
    high = root
    low = 1
    while low <= high :
        mid = (low + high) // 2
        if mid **n == root:
            return mid 
        elif mid **n < root:
            low = mid + 1
        else: high= mid -1
    return -1              
print(function(int(input("enter root: ")),int(input("Enter n: "))))