def minimumNoOfDayToMakeMBought(nums,m,k):
    high = max(nums)
    low = 1
    ans = float("inf")
    while low <= high:
        mid = (low+ high) // 2
        count =0
        bought = 0
        totalDays= float("inf")
        for i in nums:
            if i <= mid :
                count += 1
                if count == k:
                    totalDays = mid
                    count = 0
                    bought += 1
                 
            else: count = 0     
        if totalDays <= ans and bought >= m :
            ans = totalDays
            high = mid -1
        else: low = mid + 1
    return  ans if ans != float("inf") else -1   
            

def minDays(bloomDay,m,k):
    if m*k > len(bloomDay):
        return -1
    low, high = 1, max(bloomDay)
    
    def canmake(days):
        bouquets = 0
        flower = 0
        for day in bloomDay:
            if day<= days:
                flower += 1
                if flower == k:
                    bouquets += 1
                    flower = 0
            else: flower = 0  
        if bouquets >=m:
              return  True
        else: return False  
    while low<= high:
        mid = (low + high) // 2
        if canmake(mid):
            high = mid - 1
        else: low = mid + 1
    return low     

                 
def main():
    bloomDays = list(map(int,input("Enter arry sepreted by space: ").split()))
    m = int(input("Enter number of bouquets: "))
    k = int(input("Enter k: "))
    
    print(minimumNoOfDayToMakeMBought(bloomDays,m,k))
    print(minDays(bloomDays,m,k))
    

if __name__=="__main__":
    main()
    
    