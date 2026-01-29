def kokoeatingbanana(nums, hours):
    high = max(nums) 
    low = 1
    ans = float("inf")
    
    while low <= high:
        mid = (low + high) // 2
        totalhours = 0
        for i in nums:
            totalhours += (i + mid - 1) // mid
        
        if totalhours <= hours:
            ans = mid
            high = mid - 1  
        else:
            low = mid + 1 
    
    return ans
def main():
    print(kokoeatingbanana(list(map(int,input("Enter the array space seprated: ").split())),int(input("Enter the max hours: "))))   

if __name__ == "__main__":
    main()     